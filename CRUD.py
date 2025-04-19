import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="rootpassword",
        database="ab_test"
    )

def create_user(email, name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, name) VALUES (%s, %s)", (email, name))
    conn.commit()
    cursor.close()
    conn.close()
    print("User created")

def get_all_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_user_name(user_id, new_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE customer_id = %s", (new_name, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("User updated")

def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM transactions WHERE customer_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE customer_id = %s", (user_id,))
        conn.commit()
        print("User and related transactions deleted")
    except mysql.connector.IntegrityError:
        print("Cannot delete user: linked transaction exists.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_user("test@example.com", "Test User")
    get_all_users()
    update_user_name(1, "Updated User")
    delete_user(1)
