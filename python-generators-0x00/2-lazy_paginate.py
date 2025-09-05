#!/usr/bin/python3
"""
🌀 Lazy pagination generator
Fetches paginated data from the user_data table lazily using a generator
"""

import seed

def paginate_users(page_size, offset):
    """
    📄 Fetch a page of users from the database
    Args:
        page_size (int): Number of rows per page
        offset (int): Offset to start fetching from

    Returns:
        list[dict]: List of user rows
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    # convert age from Decimal to int
    for row in rows:
        row['age'] = int(row['age'])
    cursor.close()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    🔄 Generator that lazily fetches pages of users
    Args:
        page_size (int): Number of rows per page
    Yields:
        list[dict]: Next page of user rows
    """
    offset = 0  # start at the beginning
    while True:  # ✅ only one loop
        page = paginate_users(page_size, offset)
        if not page:  # no more rows
            break
        yield page
        offset += page_size  # move to next page
