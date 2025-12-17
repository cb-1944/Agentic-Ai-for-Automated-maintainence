import sqlite3


DB_PATH = "app/db/appointment.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)

def get_connection():
    return conn
