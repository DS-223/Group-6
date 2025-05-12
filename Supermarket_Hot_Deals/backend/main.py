from fastapi import FastAPI, HTTPException, Depends
from schema import ProjectInput, ProjectOutput
from typing import List
from database import get_db

from models import Project, Bandit #TODO add your models
from schema import BanditInput, BanditOutput
from sqlalchemy.orm import Session

app = FastAPI()

# In-memory store
projects = []

@app.post("/projects")
def create_project(project: ProjectInput, db: Session = Depends(get_db)):
    """
    Create a new project with a unique project ID.

    Args:
        project (ProjectInput): Contains the project name, description, and number of bandits.

    Returns:
        ProjectOutput: The newly created project including the generated project ID.
    """
    new_project = Project(
        project_id = project.project_id,
        project_name=project.project_name,
        project_description=project.project_description,
        number_of_bandits=project.number_of_bandits
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/project/{project_id}", response_model=ProjectOutput)

def get_project(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single project by its ID.

    Args:
        project_id (int): The unique ID of the project.

    Returns:
        ProjectOutput: The project details.

    Raises:
        HTTPException: If the project is not found.
    """
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    print('project', project)
    return project

@app.get("/projects", response_model=List[ProjectOutput])
def get_all_projects(db: Session = Depends(get_db)):
    """
    Retrieve all projects.

    Returns:
        List[ProjectOutput]: A list of all projects.
    """
    projects = db.query(Project).all()
    if not projects:
        raise HTTPException(status_code=404, detail="No projects found")    
    
    return projects

@app.post("/ads", response_model=BanditOutput)
def create_ad(bandit: BanditInput, db: Session = Depends(get_db)):
    # Check the project exists
    project = db.query(Project).filter(Project.project_id == bandit.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Create the new bandit
    new_bandit = Bandit(
        project_id=bandit.project_id,
        bandit_name=bandit.bandit_name,
        alpha=1.0,
        beta=1.0,
        n=0,
        number_of_success=0,
        number_of_failures=0
    )
    db.add(new_bandit)

    project.number_of_bandits += 1

    db.commit()
    db.refresh(new_bandit)
    return new_bandit

@app.get("/ads", response_model=List[BanditOutput])
def get_ads(project_id: int, db: Session = Depends(get_db)):
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return ads


from models import Transaction
from datetime import datetime

@app.post("/ads/{bandit_id}/click")
def register_click(project_id: int, bandit_id: int, db: Session = Depends(get_db)):
    bandit = db.query(Bandit).filter_by(bandit_id=bandit_id, project_id=project_id).first()
    if not bandit:
        raise HTTPException(status_code=404, detail="Ad not found")

    bandit.number_of_success += 1
    bandit.n += 1
    db.commit()

    # Optional: log transaction (if customer_id is handled)
    return {"message": "Click registered"}

import random
from schema import BanditOutput
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

@app.get("/ads/sample", response_model=List[BanditOutput])
def get_top_3_sampled_ads(project_id: int, db: Session = Depends(get_db)):
    bandits = db.query(Bandit).filter(Bandit.project_id == project_id).all()

    if not bandits:
        raise HTTPException(status_code=404, detail="No ads found for this project.")

    # Sample from Beta distribution for each ad
    sampled = sorted(
        bandits,
        key=lambda b: random.betavariate(b.alpha, b.beta),
        reverse=True
    )[:3]

    return sampled
@app.get("/analytics/clicks-per-ad")
def clicks_per_ad(project_id: int, db: Session = Depends(get_db)):
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return [{"bandit_name": ad.bandit_name, "clicks": ad.number_of_success} for ad in ads]

@app.get("/analytics/clicks-per-ad")
def clicks_per_ad(project_id: int, db: Session = Depends(get_db)):
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return {
        "labels": [ad.bandit_name for ad in ads],
        "values": [ad.number_of_success for ad in ads]
    }

@app.get("/analytics/project-bandits")
def get_project_bandits(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    bandits = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    
    return {
        "project_id": project_id,
        "bandits": [
            {"bandit_id": b.bandit_id, "bandit_name": b.bandit_name} for b in bandits
        ]
    }

