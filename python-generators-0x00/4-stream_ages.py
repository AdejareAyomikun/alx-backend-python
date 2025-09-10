import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:   # loop 1
        yield row["age"]

    cursor.close()
    connection.close()


def compute_average_age():
    """
    Computes average age using the generator stream_user_ages.
    Avoids loading entire dataset into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():   # loop 2
        total_age += age
        count += 1

    if count > 0:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found.")


if __name__ == "__main__":
    compute_average_age()
