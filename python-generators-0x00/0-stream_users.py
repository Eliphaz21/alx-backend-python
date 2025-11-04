import mysql.connector

def stream_users():
    """
    Generator function that streams user records from the user_data table one by one.
    Each row is yielded as a dictionary.
    """
    try:
        # Step 1: Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          # change this if your MySQL user is different
            password='YAbu199619##',  # update this with your real password
            database='ALX_prodev'
        )

        # Step 2: Create a cursor that returns dictionaries instead of tuples
        cursor = connection.cursor(dictionary=True)

        # Step 3: Execute the query
        cursor.execute("SELECT * FROM user_data")

        # Step 4: Fetch and yield each row one by one
        for row in cursor:
            yield row   # <-- the generator part

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        # Step 5: Close cursor and connection safely
        if cursor:
            cursor.close()
        if connection:
            connection.close()
