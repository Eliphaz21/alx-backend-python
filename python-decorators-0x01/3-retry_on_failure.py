import time
import sqlite3
import functools

# ----------------- with_db_connection decorator -----------------
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open connection
        try:
            return func(conn, *args, **kwargs)  # Pass connection
        finally:
            conn.close()  # Ensure connection is closed
    return wrapper

# ----------------- retry_on_failure decorator -----------------
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    result = func(*args, **kwargs)
                    print(f"[RETRY] Success on attempt {attempt}")
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        time.sleep(delay)
            # After all retries, raise the last exception
            print(f"[RETRY] All {retries} attempts failed.")
            raise last_exception
        return wrapper
    return decorator

# ----------------- Example usage -----------------
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# ----------------- Run the function -----------------
users = fetch_users_with_retry()
print(users)
