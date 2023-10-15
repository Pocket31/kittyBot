import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        registered_date DATE,
        trc_20_wallet_address TEXT,
        trc_20_wallet_private_key TEXT
     )
    """
)
# conn.execute('ALTER TABLE users ADD trc_20_wallet_private_key TEXT')
conn.commit()
conn.close()
