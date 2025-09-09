#!/usr/bin/python3

import sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, parm):
        self.db_name = db_name
        self.query = query
        self.parm = parm

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(self.query, self.parm)
        return cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()


with ExecuteQuery("user.db", "SELECT * FROM users WHERE age > ?", 25) as result:
    print(result)

