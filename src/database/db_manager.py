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
            "CREATE TABLE IF NOT EXISTS Users(name TEXT, account TEXT, bank TEXT, pin TEXT, birthday TEXT, balance REAL)")

        self.con.commit()

    def close_connection(self):
        self.c.close()
        self.con.close()

    def register_user(self, name, account, bank, pin, birthday, balance):
        self.c.execute(
            "INSERT INTO Users(name, account, bank, pin, birthday, balance) VALUES(?, ?, ?, ?, ?, ?)", (name, account, bank, pin, birthday, balance))

        self.con.commit()

    def get_pin_from_user(self, user):
        return self.c.execute("SELECT pin FROM Users WHERE name=?", (user,))

    def verify_existing_username(self, user):
        if self.c.execute("SELECT name FROM Users WHERE name=?", (user,)) != None:
            return True
