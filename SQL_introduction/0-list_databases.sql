#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all databases.
"""

import mysql.connector


conn = mysql.connector.connect(
    host:"localhost",
    user:"root",
    password:""
)

cursor = conn.cursor()


cursor.execute("SHOW DATABASES;")


print("Databases on this MySQL server:")
for db in cursor:
    print(f"- {db[0]}")


cursor.close()
conn.close()
