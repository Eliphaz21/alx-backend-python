#!/usr/bin/python3
import sqlite3

def stream_users_in_batches(batch_size):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM users")
    
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows
    
    conn.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            user_data = {
                "user_id": user[0],
                "name": user[1],
                "email": user[2],
                "age": user[3]
            }
            if user_data["age"] > 25:
                print(user_data)
