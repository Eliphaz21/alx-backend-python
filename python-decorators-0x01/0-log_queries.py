import sqlite3
import functools
from datetime import datetime  # Needed for timestamp logging

# Decorator to log SQL queries with timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
        
        # Log the SQL query with current timestamp
        print(f"[{datetime.now()}] Executing SQL Query: {query}")
        
        result = func(*args, **kwargs)
        
        print(f"[{datetime.now()}] Query executed successfully.\n")
        return result
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)
