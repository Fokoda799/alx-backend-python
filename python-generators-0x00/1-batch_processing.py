#!/usr/bin/python3
"""
📦 Stream users generator
This module connects to the ALX_prodev MySQL database
and yields user rows in batches """

import seed

def stream_users_in_batches(batch_size):
    """
    🔄 Generator function that streams rows in batches from the user_data table.
    
    Yields:
        batche: Each batche of users from the user_data table.
    """
    # 🔗 Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)  # 📝 Fetch rows as dictionaries

    # 📊 Execute the query to fetch all users
    cursor.execute("SELECT * FROM user_data;")

    # 🚶 Iterate over each batch one by one
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:  # 🛑 Stop iteration when no more rows
            break

        # 🎯 Yield the processed row
        yield batch

    # 🔒 Close cursor and connection to free resources
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    🗃 Processes each batch to filter users over age 25
    """
    for batch in stream_users_in_batches(batch_size):  # loop 1: over batches
        for user in batch:  # loop 2: over users in batch
            if user['age'] > 25:  # filter condition
                print(user)  # loop 3 (optional, printing counts as a loop)
