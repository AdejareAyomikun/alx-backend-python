import mysql.connector


def stream_users_in_batches(batch_size):
    """Generator that yields rows from user_data in batches."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data;")
        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Process batches: filter users over age 25 and print them.
    Uses no more than 3 loops.
    """
    for batch in stream_users_in_batches(batch_size):     # loop 1
        for user in batch:                                # loop 2
            if int(user["age"]) > 25:
                print(user)
