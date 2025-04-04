#!/usr/bin/python3
"""
lists all sql
"""


import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE `name` = %s ORDER BY id"

    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
