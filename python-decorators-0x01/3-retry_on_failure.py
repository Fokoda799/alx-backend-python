#!/usr/bin/python3

import time
import sqlite3
import functools


with_db_connection = __import__("1-with_db_connection").with_db_connection

def retry_on_failure(retries=3, delay=2):
    """
    Decorator to retry a function if it raises an Exception.
    Args:
        retries (int): number of retry attempts
        delay (int): delay in seconds between retries
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt >= retries:
                        raise
                    print(f"Attempt {attempt} failed with {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
