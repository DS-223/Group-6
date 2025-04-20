import mysql.connector
<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 🔹 Updated model
class User(BaseModel):
    customer_id: int
    email: str
    name: str

class UpdateName(BaseModel):
    new_name: str
=======
>>>>>>> 4108254b50a1ef2648d123ea74faad9c4bc4fb88

def connect():
    return mysql.connector.connect(
        host="localhost",
<<<<<<< HEAD
        port=3306,
        user="ds_user",
        password="ds_password",
        database="ab_test"
    )

@app.post("/create")
def create_user(user: User):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (customer_id, email, name) VALUES (%s, %s, %s)",
        (user.customer_id, user.email, user.name)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created", "user": user}

@app.get("/users")
def get_all_users():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id, email, name FROM users")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        users = []
        for row in rows:
            users.append({
                "customer_id": row[0],
                "email": row[1],
                "name": row[2]
            })

        return {"users": users}

    except Exception as e:
        return {"error": str(e)}



@app.put("/update/{user_id}")
def update_user_name(user_id: int, update: UpdateName):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE customer_id = %s", (update.new_name, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated", "user_id": user_id}

@app.delete("/delete/{user_id}")
def delete_user(user_id: int):
=======
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
>>>>>>> 4108254b50a1ef2648d123ea74faad9c4bc4fb88
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM transactions WHERE customer_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE customer_id = %s", (user_id,))
        conn.commit()
<<<<<<< HEAD
        message = "User and related transactions deleted"
    except mysql.connector.IntegrityError:
        message = "Cannot delete user: linked transaction exists."
    cursor.close()
    conn.close()
    return {"message": message}

import pandas as pd

@app.on_event("startup")
def load_users_on_startup():
    try:
        df = pd.read_csv("/Users/ripsime/Downloads/Group-6/ds/simulated_data_tables/users.csv")
        conn = connect()
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT IGNORE INTO users (customer_id, email, name) VALUES (%s, %s, %s)",
                (int(row["customer_id"]), row["email"], row["name"])
            )
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Users loaded successfully.")
    except Exception as e:
        print("❌ Failed to load users:", e)
=======
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
>>>>>>> 4108254b50a1ef2648d123ea74faad9c4bc4fb88
