import sqlite3

def login(user):
    # Connect to database
    conn = sqlite3.connect("users.db")

    # ❌ Vulnerable SQL Injection (OWASP A03: Injection)
    query = "SELECT * FROM users WHERE name = '" + user + "'"

    # Execute unsafe query
    conn.execute(query)

    print("Login query executed!")
