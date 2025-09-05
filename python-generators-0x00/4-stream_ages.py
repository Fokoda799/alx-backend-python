#!/usr/bin/python3
"""
📏 Stream user ages from the database and
calculate and print the average age of users
"""

import seed



def stream_user_ages():
    """
    🎯 Generator function to lazily stream user ages
    from the database

    Yield: users age one by one
    """

    # 🔌 Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    # ✔ Only select the age column from the user_data table
    cursor.execute("SELECT age FROM user_data")

    # 🏃‍ Keep fetching one row at a time
    while True:
        row = cursor.fetchone()
        if not row:  # 🚪 Stop when there are no more rows
            break

        # 🧹 row is a tuple like (67,), so take row[0] and cast to int
        yield int(row[0])

    # 🔒 Close the cursor/connection
    cursor.close()
    connection.close()



def main():
    """
    🧮 Main function: calculate and print the average age of users
    """
    
    total = 0  # accumulator for ages
    count = 0  # number of users processed

    # Iterate through ages lazily from the generator
    for age in stream_user_ages():
        total += age
        count += 1

    # Print the average (total / count)
    print(f"Average age of users: {total / count}")


# 🚀 Run the main function if the script is executed
main()
