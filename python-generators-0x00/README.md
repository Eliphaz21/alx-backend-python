Project: Python Generators – Database Streaming
Overview

This project demonstrates the use of Python generators and database integration with MySQL.
The goal is to efficiently stream rows from a database one by one instead of loading the entire dataset into memory.

It also includes scripts to:

Connect to a MySQL server

Create and initialize a database (ALX_prodev)

Create a table (user_data)

Insert records from a CSV file (user_data.csv)

Stream data rows efficiently using generators

Learning Objectives

By the end of this project, you should be able to:

✅ Understand how Python generators work
✅ Stream large datasets efficiently using yield
✅ Connect and interact with MySQL using mysql.connector
✅ Create and populate databases programmatically
✅ Use context managers and handle database connections safely

Project Structure
python-generators-0x00/
│
├── seed.py # Handles database setup, connection, table creation, and data insertion
├── 0-main.py # Test script to verify database creation and table population
├── user_data.csv # Sample dataset for populating user_data table
└── README.md # Project documentation

Database Schema

Database: ALX_prodev
Table: user_data

Field Name Type Description
user_id UUID (Primary Key, Indexed) Unique user identifier
name VARCHAR User's full name
email VARCHAR User's email address
age DECIMAL User's age
Functions in seed.py
Function Description
connect_db() Connects to the MySQL server (without selecting a DB)
create_database(connection) Creates the ALX_prodev database if it doesn’t exist
connect_to_prodev() Connects to the ALX_prodev database
create_table(connection) Creates the user_data table if it doesn’t exist
insert_data(connection, data) Inserts user data from user_data.csv into the table
Usage Instructions

Ensure MySQL is running locally
Create a user with appropriate privileges (or use root).

Install dependencies

pip install mysql-connector-python

Run the main script

python3 0-main.py

Expected Output

connection successful
Table user_data created successfully
Database ALX_prodev is present
[('UUID1', 'Alice', 'alice@example.com', 25), ('UUID2', 'Bob', 'bob@gmail.com', 40), ...]

Python Generators – Coming Next

After seeding the database, the next tasks will involve creating a generator that streams rows one by one, such as:

def stream_users(connection):
cursor = connection.cursor()
cursor.execute("SELECT \* FROM user_data;")
for row in cursor:
yield row

This allows you to process large tables without memory overload.
