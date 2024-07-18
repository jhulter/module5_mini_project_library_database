import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = "library"
    user = "root"
    password = "Theezfoot7!"
    host = "127.0.0.1"

    try:
        # Attempt to establish a connection
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        # Check if connection is successful
        if conn.is_connected():
            print("Connected to MySQL Database successful.")
            return conn

    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
