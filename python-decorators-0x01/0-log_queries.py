import sqlite3
import functools

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query argument (assuming it's named 'query' or passed positionally)
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
        
        # Log the SQL query before execution
        print(f"[LOG] Executing SQL Query: {query}")
        
        # Call the actual function
        result = func(*args, **kwargs)
        
        # Optionally log after execution
        print("[LOG] Query executed successfully.\n")
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
