#!/usr/bin/python3
"""
script lists all states with a name
starting with N from rhe database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db=MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cur = db.cursor()
cur.execute("SELECT * FROM STATES ORDER BY 'N'")

for rows in cur.fetchall():
    print(rows)

cur.close()
db.close()
