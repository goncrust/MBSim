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

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.BALANCE1
            # balance
            self.interface.balance(i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY:
            self.interface.current_scenario = Scenario.MBWAY1
            # mbway
            self.interface.mbway()
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.interface.current_scenario = Scenario.VOUCHERS1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
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

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.BALANCE2
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS:
            self.interface.current_scenario = Scenario.VOUCHERS1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.update_scenario()

    def click_2(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.TRANSFERS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 60
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                60, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

            pass

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
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
            self.interface.current_scenario = Scenario.PAYMENTS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WITHDRAW:
            # WITHDRAW 100
            self.interface.current_scenario = Scenario.CONFIRMWITHDRAW

            self.interface.withdraw(
                100, i_db_con.users_db.get_balance(self.interface.current_user))

            self.interface.update_scenario()

            pass

        elif self.interface.current_scenario == Scenario.WITHDRAWOTHERAMOUNT:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.TRANSFERS:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.PAYMENTS:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
            self.interface.current_scenario = Scenario.VOUCHERS2
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS2:
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

            pass

        elif self.interface.current_scenario == Scenario.VOUCHERS:
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

        elif self.interface.current_scenario == Scenario.WITHDRAWOTHERAMOUNT:
            # WITHDRAW other amount

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE1:
            # destroy balance
            self.interface.destroy_balance()
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE2:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.TRANSFERS:
            # transfer

            pass

        elif self.interface.current_scenario == Scenario.PAYMENTS:
            # payment

            pass

        elif self.interface.current_scenario == Scenario.MBWAY1:
            # destroy mbway
            self.interface.destroy_mbway()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.VOUCHERS1:
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

            self.interface.destroy_withdraw()

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

    def update_interface_bank_numbers_abb(self):
        self.interface.register_bank_abb, self.interface.register_account_number = i_db_con.create_account_number(
            self.interface.register_bank_text.get())
