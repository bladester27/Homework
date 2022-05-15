import sqlite3

conn = sqlite3.connect('db.sqlite3')
conn.execute('CREATE TABLE "finance" (id, appointment, summ, datem)')
