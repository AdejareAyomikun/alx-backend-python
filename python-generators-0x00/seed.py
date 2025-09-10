
import mysql.connector
from mysql.connector import errorcode
import csv
import uuid


def connect_db():
    """Connect to the MySQL server (no specific DB yet)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # adjust username if needed
            password="root"    # adjust password if needed
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Create the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev checked/created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    cursor.close()


def connect_to_prodev():
    """Connect directly to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # adjust username
            password="root",   # adjust password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """Create user_data table if not exists."""
    cursor = connection.cursor()
    table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    );
    """
    try:
        cursor.execute(table_query)
        connection.commit()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    cursor.close()


def insert_data(connection, csv_file):
    """Insert data from CSV file into user_data table if not already present."""
    cursor = connection.cursor()
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row["name"]
            email = row["email"]
            age = row["age"]

            # check if email already exists
            cursor.execute("SELECT * FROM user_data WHERE email = %s;", (email,))
            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age)
                )
    connection.commit()
    cursor.close()
