#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments du terminal
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Requête : noms commençant par 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Affiche les résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture
    cursor.close()
    db.close()
