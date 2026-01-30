import sqlite3

def login(user):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + user + "'"
    conn.execute(query)
