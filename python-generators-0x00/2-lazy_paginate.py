#!/usr/bin/python3
seed = __import__('seed')

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    offset = 0
    while True:  # we use only one loop (as required)
        page = paginate_users(page_size, offset)
        if not page:
            break  # stop when no more data
        yield page  # yield returns one page at a time (lazy loading)
        offset += page_size  # move to the next page
