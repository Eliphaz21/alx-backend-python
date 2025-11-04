import asyncio
import aiosqlite

DB_FILE = "my_database.db"

# Async function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            result = await cursor.fetchall()
            print("All users:")
            for row in result:
                print(row)
            return result

# Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect(DB_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            result = await cursor.fetchall()
            print("Users older than 40:")
            for row in result:
                print(row)
            return result

# Run both queries concurrently
async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    # results[0] -> all users, results[1] -> users older than 40
    return results

# Entry point
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
