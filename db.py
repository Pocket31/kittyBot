import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        registered_date DATE
     )
    """
)

conn.commit()
conn.close()
