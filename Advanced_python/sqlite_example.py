import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
connection.commit()

for row in cursor.execute("SELECT * FROM users"):
    print(row)

connection.close()