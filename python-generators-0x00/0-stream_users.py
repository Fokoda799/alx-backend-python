#!/usr/bin/python3
"""
📦 Stream users generator
This module connects to the ALX_prodev MySQL database
and yields user rows one by one as dictionaries.
"""

import seed

def stream_users():
    """
    🔄 Generator function that streams rows from the user_data table.
    
    Yields:
        dict: Each row from the user_data table with 'age' as int
    """
    # 🔗 Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # 📝 Fetch rows as dictionaries

    # 📊 Execute the query to fetch all users
    cursor.execute("SELECT * FROM user_data;")

    # 🚶 Iterate over each row one by one
    while True:
        row = cursor.fetchone()
        if row is None:  # 🛑 Stop iteration when no more rows
            break

        # 🔢 Convert 'age' from Decimal to int for clean output
        row['age'] = int(row['age'])

        # 🎯 Yield the processed row
        yield row

    # 🔒 Close cursor and connection to free resources
    cursor.close()
    connection.close()
