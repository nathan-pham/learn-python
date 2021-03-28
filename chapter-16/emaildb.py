import sqlite3 as sql

connection = sql.connect("emaildb.sqlite")
ref = connection.cursor()
