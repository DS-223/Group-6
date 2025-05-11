from fastapi import APIRouter, HTTPException
from typing import List
from schema import BanditOutput, AdUpdate
from data import bandits_by_project
import random

router = APIRouter()


# 1. Get all ads
@router.get("/ads", response_model=List[BanditOutput], summary="Get all ads across all projects")
def get_all_ads():

    """
    Retrieve all ads from all projects.

    Returns:
        List[BanditOutput]: A list of all bandits with project ID injected.
    """
    
    all_ads = []
    for project_id, bandits in bandits_by_project.items():
        for b in bandits:
            b["project_id"] = project_id
            all_ads.append(BanditOutput(**b))
    return all_ads


# 2. Get top 3 ads after sampling (Thompson Sampling logic)
@router.get("/ads/sample", response_model=List[BanditOutput], summary="Get top 3 sampled ads for a project")
def get_sampled_ads(project_id: int):

    """
    Sample and return the top 3 ads for a project using Thompson Sampling.

    Args:
        project_id (int): The project identifier.

    Returns:
        List[BanditOutput]: Top 3 ads with highest sampled performance.

    Raises:
        HTTPException: If no ads are found for the given project.
    """
    
    bandits = bandits_by_project.get(project_id)
    if not bandits:
        raise HTTPException(status_code=404, detail="Project not found")

    sampled_ads = sorted(
        bandits,
        key=lambda b: random.betavariate(b["alpha"], b["beta"]),
        reverse=True
    )[:3]

    return [BanditOutput(**b) for b in sampled_ads]


# 3. Register a click on an ad

@router.post("/ads/{ad_id}/click", summary="Register a click on an ad")

def register_click(project_id: int, ad_id: int):
    """
    Register a successful click on an ad.

    Args:
        project_id (int): The project identifier.
        ad_id (int): The ad identifier.

    Returns:
        dict: A success message.

    Raises:
        HTTPException: If the ad is not found.
    """
    for b in bandits_by_project.get(project_id, []):
        if b["bandit_id"] == ad_id:
            b["number_of_success"] += 1
            b["n"] += 1
            return {"message": "Click registered"}
    raise HTTPException(status_code=404, detail="Ad not found")





# 4. Update ad details
@router.put("/ads/{ad_id}", summary="Update ad details")

def update_ad(project_id: int, ad_id: int, update: AdUpdate):
    """
    Update the details of a specific ad.

    Args:
        project_id (int): The project identifier.
        ad_id (int): The ad identifier.
        update (AdUpdate): Fields to update.

    Returns:
        dict: A success message.

    Raises:
        HTTPException: If the ad is not found.
    """
    for b in bandits_by_project.get(project_id, []):
        if b["bandit_id"] == ad_id:
            b.update(update.dict(exclude_unset=True))
            return {"message": "Ad updated successfully"}
    raise HTTPException(status_code=404, detail="Ad not found")


