from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
from loguru import logger
import os

fake = Faker()
random.seed(42)

NUM_USERS = 50
NUM_PROJECTS = 10
MAX_BANDITS_PER_PROJECT = 5
MAX_TRANSACTIONS = 500

logger.info("Starting data generation...")

def generate_users(num_users=NUM_USERS):
    users = []
    for user_id in range(1, num_users + 1):
        users.append({
            "customer_id": user_id,
            "email": fake.unique.email(),
            "name": fake.name()
        })
    df = pd.DataFrame(users)
    logger.success(f"Generated {len(df)} users.")
    return df


def generate_projects(num_projects=NUM_PROJECTS):
    projects = []
    for project_id in range(1, num_projects + 1):
        num_bandits = random.randint(1, MAX_BANDITS_PER_PROJECT)
        projects.append({
            "project_id": project_id,
            "project_name": fake.bs().capitalize(),
            "project_description": fake.text(max_nb_chars=100),
            "number_of_bandits": num_bandits
        })
    df = pd.DataFrame(projects)
    logger.success(f"Generated {len(df)} projects.")
    return df

def generate_bandits(projects_df):
    bandits = []
    bandit_id = 1
    for _, row in projects_df.iterrows():
        for _ in range(row['number_of_bandits']):
            alpha = random.uniform(0.5, 3.0)
            beta = random.uniform(0.5, 3.0)
            n = random.randint(10, 500)
            success = random.randint(0, n)
            failures = n - success

            bandits.append({
                "bandit_id": bandit_id,
                "project_id": row['project_id'],
                "bandit_name": fake.color_name() + "_" + fake.word(),
                "alpha": round(alpha, 2),
                "beta": round(beta, 2),
                "n": n,
                "number_of_success": success,
                "number_of_failures": failures
            })
            bandit_id += 1
    df = pd.DataFrame(bandits)
    logger.success(f"Generated {len(df)} bandits.")
    return df


def generate_transactions(users_df, projects_df, bandits_df, num_transactions=MAX_TRANSACTIONS):
    transactions = []
    for transaction_id in range(1, num_transactions + 1):
        user = users_df.sample().iloc[0]
        project = projects_df.sample().iloc[0]
        valid_bandits = bandits_df[bandits_df['project_id'] == project['project_id']]
        if valid_bandits.empty:
            continue
        bandit = valid_bandits.sample().iloc[0]

        timestamp = fake.date_time_between(start_date='-30d', end_date='now')
        clicked = random.choice([True, False])

        transactions.append({
            "transaction_id": transaction_id,
            "customer_id": user['customer_id'],
            "project_id": project['project_id'],
            "bandit_id": bandit['bandit_id'],
            "timestamp": timestamp,
            "clicked": clicked
        })
    df = pd.DataFrame(transactions)
    logger.success(f"Generated {len(df)} transactions.")
    return df


def main():
    users = generate_users()
    projects = generate_projects()
    bandits = generate_bandits(projects)
    transactions = generate_transactions(users, projects, bandits)

    # Save data to CSV (optional)
    output_dir = "generated_data"
    os.makedirs(output_dir, exist_ok=True)

    users.to_csv(os.path.join(output_dir, "users.csv"), index=False)
    projects.to_csv(os.path.join(output_dir, "projects.csv"), index=False)
    bandits.to_csv(os.path.join(output_dir, "bandits.csv"), index=False)
    transactions.to_csv(os.path.join(output_dir, "transactions.csv"), index=False)

    logger.success("All datasets have been saved to CSV.")

if __name__ == "__main__":
    main()
