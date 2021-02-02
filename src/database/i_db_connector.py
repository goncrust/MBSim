import database.db_manager as db_m
from database.banks import *
from datetime import date, datetime
import hashlib

users_db = db_m.UDatabase("src/database/bases/users.db")
movements_db = db_m.MDatabase("src/database/bases/movements.db")

TRANSFER = 0
WITHDRAW = 1
PAYMENT = 2


def login_user(username, pin):

    pin = hashlib.sha512(pin.encode('utf-8')).hexdigest()

    real_pass = None

    try:
        real_pass = users_db.get_pin_from_user(username).fetchall()[0][0]
    except IndexError:
        return False

    if real_pass == pin:
        return True


def register_user(username, pin, bank_abb, account_number, birthday):

    # birthday from <class 'datetime.date'> to <class 'str'>
    #print(abs(date.today() - birthday).year)

    year_difference = date.today().year - birthday.year
    today = date.today()

    if date(2000, today.month, today.day) < date(2000, birthday.month, birthday.day):
        year_difference = year_difference - 1

    if (year_difference < 16):
        return False, 6

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

    # encryption
    pin = hashlib.sha512(pin.encode('utf-8')).hexdigest()

    # check for already existing username
    if users_db.verify_existing_username(username):
        return False, 4

    # bank abbreviation and account number
    bank, account = bank_abb, account_number

    # commit to db
    users_db.register_user(username, account, bank, pin, birthday, 0)

    return True, 0


def create_account_number(bank_extended):
    finished = False

    bank, account = ["", ""]

    while not finished:
        bank, account = Bank.generate_account_number(bank_extended)
        if not users_db.verify_existing_account_number(account):
            finished = True

    return bank, account


def transfer(user_from, iban_to, amount):
    users_db.set_balance(user_from, users_db.get_balance(user_from) - amount)

    user_to = users_db.get_name_from_account_number(iban_to)

    users_db.set_balance(user_to, users_db.get_balance(user_to) + amount)

    register_movement(TRANSFER, users_db.get_account_number_from_name(
        user_from), amount, iban_to, None, None)


def payments(user_from, entity, reference, amount):
    users_db.set_balance(user_from, users_db.get_balance(user_from) - amount)

    register_movement(PAYMENT, users_db.get_account_number_from_name(
        user_from), amount, None, entity, reference)


def register_movement(movement_type, account, amount, account_to, entity, reference):
    date_now = datetime.now().strftime("%d-%m-%Y %H:%M")

    if movement_type == TRANSFER:
        movements_db.register_transfer(account, account_to, amount, date_now)
    elif movement_type == WITHDRAW:
        movements_db.register_withdraw(account, amount, date_now)
    elif movement_type == PAYMENT:
        movements_db.register_payment(
            account, entity, reference, amount, date_now)
