import sqlite3


class Database:

    def __init__(self, db_file):
        self.db_file = db_file

        self.connect()
        self.set_cursor()

        self.default_tables()

    def connect(self):
        self.con = sqlite3.connect(self.db_file)

    def set_cursor(self):
        self.c = self.con.cursor()

    def default_tables(self):
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS Users(name TEXT, account INT, bank TEXT, pin INT, birthday TEXT, balance INT)")

    def close_connection(self):
        self.c.close()
        self.con.close()
