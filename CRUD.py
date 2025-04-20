import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    customer_id: int
    email: str
    name: str

class UpdateName(BaseModel):
    new_name: str

def connect():
    return mysql.connector.connect(
        host="localhost",
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
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM transactions WHERE customer_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE customer_id = %s", (user_id,))
        conn.commit()
        message = "User and related transactions deleted"
    except mysql.connector.IntegrityError:
        message = "Cannot delete user: linked transaction exists."
    cursor.close()
    conn.close()
    return {"message": message}
