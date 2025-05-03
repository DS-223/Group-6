import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="rootpassword",
        database="ab_test"
    )

def get_user_by_id(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE customer_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_projects():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_bandits_by_project(project_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bandits WHERE project_id = %s", (project_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_transactions_by_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE customer_id = %s", (user_id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def reset_bandit_stats(bandit_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE bandits
        SET number_of_success = 0, number_of_failures = 0, alpha = 1.0, beta = 1.0, n = 0
        WHERE bandit_id = %s
    """, (bandit_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Bandit {bandit_id} stats reset.")

def add_bandit(project_id, bandit_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bandits (project_id, bandit_name, alpha, beta, n, number_of_success, number_of_failures)
        VALUES (%s, %s, 1.0, 1.0, 0, 0, 0)
    """, (project_id, bandit_name))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Bandit '{bandit_name}' added to project {project_id}")



