#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

    cursor = db.cursor()

    # SAFE query with parameterization (recommended)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
