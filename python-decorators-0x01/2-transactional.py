#!/usr/bin/python3

import functools
import sqlite3


with_db_connection = __import__("1-with_db_connection").with_db_connection

def transactional(func):
    """
    💾 Decorator to wrap a function inside a database transaction.
    - If the function executes successfully ➡️ commit changes.
    - If an exception occurs ➡️ rollback changes.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()   # ✅ Commit on success
            return result
        except Exception as e:
            conn.rollback()  # ❌ Rollback on error
            print(f"⚠️ Transaction failed: {e}")
            raise
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
    #### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
