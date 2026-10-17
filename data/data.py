import sqlite3 as sq

DB_PATH = 'data/Users.db'

def connect_DB():
    return sq.connect(DB_PATH)
def cursor_connect(con) :
    return con.cursor()