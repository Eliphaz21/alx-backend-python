import sqlite3

class DatabaseConnection:
    """
    Custom context manager for handling SQLite database connections.
    Ensures that the connection is properly closed even if exceptions occur.
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        # Open the database connection
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the database connection
        if self.conn:
            self.conn.close()
        # Returning False propagates any exception, True suppresses it
        return False

# Example usage
if __name__ == "__main__":
    db_file = "my_database.db"  # Replace with your database file

    with DatabaseConnection(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()

        print("Users in database:")
        for row in results:
            print(row)
