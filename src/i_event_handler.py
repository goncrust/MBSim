from scenarios import *
import database.i_db_connector as i_db_con


# button events
class IEventHandler:

    def __init__(self, interface):
        self.interface = interface

    def click_0(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.WITHDRAW
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 20
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                20, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.BALANCE1
            # balance
            self.interface.balance(
                i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY:
            self.interface.current_scenario = Scenario.MBWAY1
            # mbway
            self.interface.mbway()
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.voucher = "Games"

            self.interface.current_scenario = Scenario.VOUCHERS1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.vouchers(10, i_db_con.users_db.get_balance(
                self.interface.current_user) - 10)
            self.interface.update_scenario()

    def click_1(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.BALANCE
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 40
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                40, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE:
            current_user_account_number = i_db_con.users_db.get_account_number_from_name(
                self.interface.current_user)
            self.interface.movements_menu(
                i_db_con.movements_db.retrieve_data(current_user_account_number), current_user_account_number)

            self.interface.current_scenario = Scenario.BALANCE2
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.voucher = "Movies"

            self.interface.current_scenario = Scenario.VOUCHERS1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.vouchers(20, i_db_con.users_db.get_balance(
                self.interface.current_user) - 20)
            self.interface.update_scenario()

    def click_2(self, event):

        if self.interface.current_scenario == Scenario.MAIN:

            # transfers
            self.interface.transfers()

            self.interface.current_scenario = Scenario.TRANSFERS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 60
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                60, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.vouchers(30, i_db_con.users_db.get_balance(
                self.interface.current_user) - 30)
            self.interface.update_scenario()

    def click_3(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            self.interface.destroy_login()

            self.interface.current_scenario = Scenario.REGISTER
            self.interface.update_scenario()

            self.interface.change_bank_register("")

        elif self.interface.current_scenario == Scenario.REGISTER:
            self.interface.destroy_register()

            self.interface.current_scenario = Scenario.LOGIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MAIN:

            # payments
            self.interface.payments()

            self.interface.current_scenario = Scenario.PAYMENTS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 100
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                100, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAWOTHERAMOUNT:
            self.interface.withdraw_custom_destroy()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.TRANSFERS:

            # destroy tranfers
            self.interface.transfers_destroy()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.PAYMENTS:

            # destroy payments
            self.interface.payments_destroy()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.vouchers(50, i_db_con.users_db.get_balance(
                self.interface.current_user) - 50)

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS2:
            self.interface.destroy_vouchers()
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.ADMIN:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.ADMIN1:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.CONFIRMWITHDRAW:
            self.interface.destroy_withdraw()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

    def click_4(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            i_db_con.users_db.close_connection()
            i_db_con.movements_db.close_connection()

            self.interface.window.destroy()

        elif self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.MBWAY
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 200
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                200, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.voucher = "Music"

            self.interface.current_scenario = Scenario.VOUCHERS1
            self.interface.update_scenario()

    def click_5(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.ADMIN
            self.interface.update_scenario()

    def click_6(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.VOUCHERS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            self.interface.current_scenario = Scenario.WITHDRAWOTHERAMOUNT

            self.interface.withdraw_custom()

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.ADMIN1:
            # delete user

            pass

    def click_7(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            # account login
            if (i_db_con.login_user(self.interface.login_username_text.get(), self.interface.login_pin_text.get())):
                self.interface.current_user = self.interface.login_username_text.get()
                self.interface.destroy_login()

                self.interface.current_scenario = Scenario.MAIN
                self.interface.update_scenario()
            else:
                self.interface.login_warning()

        elif self.interface.current_scenario == Scenario.REGISTER:
            # account register
            if (self.interface.register_username_field.cget("fg") == "grey" or self.interface.register_pin_field.cget("fg") == "grey"):
                self.interface.blink_info_register()
            elif (self.interface.register_pin_field.get() != self.interface.register_pin_confirm_field.get()):
                self.interface.set_warning_message_register(5)
            else:

                success, message = i_db_con.register_user(self.interface.register_username_text.get(), self.interface.register_pin_text.get(),
                                                          self.interface.register_bank_abb, self.interface.register_account_number,
                                                          self.interface.register_calendar_field.selection_get())

                if success:

                    self.interface.destroy_register()

                    self.interface.current_scenario = Scenario.LOGIN
                    self.interface.update_scenario()

                else:
                    self.interface.set_warning_message_register(message)

        elif self.interface.current_scenario == Scenario.MAIN:
            # logout
            self.interface.current_user = None

            self.interface.current_scenario = Scenario.LOGIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.TRANSFERS:

            # destroy tranfers

            only_numbers = True
            for n in self.interface.amount_text.get():
                if n != "." and n != ",":
                    try:
                        int(n)
                    except:
                        only_numbers = False

            if only_numbers == False:
                self.interface.transfers_warning()
            else:

                if (i_db_con.users_db.get_balance(self.interface.current_user) - float(self.interface.amount_text.get())) >= 0:

                    iban_text = self.interface.iban_text.get()

                    iban_text = iban_text.replace(" ", "")

                    if len(iban_text) == 25:

                        iban_text = iban_text[:4] + " " + iban_text[4:8] + \
                            " " + iban_text[8:12] + " " + \
                            iban_text[12:23] + " " + iban_text[23:25]

                        if i_db_con.users_db.verify_existing_account_number(iban_text):
                            i_db_con.transfer(
                                self.interface.current_user, iban_text, float(self.interface.amount_text.get()))

                            self.interface.transfers_destroy()
                            self.interface.current_scenario = Scenario.MAIN
                            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAWOTHERAMOUNT:
            # WITHDRAW other amount

            only_numbers = True
            for n in self.interface.custom_withdraw_text.get():
                if n != "." and n != ",":
                    try:
                        int(n)
                    except:
                        only_numbers = False

            if only_numbers:
                self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

                self.interface.withdraw(
                    float(self.interface.custom_withdraw_text.get()), i_db_con.users_db.get_balance(self.interface.current_user))

                self.interface.withdraw_custom_destroy()

                self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE1:
            # destroy balance
            self.interface.destroy_balance()
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE2:
            # destroy movements
            self.interface.movements_menu_destroy()
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.PAYMENTS:

            # destroy payments
            only_numbers = True
            for n in self.interface.entity_text.get():
                try:
                    int(n)
                except:
                    only_numbers = False

            for n in self.interface.reference_text.get():
                try:
                    int(n)
                except:
                    only_numbers = False

            for n in self.interface.payments_amount_text.get():
                if n != "." and n != ",":
                    try:
                        int(n)
                    except:
                        only_numbers = False

            if only_numbers == False:
                self.interface.payments_warning()
            else:
                if (i_db_con.users_db.get_balance(self.interface.current_user) - float(self.interface.payments_amount_text.get())) >= 0:
                    i_db_con.payments(self.interface.current_user, self.interface.entity_text.get(
                    ), self.interface.reference_text.get(), float(self.interface.payments_amount_text.get()))

                    self.interface.payments_destroy()
                    self.interface.current_scenario = Scenario.MAIN
                    self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY1:
            # destroy mbway
            self.interface.destroy_mbway()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS2:
            # voucher
            self.interface.destroy_vouchers()

            if self.interface.voucher_code != None:
                i_db_con.register_movement(i_db_con.VOUCHER, i_db_con.users_db.get_account_number_from_name(
                    self.interface.current_user), self.interface.voucher_amount, None, None, None, self.interface.voucher_type_text, self.interface.voucher_code)

                i_db_con.users_db.set_balance(self.interface.current_user, i_db_con.users_db.get_balance(
                    self.interface.current_user) - float(self.interface.voucher_amount))

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.ADMIN:
            self.interface.current_scenario = Scenario.ADMIN1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.ADMIN1:
            # confirm user modification

            pass

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.CONFIRMWITHDRAW:
            # confirm withdraw
            if self.interface.final_balance >= 0:
                i_db_con.users_db.set_balance(
                    self.interface.current_user, self.interface.final_balance)

                i_db_con.register_movement(i_db_con.WITHDRAW, i_db_con.users_db.get_account_number_from_name(
                    self.interface.current_user), self.interface.amount_withdraw, None, None, None, None, None)

            self.interface.destroy_withdraw()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

    def update_interface_bank_numbers_abb(self):
        self.interface.register_bank_abb, self.interface.register_account_number = i_db_con.create_account_number(
            self.interface.register_bank_text.get())
