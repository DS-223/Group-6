
from fastapi import FastAPI, HTTPException
from models import ProjectInput, ProjectOutput
from ads import router as ads_router
from typing import List

app = FastAPI()
app.include_router(ads_router)

# In-memory store
projects = []

@app.post("/projects", response_model=ProjectOutput)
def create_project(project: ProjectInput):
    """
    Create a new project with a unique project ID.

    Args:
        project (ProjectInput): Contains the project name, description, and number of bandits.

    Returns:
        ProjectOutput: The newly created project including the generated project ID.
    """
    new_id = max([p["project_id"] for p in projects], default=0) + 1
    new_project = {"project_id": new_id, **project.dict()}
    projects.append(new_project)
    return new_project

@app.get("/projects/{project_id}", response_model=ProjectOutput)

def get_project(project_id: int):
    """
    Retrieve a single project by its ID.

    Args:
        project_id (int): The unique ID of the project.

    Returns:
        ProjectOutput: The project details.

    Raises:
        HTTPException: If the project is not found.
    """
    for proj in projects:
        if proj["project_id"] == project_id:
            return proj
    raise HTTPException(status_code=404, detail="Project not found")
