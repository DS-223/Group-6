#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import sys
import random  
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone

from sqlalchemy.orm import Session
from models import Project, Bandit
from database import engine


# In[3]:


PROJECT_NAME = "Supermarket Hot Deals Thompson Experiment"
NUM_PRODUCTS = 6   
PRODUCTS_PER_PAGE = 3


# In[5]:


RESET = False  # Set to True if you want to delete and recreate bandits

with Session(engine) as session:

    project = session.query(Project).filter(Project.project_name == PROJECT_NAME).first()
    if not project:
        project = Project(
            project_name=PROJECT_NAME,
            project_description="Auto-created test for modeling",
            number_of_bandits=NUM_PRODUCTS
        )
        session.add(project)
        session.commit()
        print(f"Created new project with id: {project.project_id}")
    else:
        print(f"Using existing project with id: {project.project_id}")

    project_id = project.project_id

    if RESET:
        session.query(Bandit).filter(Bandit.project_id == project_id).delete()
        session.commit()
        print("Old bandits deleted.")

    existing = session.query(Bandit).filter(Bandit.project_id == project_id).count()
    if existing == 0:
        for i in range(NUM_PRODUCTS):
            bandit = Bandit(
                project_id=project_id,
                bandit_name=f"Product {i+1}",
                alpha=random.randint(1, 5),
                beta=random.randint(1, 5),
                n=0,
                number_of_success=0,
                number_of_failures=0
            )
            session.add(bandit)
        session.commit()
        print(f"Added {NUM_PRODUCTS} bandits.")
    else:
        print(f"{existing} bandits already exist for this project.")

def get_page_recommendations(project_id, page_num=0):
    with Session(engine) as session:
        bandits = session.query(Bandit).filter(Bandit.project_id == project_id).all()
        samples = [np.random.beta(b.alpha, b.beta) for b in bandits]
        sorted_bandits = [b for _, b in sorted(zip(samples, bandits), key=lambda pair: pair[0], reverse=True)]
        start = page_num * PRODUCTS_PER_PAGE
        end = start + PRODUCTS_PER_PAGE
        return sorted_bandits[start:end]

for p in range(2):
    print(f"\nRecommended products on page {p+1}:")
    recs = get_page_recommendations(project_id=project_id, page_num=p)
    for b in recs:
        print(f"{b.bandit_name} (alpha={b.alpha}, beta={b.beta})")

def simulate_click(bandit: Bandit, clicked: bool):
    with Session(engine) as session:
        db_bandit = session.query(Bandit).filter(Bandit.bandit_id == bandit.bandit_id).first()
        if clicked:
            db_bandit.alpha += 1
            db_bandit.number_of_success += 1
        else:
            db_bandit.beta += 1
            db_bandit.number_of_failures += 1
        db_bandit.n += 1
        session.commit()

simulate_click(recs[0], clicked=True)
simulate_click(recs[1], clicked=False)

Thompson Sampling algorithm to recommend supermarket products. It first looks for an existing project in the database; if none is found, it creates one. Then it checks for associated products (bandits). If none exist, it adds new ones with random alpha and beta values, which are used in the Beta distribution to calculate selection probabilities. The get_page_recommendations() function ranks products by sampling from their distributions and shows the top ones per page. Simulated clicks update each product’s success or failure, helping the model learn over time which products perform better.