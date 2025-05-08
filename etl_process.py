import os
import pandas as pd
from loguru import logger
import random
import glob
from os import path

from Database.models import *
from Database.database import engine
from Database.data_generator import generate_users, generate_projects, generate_bandits, generate_transactions

NUM_USERS = 50
NUM_PROJECTS = 10
MAX_TRANSACTIONS = 500

os.makedirs("data", exist_ok=True)

users = generate_users(NUM_USERS)
users.to_csv("data/users.csv", index=False)
logger.info(f"Users: {users.shape}")

projects = generate_projects(NUM_PROJECTS)
projects.to_csv("data/projects.csv", index=False)
logger.info(f"Projects: {projects.shape}")

bandits = generate_bandits(projects)
bandits.to_csv("data/bandits.csv", index=False)
logger.info(f"Bandits: {bandits.shape}")

transactions = generate_transactions(users, projects, bandits, MAX_TRANSACTIONS)
transactions.to_csv("data/transactions.csv", index=False)
logger.info(f"Transactions: {transactions.shape}")

def load_csv_to_table(table_name: str, csv_path: str) -> None:
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    logger.info(f"✅ Data loaded into table: {table_name}")

folder_path = "data/*.csv"
files = glob.glob(folder_path)
base_names = [path.splitext(path.basename(file))[0] for file in files]

for table in base_names:
    try:
        logger.info(f"Loading table: {table}")
        load_csv_to_table(table, path.join("data", f"{table}.csv"))
    except Exception as e:
        logger.error(f"❌ Failed to load {table}: {e}")

print("All tables are populated successfully.")