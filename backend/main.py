from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dummy in-memory data
users = {
    1: {"id": 1, "email": "alice@example.com", "name": "Alice"},
    2: {"id": 2, "email": "bob@example.com", "name": "Bob"}
}

projects = [
    {"project_id": 1, "project_name": "Recommendation A/B Test", "project_description": "Testing 2 layouts", "number_of_bandits": 2}
]

bandits_by_project = {
    1: [
        {"bandit_id": 1, "bandit_name": "Layout A"},
        {"bandit_id": 2, "bandit_name": "Layout B"}
    ]
}

transactions_by_user = {
    1: [{"transaction_id": 1001, "project_id": 1, "bandit_id": 1, "clicked": True}],
    2: [{"transaction_id": 1002, "project_id": 1, "bandit_id": 2, "clicked": False}]
}

# Request model for adding bandits
class BanditInput(BaseModel):
    project_id: int
    bandit_name: str

# Endpoints
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.get("/projects/")
def get_projects():
    return projects

@app.get("/projects/{project_id}/bandits")
def get_bandits(project_id: int):
    return bandits_by_project.get(project_id, [])

@app.post("/bandits/")
def add_bandit(bandit: BanditInput):
    new_id = max([b["bandit_id"] for b in bandits_by_project.get(bandit.project_id, [])], default=0) + 1
    new_bandit = {"bandit_id": new_id, "bandit_name": bandit.bandit_name}
    bandits_by_project.setdefault(bandit.project_id, []).append(new_bandit)
    return new_bandit

@app.put("/bandits/{bandit_id}/reset")
def reset_bandit(bandit_id: int):
    return {"message": f"Bandit {bandit_id} stats reset (dummy response)."}

@app.get("/users/{user_id}/transactions")
def get_transactions(user_id: int):
    return transactions_by_user.get(user_id, [])
