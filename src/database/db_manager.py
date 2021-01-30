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

        if not self.verify_existing_username("admin"):
            self.register_user(
                "admin", "PT50 0035 0000 00000000000 54", "caixa",
                "f02595051ebd518fd644330d62943e604048a66ec62d4eee6b5f974cd2f9d636e4ea9da3ac9c2705477ccab0315b3f56047286d728a63070c2963f1a9fed4544",
                "01-01-2000", 0)

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
        try:
            self.c.execute("SELECT name FROM Users WHERE name=?",
                           (user,)).fetchall()[0]
            return True
        except IndexError:
            return False

    def verify_existing_account_number(self, account):
        try:
            self.c.execute(
                "SELECT account FROM Users WHERE account=?", (account,)).fetchall()[0]
            return True
        except IndexError:
            return False

    def get_balance(self, user):
        return self.c.execute("SELECT balance FROM Users WHERE name=?", (user,)).fetchall()[0][0]

    def set_balance(self, user, balance):
        self.c.execute(
            "UPDATE Users SET balance=? WHERE name=?", (balance, user))

        self.con.commit()
