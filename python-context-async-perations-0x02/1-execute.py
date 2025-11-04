import sqlite3

class ExecuteQuery:
    """
    Custom context manager to execute a SQL query with parameters
    and automatically handle database connection and cleanup.
    """
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.results = None

    def __enter__(self):
        # Open database connection
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        # Execute the query with parameters
        cursor.execute(self.query, self.params)
        # Fetch all results
        self.results = cursor.fetchall()
        return self.results  # The result will be assigned to the variable in 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection
        if self.conn:
            self.conn.close()
        # If exception occurred, it will propagate
        return False
