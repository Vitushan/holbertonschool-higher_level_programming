#!/usr/bin/python3
"""
lists all cities from the database
"""


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cur = db.cursor()

query = cur.execute(query)
for row in cur.fetchall():
    print(row)

cur.close()
db.close()
