#!/usr/bin/python3
import sqlite3


def stream_users_in_batches(batch_size):
    """
    Generator that fetches user data in batches from user_data table.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Get total number of users
    cursor.execute("SELECT COUNT(*) FROM user_data")
    total = cursor.fetchone()[0]

    # Stream users in batches
    for offset in range(0, total, batch_size):
        cursor.execute(
            "SELECT user_id, name, email, age FROM user_data LIMIT ? OFFSET ?",
            (batch_size, offset)
        )
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows  # ✅ yield each batch — no return used

    conn.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter and print users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):  # first loop
        for user in batch:  # second loop
            user_info = {
                "user_id": user[0],
                "name": user[1],
                "email": user[2],
                "age": user[3]
            }
            if user_info["age"] > 25:
                print(user_info)
