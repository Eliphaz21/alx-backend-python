import sqlite3
import functools

# --------------- Previous decorator ---------------
# Automatically opens and closes the DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open DB connection
        try:
            return func(conn, *args, **kwargs)  # Pass connection to function
        finally:
            conn.close()  # Ensure connection is closed
    return wrapper

# --------------- Transaction decorator ---------------
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)  # Run the function
            conn.commit()  # Commit changes if no exception
            print("[TRANSACTION] Committed successfully.")
            return result
        except Exception as e:
            conn.rollback()  # Rollback changes if exception
            print(f"[TRANSACTION] Rolled back due to error: {e}")
            raise  # Re-raise the exception
    return wrapper

# --------------- Example usage ---------------
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET email = ? WHERE id = ?", 
        (new_email, user_id)
    )
    print(f"User {user_id} email updated to {new_email}")

# Run the function
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
