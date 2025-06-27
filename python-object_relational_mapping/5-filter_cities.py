"""
script that takes in the name of a state as an argument and lists all cities of that state
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=db_name,
        state_name=state_name
    )
    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.name, states.name
        ORDER BY cities.id ASC
"""
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
