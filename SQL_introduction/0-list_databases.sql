#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


import mysql.connector as MC


    conn = MC.connect(host = 'localhost', database = 'data', user = 'root', password= '')
    cursor = conn.cursor()
 