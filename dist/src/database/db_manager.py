import sqlite3


class UDatabase:

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
                "01-01-2000", 10000)

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

    def delete_user(self, name):
        self.c.execute("DELETE FROM Users WHERE name=?", (name,))

        self.con.commit()

    def get_name_from_account_number(self, account):
        return self.c.execute("SELECT name FROM Users WHERE account=?", (account,)).fetchall()[0][0]

    def get_account_number_from_name(self, name):
        return self.c.execute("SELECT account FROM Users WHERE name=?", (name,)).fetchall()[0][0]

    def get_bank_from_name(self, name):
        return self.c.execute("SELECT bank FROM Users WHERE name=?", (name,)).fetchall()[0][0]

    def get_birthday_from_name(self, name):
        return self.c.execute("SELECT birthday FROM Users WHERE name=?", (name,)).fetchall()[0][0]


class MDatabase:

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
            "CREATE TABLE IF NOT EXISTS Withdraw(account TEXT, amount REAL, date)")

        self.c.execute(
            "CREATE TABLE IF NOT EXISTS Transfers(account TEXT, account_to TEXT, amount REAL, date TEXT)")

        self.c.execute(
            "CREATE TABLE IF NOT EXISTS Payments(account TEXT, entity TEXT, reference TEXT, amount REAL, date TEXT)")

        self.c.execute(
            "CREATE TABLE IF NOT EXISTS Vouchers(account TEXT, type TEXT, code TEXT, amount REAL, date TEXT)")

        self.con.commit()

    def close_connection(self):
        self.c.close()
        self.con.close()

    def register_transfer(self, account, account_to, amount, date):
        self.c.execute(
            "INSERT INTO Transfers(account, account_to, amount, date) VALUES(?, ?, ?, ?)", (account, account_to, amount, date))

        self.con.commit()

    def register_withdraw(self, account, amount, date):
        self.c.execute("INSERT INTO Withdraw(account, amount, date) Values(?, ?, ?)",
                       (account, amount, date))

        self.con.commit()

    def register_payment(self, account, entity, reference, amount, date):
        self.c.execute("INSERT INTO Payments(account, entity, reference, amount, date) Values(?, ?, ?, ?, ?)",
                       (account, entity, reference, amount, date))

        self.con.commit()

    def register_voucher(self, account, voucher_type, voucher_code, amount, date):
        self.c.execute("INSERT INTO Vouchers(account, type, code, amount, date) Values(?, ?, ?, ?, ?)",
                       (account, voucher_type, voucher_code, amount, date))

        self.con.commit()

    def retrieve_data(self, account):
        withdraw_data = self.c.execute(
            "SELECT * FROM Withdraw WHERE account=?", (account,)).fetchall()
        transfers_data = self.c.execute(
            "SELECT * FROM Transfers WHERE account=? OR account_to=?", (account, account)).fetchall()
        payments_data = self.c.execute(
            "SELECT * FROM Payments WHERE account=?", (account,)).fetchall()
        vouchers_data = self.c.execute(
            "SELECT * FROM Vouchers WHERE account=?", (account,)).fetchall()

        return withdraw_data, transfers_data, payments_data, vouchers_data
