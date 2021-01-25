import database.db_manager as db_m

users_db = db_m.Database("src/database/bases/users.db")

#users_db.register_user("admin", "0000 0000 0000", "caixa", "1234", "01-01-2000", 0)


def login_user(username, password):
    real_pass = users_db.get_pin_from_user(username).fetchall()[0][0]

    if real_pass == password:
        return True
