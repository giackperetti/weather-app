import sqlite3

connection: sqlite3.Connection = sqlite3.connect('users.db')

with open('users.sql') as f:
    connection.executescript(f.read())

db_cursor: sqlite3.Cursor = connection.cursor()

db_cursor.execute("INSERT INTO users (name) VALUES (?)", ('admin',))

connection.commit()
connection.close()
