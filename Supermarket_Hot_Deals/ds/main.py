from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI()

# Dummy in-memory data
users = {
    1: {"customer_id": 1, "email": "alice@example.com", "name": "Alice"},
    2: {"customer_id": 2, "email": "bob@example.com", "name": "Bob"}
}

projects = [
    {"project_id": 1, "project_name": "Layout Test", "project_description": "A/B/C test", "number_of_bandits": 2}
]

bandits_by_project = {
    1: [
        {"bandit_id": 1, "bandit_name": "Layout A", "alpha": 1.0, "beta": 1.0, "n": 0, "number_of_success": 0, "number_of_failures": 0},
        {"bandit_id": 2, "bandit_name": "Layout B", "alpha": 1.0, "beta": 1.0, "n": 0, "number_of_success": 0, "number_of_failures": 0}
    ]
}

transactions_by_user = {
    1: [
        {"transaction_id": 1001, "project_id": 1, "bandit_id": 1, "timestamp": "2025-04-20T10:00:00", "clicked": True}
    ]
}

# Request models
class UserInput(BaseModel):
    email: str
    name: str

class ProjectInput(BaseModel):
    project_name: str
    project_description: str
    number_of_bandits: int

class BanditInput(BaseModel):
    project_id: int
    bandit_name: str

class TransactionInput(BaseModel):
    customer_id: int
    project_id: int
    bandit_id: int
    clicked: bool

# USERS
@app.get("/users")
def get_users():
    return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users")
def create_user(user: UserInput):
    new_id = max(users.keys(), default=0) + 1
    new_user = {"customer_id": new_id, **user.dict()}
    users[new_id] = new_user
    return new_user

# PROJECTS
@app.get("/projects")
def get_projects():
    return projects

@app.get("/projects/{project_id}")
def get_project(project_id: int):
    for proj in projects:
        if proj["project_id"] == project_id:
            return proj
    raise HTTPException(status_code=404, detail="Project not found")

@app.post("/projects")
def create_project(project: ProjectInput):
    new_id = max([p["project_id"] for p in projects], default=0) + 1
    new_project = {"project_id": new_id, **project.dict()}
    projects.append(new_project)
    return new_project

# BANDITS
@app.get("/projects/{project_id}/bandits")
def get_bandits(project_id: int):
    return bandits_by_project.get(project_id, [])

@app.post("/projects/{project_id}/bandits")
def add_bandit(project_id: int, bandit: BanditInput):
    bandits = bandits_by_project.get(project_id, [])
    new_id = max([b["bandit_id"] for b in bandits], default=0) + 1
    new_bandit = {
        "bandit_id": new_id,
        "bandit_name": bandit.bandit_name,
        "alpha": 1.0, "beta": 1.0, "n": 0, "number_of_success": 0, "number_of_failures": 0
    }
    bandits_by_project.setdefault(project_id, []).append(new_bandit)
    return new_bandit

@app.put("/bandits/{bandit_id}/reset")
def reset_bandit(bandit_id: int):
    for bandits in bandits_by_project.values():
        for bandit in bandits:
            if bandit["bandit_id"] == bandit_id:
                bandit["alpha"] = 1.0
                bandit["beta"] = 1.0
                bandit["n"] = 0
                bandit["number_of_success"] = 0
                bandit["number_of_failures"] = 0
                return {"message": f"Bandit {bandit_id} stats reset."}
    raise HTTPException(status_code=404, detail="Bandit not found")

# TRANSACTIONS
@app.get("/users/{user_id}/transactions")
def get_transactions(user_id: int):
    return transactions_by_user.get(user_id, [])

@app.post("/transactions")
def add_transaction(tx: TransactionInput):
    user_txs = transactions_by_user.setdefault(tx.customer_id, [])
    new_id = max([t["transaction_id"] for t in user_txs], default=1000) + 1
    tx_record = {
        "transaction_id": new_id,
        "project_id": tx.project_id,
        "bandit_id": tx.bandit_id,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "clicked": tx.clicked
    }
    user_txs.append(tx_record)
    return tx_record

# RECOMMENDATION (SIMULATED)
@app.get("/projects/{project_id}/recommend_bandit")
def recommend_bandit(project_id: int):
    bandits = bandits_by_project.get(project_id, [])
    if not bandits:
        raise HTTPException(status_code=404, detail="No bandits found")
    # Simulate Thompson Sampling logic (very simplified)
    scores = [(b["bandit_id"], (b["number_of_success"] + 1) / (b["n"] + 2)) for b in bandits]
    best = max(scores, key=lambda x: x[1])[0]
    for b in bandits:
        if b["bandit_id"] == best:
            return b
