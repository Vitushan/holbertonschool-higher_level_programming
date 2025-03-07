#!/usr/bin/python3
"""
That script  takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
