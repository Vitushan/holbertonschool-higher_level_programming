#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all databases.
"""

import mysql.connector

# Connexion au serveur MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Envoi de la commande SQL SHOW DATABASES
cursor.execute("SHOW DATABASES;")

# Affichage des résultats
print("Databases on this MySQL server:")
for db in cursor:
    print(f"- {db[0]}")

# Fermeture
cursor.close()
conn.close()
