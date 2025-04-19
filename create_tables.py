import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="rootpassword"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ab_test")
cursor.execute("USE ab_test")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255),
    name VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(255),
    project_description TEXT,
    number_of_bandits INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bandits (
    bandit_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    bandit_name VARCHAR(255),
    alpha FLOAT,
    beta FLOAT,
    n INT,
    number_of_success INT,
    number_of_failures INT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    project_id INT,
    bandit_id INT,
    timestamp DATETIME,
    clicked BOOLEAN,
    FOREIGN KEY (customer_id) REFERENCES users(customer_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (bandit_id) REFERENCES bandits(bandit_id)
)
""")

print(" Database and tables created.")

cursor.close()
conn.close()
