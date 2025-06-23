#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


import mysql.connector as MC


conn = Mc.connect(
    host='localhost',
    user='root',
    password='',
)
cursor = conn.cursor()
