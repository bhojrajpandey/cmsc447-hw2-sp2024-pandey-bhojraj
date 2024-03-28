import sqlite3
connection = sqlite3.connect("users.db")
cursor = connection.cursor()
command = "CREATE TABLE IF NOT EXISTS users(name TEXT, Id TEXT, points INTEGER)"
cursor.execute(command)
cursor.execute("INSERT INTO users VALUES ('Steve Smith','211', 80)")
cursor.execute("INSERT INTO users VALUES ('Jian Wong','122', 92)")
cursor.execute("INSERT INTO users VALUES ('Chris Peterson','213', 91)")
cursor.execute("INSERT INTO users VALUES ('Sai Patel','524', 94)")
cursor.execute("INSERT INTO users VALUES ('Andrew Whitehead','425', 99)")
cursor.execute("INSERT INTO users VALUES ('Lynn Roberts','626', 90)")
cursor.execute("INSERT INTO users VALUES ('Robert Sanders','287', 75)")
connection.commit()
connection.close()