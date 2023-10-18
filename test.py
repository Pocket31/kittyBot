import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute(
    f"SELECT * FROM users WHERE user_id=253833381")
user_info = cursor.fetchone()
print(user_info)
