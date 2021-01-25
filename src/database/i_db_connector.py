import database.db_manager as db_m

users_db = db_m.Database("src/database/bases/users.db")

#users_db.register_user("admin", "0000 0000 0000", "caixa", "1234", "01-01-2000", 0)


def login_user(username, pin):

    real_pass = None

    try:
        real_pass = users_db.get_pin_from_user(username).fetchall()[0][0]
    except IndexError:
        print("user doesn't exist")

    if real_pass == pin:
        return True


def register_user(username, pin, bank, birthday):

    # birthday from <class 'datetime.date'> to <class 'str'>
    birthday = birthday.strftime("%d-%m-%Y")

    # check for numbers in username and username < 4
    only_letters = True
    for l in username:
        try:
            int(l)
            only_letters = False
        except:
            continue

    if not only_letters:
        return False

    if len(username) < 4:
        return False

    # check for letters in pin and leght != 4
    if len(str(pin)) != 4:
        return False

    only_nms = True
    for n in pin:
        try:
            int(n)
        except:
            only_nms = False

    if not only_nms:
        return False

    return True
