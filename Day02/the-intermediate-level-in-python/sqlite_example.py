"""Creates an in-memory SQLite database and runs queries."""
import sqlite3

if __name__ == "__main__":
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.executemany("INSERT INTO users(name) VALUES (?)", [("Ada",), ("Lin",), ("Max",)])
    cursor.execute("SELECT id, name FROM users WHERE name LIKE ?", ("%a%",))
    for row in cursor.fetchall():
        print(row)
    connection.close()
