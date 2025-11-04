import mysql.connector
from mysql.connector import Error
import csv
import uuid

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YAbu199619##"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None

def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
    except Error as e:
        print("Error creating database:", e)

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YAbu199619##",
            database="ALX_prodev"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error connecting to ALX_prodev:", e)
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
        """
        cursor.execute(query)
        print("Table user_data created successfully")
    except Error as e:
        print("Error creating table:", e)

def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                cursor.execute(
                    "INSERT IGNORE INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, row['name'], row['email'], row['age'])
                )
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print("Error inserting data:", e)

def stream_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
