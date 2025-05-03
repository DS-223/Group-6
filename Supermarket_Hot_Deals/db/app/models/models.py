"""
This module defines all database models (ORM mappings) for the Supermarket Hot Deals project.
Each class corresponds to a table in the database and includes relationships for joined queries.
"""

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base


class User(Base):
    """
    Represents a customer using the supermarket platform.

    Attributes:
        customer_id (int): Primary key, uniquely identifies the user.
        email (str): Customer's email address (must be unique).
        name (str): Full name of the customer.
    Relationships:
        transactions (List[Transaction]): All purchases or clicks made by the user.
    """
    __tablename__ = "users"

    customer_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="customer")


class Project(Base):
    """
    Represents a marketing campaign or product group (e.g., "Weekly Hot Deals").

    Attributes:
        project_id (int): Primary key.
        project_name (str): Descriptive name of the promotion or product group.
        project_description (str): Optional long description.
        number_of_bandits (int): Number of variants in the campaign.
    Relationships:
        bandits (List[Bandit]): Available variants in the promotion.
        transactions (List[Transaction]): Purchases associated with this campaign.
    """
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    project_description = Column(Text)
    number_of_bandits = Column(Integer)

    bandits = relationship("Bandit", back_populates="project")
    transactions = relationship("Transaction", back_populates="project")

class Bandit(Base):
    """
    Represents a promotional option or variant within a campaign.

    Attributes:
        bandit_id (int): Primary key.
        project_id (int): Foreign key linking to a campaign.
        bandit_name (str): Name or label for this variant.
        alpha (float): Success prior (Bayesian A/B testing), default = 1.
        beta (float): Failure prior (Bayesian A/B testing), default = 1.
        n (int): Total trials.
        number_of_success (int): Number of successful clicks or purchases, default = 0.
        number_of_failures (int): Number of unsuccessful trials, default = 0.
    Relationships:
        project (Project): The project this bandit belongs to.
        transactions (List[Transaction]): All transactions that used this bandit.
    """
    __tablename__ = "bandits"

    bandit_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    bandit_name = Column(String, nullable=False)
    alpha = Column(Float, default=1)
    beta = Column(Float, default=1)
    n = Column(Integer)
    number_of_success = Column(Integer, default=0)
    number_of_failures = Column(Integer, default=0)

    project = relationship("Project", back_populates="bandits")
    transactions = relationship("Transaction", back_populates="bandit")


class Transaction(Base):
    """
    Represents a customer interaction with a campaign or product (e.g., click or purchase).

    Attributes:
        transaction_id (int): Primary key.
        customer_id (int): Foreign key referencing the user.
        project_id (int): Foreign key referencing the campaign.
        bandit_id (int): Foreign key referencing the variant shown.
        timestamp (datetime): Time of the transaction.
        clicked (bool): Whether the user clicked/purchased (conversion).
    Relationships:
        customer (User): The customer who performed the transaction.
        project (Project): The campaign associated with the transaction.
        bandit (Bandit): The specific variant shown.
    """
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.customer_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    bandit_id = Column(Integer, ForeignKey("bandits.bandit_id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    clicked = Column(Boolean, default=False)

    customer = relationship("User", back_populates="transactions")
    project = relationship("Project", back_populates="transactions")
    bandit = relationship("Bandit", back_populates="transactions")


class Prediction(Base):
    """
    Stores the output of predictive models for customer interactions.

    Attributes:
        prediction_id (int): Primary key.
        customer_id (int): Foreign key referencing the customer.
        project_id (int): Foreign key referencing the promotion/project.
        bandit_id (int): Optional foreign key referencing the shown variant.
        timestamp (datetime): When the prediction was generated.
        predicted_score (float): Model output, such as click probability.
        model_version (str): Version tag or identifier of the predictive model.
    Relationships:
        customer (User): The user for whom prediction is made.
        project (Project): The campaign associated with prediction.
        bandit (Bandit): Optional variant associated.
    """
    __tablename__ = "predictions"

    prediction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.customer_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    bandit_id = Column(Integer, ForeignKey("bandits.bandit_id"), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    predicted_score = Column(Float, nullable=False)
    model_version = Column(String, nullable=False)

    customer = relationship("User")
    project = relationship("Project")
    bandit = relationship("Bandit")

