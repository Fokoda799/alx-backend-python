#!/usr/bin/python3

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()


with DatabaseConnection("user.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    print(cursor.fetchall())
