from sqlalchemy import (
    Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    customer_id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    # Relationships
    transactions = relationship('Transaction', back_populates='customer')


class Project(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String, nullable=False)
    project_description = Column(Text)
    number_of_bandits = Column(Integer, nullable=False)

    # Relationships
    bandits = relationship('Bandit', back_populates='project')
    transactions = relationship('Transaction', back_populates='project')


class Bandit(Base):
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