import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="rootpassword",
    database="ab_test"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO users (email, name)
VALUES ('user1@example.com', 'Alice')
""")

cursor.execute("""
INSERT INTO projects (project_name, project_description, number_of_bandits)
VALUES ('Hot Deals Layout Test', 'Testing layout versions A and B for CTR', 2)
""")

cursor.execute("""
INSERT INTO bandits (project_id, bandit_name, alpha, beta, n, number_of_success, number_of_failures)
VALUES 
  (1, 'Layout A', 1.0, 1.0, 0, 0, 0),
  (1, 'Layout B', 1.0, 1.0, 0, 0, 0)
""")

cursor.execute("""
INSERT INTO transactions (customer_id, project_id, bandit_id, timestamp, clicked)
VALUES (1, 1, 1, NOW(), TRUE)
""")

conn.commit()
print(" Sample data inserted.")
cursor.close()
conn.close()
