#!/usr/bin/python3
import mysql.connector


def stream_users():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # adjust if needed
            password="root",   # adjust if needed
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data;")

        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
