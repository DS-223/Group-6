from fastapi import FastAPI, HTTPException, Depends
from schema import ProjectInput, ProjectOutput
from typing import List
from database import get_db
from models import Project, Bandit 
from schema import BanditInput, BanditOutput
from sqlalchemy.orm import Session
import random
from fastapi import Depends, HTTPException
from models import Transaction
from datetime import datetime

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
    """
    Create a new ad (bandit) for a given project.

    This endpoint initializes a new bandit under a specific project with
    default parameters for Thompson Sampling (alpha=1.0, beta=1.0, n=0, etc.).

    Args:
        bandit (BanditInput): Input data containing the project ID and the name of the bandit.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        BanditOutput: The newly created bandit's data including its initialized values.

    Raises:
        HTTPException: If the specified project does not exist (404).
    """
    project = db.query(Project).filter(Project.project_id == bandit.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

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
    """
    Retrieve all ads (bandits) for a given project.

    This endpoint returns a list of all bandits that belong to the specified project.

    Args:
        project_id (int): The unique ID of the project whose ads are being requested.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        List[BanditOutput]: A list of bandits associated with the specified project.
    """
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return ads



@app.post("/ads/{bandit_id}/click")
def register_click(project_id: int, bandit_id: int, db: Session = Depends(get_db)):
    """
    Register a click (success) for a specific ad (bandit) in a project.

    This endpoint increments the number of successes and the total impression count
    for a given bandit, simulating a user clicking on the ad.

    Args:
        project_id (int): The ID of the project the bandit belongs to.
        bandit_id (int): The ID of the bandit (ad) to register the click for.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        dict: A success message confirming that the click has been registered.

    Raises:
        HTTPException: If the bandit with the specified ID and project ID is not found (404).
    """
    bandit = db.query(Bandit).filter_by(bandit_id=bandit_id, project_id=project_id).first()
    if not bandit:
        raise HTTPException(status_code=404, detail="Ad not found")

    bandit.number_of_success += 1
    bandit.n += 1
    db.commit()

    return {"message": "Click registered"}


@app.get("/ads/sample", response_model=List[BanditOutput])
def get_top_3_sampled_ads(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the top 3 sampled ads (bandits) for a given project using Thompson Sampling.

    This endpoint performs sampling from the Beta distribution for each bandit and returns
    the top 3 ads with the highest sampled values. This is used for selecting which ads to display
    based on learned performance.

    Args:
        project_id (int): The unique ID of the project whose bandits are being sampled.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        List[BanditOutput]: A list of the top 3 bandits sampled by Thompson Sampling.

    Raises:
        HTTPException: If no bandits are found for the given project (404).
    """
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
    """
    Retrieve the number of clicks (successes) per ad (bandit) for a given project.

    This endpoint returns a list of dictionaries showing the name of each ad and the number
    of clicks it has received, allowing simple analytics and performance monitoring.

    Args:
        project_id (int): The unique ID of the project to retrieve ad performance for.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        List[dict]: A list of dictionaries with each containing:
            - 'bandit_name': The name of the ad (str)
            - 'clicks': Number of successful clicks (int)
    """ 
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return [{"bandit_name": ad.bandit_name, "clicks": ad.number_of_success} for ad in ads]

@app.get("/analytics/clicks-per-ad")
def clicks_per_ad(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve ad performance data (clicks) formatted for charting purposes.

    This endpoint returns a dictionary with two parallel lists: 'labels' for ad names and
    'values' for the corresponding number of clicks. Useful for generating bar charts or
    other visualizations.

    Args:
        project_id (int): The unique ID of the project to retrieve ad performance for.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        dict: A dictionary with:
            - 'labels' (List[str]): Names of the ads (bandits)
            - 'values' (List[int]): Number of clicks per ad
    """
    ads = db.query(Bandit).filter(Bandit.project_id == project_id).all()
    return {
        "labels": [ad.bandit_name for ad in ads],
        "values": [ad.number_of_success for ad in ads]
    }

@app.get("/analytics/project-bandits")
def get_project_bandits(project_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all bandits (ads) associated with a specific project.

    This endpoint returns the project ID along with a list of all bandits under that project,
    including each bandit's ID and name. Useful for displaying available ad options in a project.

    Args:
        project_id (int): The unique ID of the project to retrieve bandits from.
        db (Session, optional): SQLAlchemy database session. Automatically provided by FastAPI.

    Returns:
        dict: A dictionary containing:
            - 'project_id' (int): The ID of the project
            - 'bandits' (List[dict]): A list of dictionaries, each with:
                - 'bandit_id' (int): The ID of the bandit
                - 'bandit_name' (str): The name of the bandit

    Raises:
        HTTPException: If the project with the given ID is not found (404).
    """
    
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



