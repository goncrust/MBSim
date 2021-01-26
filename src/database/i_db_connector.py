import database.db_manager as db_m
from database.banks import *

users_db = db_m.Database("src/database/bases/users.db")

#users_db.register_user("admin", "0000 0000 0000", "caixa", "1234", "01-01-2000", 0)


def login_user(username, pin):

    real_pass = None

    try:
        real_pass = users_db.get_pin_from_user(username).fetchall()[0][0]
    except IndexError:
        return False

    if real_pass == pin:
        return True


def register_user(username, pin, bank_abb, account_number, birthday):

    # birthday from <class 'datetime.date'> to <class 'str'>
    birthday = birthday.strftime("%d-%m-%Y")

    # check for numbers in username and username < 4
    # only_letters = True
    # for l in username:
    # try:
    #    int(l)
    #    only_letters = False
    # except:
    #    continue

    # if not only_letters:
    #    return False, 0

    username_only_letters = username

    for l in range(len(username_only_letters)):
        if username_only_letters[l] == " ":
            username_only_letters = username_only_letters[:l] + \
                "a" + username_only_letters[l+1:]

    if not username_only_letters.isalpha():
        return False, 0

    if len(username) < 4:
        return False, 1

    # check for letters in pin and leght != 4
    only_nms = True
    for n in pin:
        try:
            int(n)
        except:
            only_nms = False

    if not only_nms:
        return False, 2

    if len(str(pin)) != 4:
        return False, 3

    # check for already existing username
    if users_db.verify_existing_username(username):
        return False, 4

    # bank abbreviation and account number
    bank, account = bank_abb, account_number

    return True, 0


def create_account_number(bank_extended):
    finished = False

    bank, account = ["", ""]

    while not finished:
        bank, account = Bank.generate_account_number(bank_extended)
        if not users_db.verify_existing_account_number(account):
            finished = True

    return bank, account
