#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all databases.
"""

import mysql.connector as MC


config = {
    'host': 'localhost',
    'user':'root',
    'password': 'Database'
}

try:
    conn = MC.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SHOW DATABASES;')

    print("All lists of databases")
    for (db,) in cursor:
        print(db)

    cursor.close()
    conn.close()
except MC.Error as err:
    print(f"Error: {err}")
