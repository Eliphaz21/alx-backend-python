import sqlite3

def stream_users_in_batches(batch_size):
    """
    Generator that fetches user data in batches from the users database.
    """
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Count total rows
    cursor.execute("SELECT COUNT(*) FROM user_data")
    total_rows = cursor.fetchone()[0]

    # Fetch users in batches using yield
    for offset in range(0, total_rows, batch_size):
        cursor.execute("SELECT user_id, name, email, age FROM user_data LIMIT ? OFFSET ?", (batch_size, offset))
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch  # yield each batch to the processor

    conn.close()


def batch_processing(batch_size):
    """
    Processes each batch and filters users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        # Filter users older than 25
        for user in batch:
            user_dict = {
                "user_id": user[0],
                "name": user[1],
                "email": user[2],
                "age": user[3]
            }
            if user_dict["age"] > 25:
                print(user_dict)
