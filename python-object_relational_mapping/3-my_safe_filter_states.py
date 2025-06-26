"""
script should connect to a MySQL
server running on localhost at port 3306
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
