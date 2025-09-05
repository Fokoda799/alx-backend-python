#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

# Connect to MySQL server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alxuser",
            password="wac2003A$"  # replace with your MySQL root password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create the ALX_prodev database if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully or already exists")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

# Connect to ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alxuser",
            password="wac2003A$",  # replace with your MySQL root password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age Integer NOT NULL,
        UNIQUE(email)
    )
    """
    try:
        cursor.execute(create_table_query)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Insert data from CSV into the table
def insert_data(connection, data):
    cursor = connection.cursor()
    with open(data, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            try:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) "
                    "VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE name=name",
                    (user_id, name, email, age)
                )
            except mysql.connector.Error as err:
                print(f"Error inserting {email}: {err}")
    connection.commit()
    cursor.close()
