#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


from mysql.connector as MC

try:
    conn = MC.connect(host = 'localhost', database = 'data', user = 'root', password= '')
    cursor = conn.cursor()
 
except MC.Error as err:
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close
