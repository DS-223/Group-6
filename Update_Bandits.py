import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword",
    database="ab_test"
)

cursor = conn.cursor()

click_occurred = random.choice([True, False])

if click_occurred:
    cursor.execute("""
        UPDATE bandits
        SET number_of_success = number_of_success + 1,
            n = n + 1,
            alpha = alpha + 1
        WHERE bandit_id = 1
    """)
else:
    cursor.execute("""
        UPDATE bandits
        SET number_of_failures = number_of_failures + 1,
            n = n + 1,
            beta = beta + 1
        WHERE bandit_id = 1
    """)

conn.commit()
print(f"Click {'SUCCESS' if click_occurred else 'FAILURE'} simulated for Layout A.")
cursor.close()
conn.close()
