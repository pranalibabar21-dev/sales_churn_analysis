import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute(
    "SELECT * FROM users WHERE username=?",
    ("admin",)
)

admin = cursor.fetchone()

if not admin:

    cursor.execute(
        """
        INSERT INTO users(
            username,
            password,
            role
        )
        VALUES (?, ?, ?)
        """,
        (
            "admin",
            generate_password_hash("admin123"),
            "admin"
        )
    )

    conn.commit()

print("DONE")
print(cursor.execute("SELECT * FROM users").fetchall())

conn.close()