import pandas as pd
import mysql.connector

df = pd.read_csv("simulated_data.csv")

df['timestamp'] = pd.to_datetime(df['timestamp'])

conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="rootpassword",
    database="ab_test"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sessions (
            user_id, session_id, layout_version, product_id,
            clicked, purchased, amount_spent, timestamp
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['user_id'],
        row['session_id'],
        row['layout_version'],
        row['product_id'],
        int(row['clicked']),
        int(row['purchased']),
        float(row['amount_spent']),
        row['timestamp']
    ))

conn.commit()
cursor.close()
conn.close()

print("Session data from CSV has been pushed to the database.")
