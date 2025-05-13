from sqlalchemy import (
    Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

class User(Base):
    """
    Represents a customer/user in the system.
    Each user can perform multiple transactions.
    """
    __tablename__ = 'users'

    customer_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    # Relationships
    transactions = relationship('Transaction', back_populates='customer')


class Project(Base):
    """
    Represents a project that contains multiple bandits.
    Projects are used to group related bandits and experiments.
    """
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String, nullable=False)
    project_description = Column(Text)
    number_of_bandits = Column(Integer, nullable=False)

    # Relationships
    bandits = relationship('Bandit', back_populates='project')
    transactions = relationship('Transaction', back_populates='project')


class Bandit(Base):
    """
    Represents an individual bandit (variant/option) in a multi-armed bandit algorithm.
    Tracks statistics like alpha, beta, number of successes/failures for Thompson Sampling.
    """
    __tablename__ = 'bandits'

    bandit_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    bandit_name = Column(String, nullable=False)

    alpha = Column(Float, nullable=False)
    beta = Column(Float, nullable=False)
    n = Column(Integer, nullable=False)
    number_of_success = Column(Integer, nullable=False)
    number_of_failures = Column(Integer, nullable=False)

    # Relationships
    project = relationship('Project', back_populates='bandits')
    transactions = relationship('Transaction', back_populates='bandit')


class Transaction(Base):
    """
    Represents a single interaction or event where a user was shown a bandit (variant).
    Records whether the user clicked (success) or not.
    """
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('users.customer_id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    bandit_id = Column(Integer, ForeignKey('bandits.bandit_id'), nullable=False)

    timestamp = Column(DateTime, nullable=False)
    clicked = Column(Boolean, default=False)

    # Relationships
    customer = relationship('User', back_populates='transactions')
    project = relationship('Project', back_populates='transactions')
    bandit = relationship('Bandit', back_populates='transactions')


Base.metadata.create_all(engine, checkfirst=True)

print("Database tables created or already exist.")
# This will create the tables in the database if they do not already exist.
    
