#!/usr/bin/env python3
import time
import sqlite3
import functools


with_db_connection = __import__("1-with_db_connection").with_db_connection

query_cache = {}

def cache_query(func):
    """
    Decorator to cache query results based on the SQL query string.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if query in query_cache:
            print(f"Fetching result from cache for query: {query}")
            return query_cache[query]
        result = func(*args, **kwargs)
        query_cache[query] = result
        print(f"Caching result for query: {query}")
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will hit the DB and cache result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")

print(users)
print(users_again)
