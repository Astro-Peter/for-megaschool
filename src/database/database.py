import sqlite3
from contextlib import closing

def get_db_connection():
    connection = sqlite3.connect('db.sqlite')
    connection.row_factory = sqlite3.Row
    return connection