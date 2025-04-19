import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="rootpassword",
        database="ab_test"
    )
    print("Successfully connected to MySQL database!")
    conn.close()
except mysql.connector.Error as err:
    print("Failed to connect:")
    print(err)
