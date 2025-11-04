#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    """
    Generator that streams user ages one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield age  # yield sends one value at a time (lazy)
    
    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Calculates the average age of all users using the generator.
    """
    total_age = 0
    count = 0

    # First loop: iterate through all ages one by one
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Compute average after streaming completes
    average_age = total_age / count if count > 0 else 0
    print(f"Average age of users: {average_age:.2f}")
