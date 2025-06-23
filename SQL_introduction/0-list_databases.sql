#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all databases.
"""

import mysql.connector


config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Database'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES;")

    print("All lists of databases:")
    for (db,) in cursor:
    print(db)

    cursor.close()
    conn.close()
