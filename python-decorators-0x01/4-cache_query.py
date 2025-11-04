import time
import sqlite3
import functools

# ----------------- Cache dictionary -----------------
query_cache = {}

# ----------------- with_db_connection decorator -----------------
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')  # Open DB connection
        try:
            return func(conn, *args, **kwargs)  # Pass connection to function
        finally:
            conn.close()  # Ensure connection is closed
    return wrapper

# ----------------- cache_query decorator -----------------
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[1] if len(args) > 1 else None)
        if query is None:
            raise ValueError("Query must be provided as an argument or keyword argument")
        
        if query in query_cache:
            print("[CACHE] Returning cached result")
            return query_cache[query]
        
        print("[CACHE] Query not cached, fetching from database")
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

# ----------------- Example usage -----------------
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ----------------- Test -----------------
# First call → fetches from DB
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call → uses cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
