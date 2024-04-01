import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    q = """ CREATE TABLE IF NOT EXISTS request_history(id INTEGER, a REAL, b REAL, c REAL, d REAL, e REAL) """
    cursor.execute(q)

    cursor.execute(""" DELETE FROM request_history""")
