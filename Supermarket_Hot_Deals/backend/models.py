from pydantic import BaseModel
from typing import Optional




# -------------------------------
# USERS
# -------------------------------
class UserInput(BaseModel):
    email: str
    name: str

class UserOutput(UserInput):
    customer_id: int


# -------------------------------
# PROJECTS
# -------------------------------
class ProjectInput(BaseModel):
    project_name: str
    project_description: str
    number_of_bandits: int

class ProjectOutput(ProjectInput):
    project_id: int


# -------------------------------
# BANDITS / ADS
# -------------------------------
class BanditInput(BaseModel):
    project_id: int
    bandit_name: str

class BanditOutput(BaseModel):
    bandit_id: int
    #project_id: Optional[int] = None
    bandit_name: str
    alpha: float
    beta: float
    n: int
    number_of_success: int
    number_of_failures: int

class AdUpdate(BaseModel):
    bandit_name: Optional[str] = None
    alpha: Optional[float] = None
    beta: Optional[float] = None
    number_of_success: Optional[int] = None
    number_of_failures: Optional[int] = None
    n: Optional[int] = None


# -------------------------------
# TRANSACTIONS
# -------------------------------
class TransactionInput(BaseModel):
    customer_id: int
    project_id: int
    bandit_id: int
    clicked: bool

class TransactionOutput(TransactionInput):
    transaction_id: int
    timestamp: str




