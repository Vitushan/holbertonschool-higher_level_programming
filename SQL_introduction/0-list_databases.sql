#!/usr/bin/python3


import mysql.connector as MC

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
}

try:
    conn = MC.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SHOW DATABASES;')

    print("All lists of Databases")
    for (db,) in cursor:
    print(db)
    cursor.close()
    conn.close()
except MC.Error as err:
    print(f"Error: {err}")