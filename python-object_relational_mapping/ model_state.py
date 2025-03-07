#!/usr/bin/python3
"""
lists cities of the states
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.conne t(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    results = cur.fetchall()
    print(", ".join([city[0] for city in results]))

    cur.close()
    db.close()
