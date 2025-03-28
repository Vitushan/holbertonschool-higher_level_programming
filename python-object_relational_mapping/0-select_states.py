#!/usr/bin/python3
"""
Script that listd all states on the database hbtn_0e_0_usa.
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

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
