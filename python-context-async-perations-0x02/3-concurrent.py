#!/usr/bin/python3
"""
Module: 2-concurrent_async_queries
Description: Demonstrates how to run concurrent asynchronous SQLite queries using asyncio and aiosqlite.
"""

import asyncio
import aiosqlite


async def async_fetch_users(db_path="users.db"):
    """
    Fetch all users from the database asynchronously.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        list: List of tuples representing all users.
    """
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute("SELECT * FROM users;")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows


async def async_fetch_older_users(db_path="users.db"):
    """
    Fetch users older than 40 from the database asynchronously.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        list: List of tuples representing users older than 40.
    """
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40;")
        rows = await cursor.fetchall()
        await cursor.close()
        return rows


async def fetch_concurrently():
    """
    Run multiple asynchronous database queries concurrently
    and return their results.
    
    Returns:
        tuple: Two lists, first all users, second users older than 40.
    """
    # Execute both queries concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return all_users, older_users


if __name__ == "__main__":
    # Run concurrent fetch using asyncio.run
    all_users, older_users = asyncio.run(fetch_concurrently())
    
    print("All Users:")
    print(all_users)
    print("\nUsers Older Than 40:")
    print(older_users)
