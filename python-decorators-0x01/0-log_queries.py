#!/usr/bin/python3
"""
 📌 This module provides a simple decorator for logging function queries.

Functions:
    log_queries(func): A decorator that logs the first argument passed to the function.
"""

import functools


def log_queries(func):
    """
    📝 Decorator that prints the first positional argument passed 
    to the decorated function before calling it.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that logs the first argument.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #  🖨️ Log the first argument passed to the function
        print(args[0])

        # 📞 Call the original function with all arguments
        func(*args, **kwargs)

    return wrapper



@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
