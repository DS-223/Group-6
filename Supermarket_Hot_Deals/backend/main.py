
from fastapi import FastAPI, HTTPException, Depends
from schema import ProjectInput, ProjectOutput
from ads import router as ads_router
from typing import List
from database import get_db

from models import Project #TODO add your models

from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(ads_router)

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

