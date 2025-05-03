import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="rootpassword",
    database="ab_test"
)
cursor = conn.cursor()

cursor.execute("DELETE FROM transactions")
cursor.execute("DELETE FROM bandits")
cursor.execute("DELETE FROM projects")
cursor.execute("DELETE FROM users")


users = pd.read_csv("users.csv")
for _, row in users.iterrows():
    cursor.execute(
        "INSERT INTO users (customer_id, email, name) VALUES (%s, %s, %s)",
        (int(row['customer_id']), row['email'], row['name'])
    )

projects = pd.read_csv("projects.csv")
for _, row in projects.iterrows():
    cursor.execute(
        "INSERT INTO projects (project_id, project_name, project_description, number_of_bandits) VALUES (%s, %s, %s, %s)",
        (int(row['project_id']), row['project_name'], row['project_description'], int(row['number_of_bandits']))
    )

bandits = pd.read_csv("bandits.csv")
for _, row in bandits.iterrows():
    cursor.execute(
        """INSERT INTO bandits (bandit_id, project_id, bandit_name, alpha, beta, n, number_of_success, number_of_failures)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        (
            int(row['bandit_id']), int(row['project_id']), row['bandit_name'],
            float(row['alpha']), float(row['beta']), int(row['n']),
            int(row['number_of_success']), int(row['number_of_failures'])
        )
    )

transactions = pd.read_csv("transactions.csv")
transactions['timestamp'] = pd.to_datetime(transactions['timestamp'])  # ensure datetime format
for _, row in transactions.iterrows():
    cursor.execute(
        """INSERT INTO transactions (transaction_id, customer_id, project_id, bandit_id, timestamp, clicked)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (
            int(row['transaction_id']), int(row['customer_id']), int(row['project_id']), int(row['bandit_id']),
            row['timestamp'].to_pydatetime(), bool(row['clicked'])
        )
    )

conn.commit()
cursor.close()
conn.close()

print("All data from CSV files has been pushed to the database.")

