from scenarios import *
import database.i_db_connector as i_db_con


# button events
class IEventHandler:

    def __init__(self, interface):
        self.interface = interface

    def click_0(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.WHITHDRAW
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            # whithdraw 20

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.BALANCE1
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MBWAY:
            self.interface.current_scenario = Scenario.MBWAY1
            self.interface.update_scenario()

    def click_1(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.BALANCE
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            # whithdraw 40

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.BALANCE2
            self.interface.update_scenario()

    def click_2(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.TRANSFERS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            # whithdraw 60

            pass

    def click_3(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            self.interface.destroy_login()

            self.interface.current_scenario = Scenario.REGISTER
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.REGISTER:
            self.interface.destroy_register()

            self.interface.current_scenario = Scenario.LOGIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.PAYMENTS
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            # whithdraw 100

            pass

        elif self.interface.current_scenario == Scenario.WHITHDRAWOTHERAMOUNT:
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

    def click_4(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            i_db_con.users_db.close_connection()

            self.interface.window.destroy()

        elif self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.MBWAY
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            # whithdraw 200

            pass

    def click_5(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

    def click_6(self, event):

        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            self.interface.current_scenario = Scenario.WHITHDRAWOTHERAMOUNT
            self.interface.update_scenario()

    def click_7(self, event):

        if self.interface.current_scenario == Scenario.LOGIN:
            # account login
            if (i_db_con.login_user(self.interface.login_username_text.get(), self.interface.login_pin_text.get())):
                self.interface.destroy_login()

                self.interface.current_scenario = Scenario.MAIN
                self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.REGISTER:
            # account register
            if (self.interface.register_username_field.cget("fg") == "grey" or self.interface.register_pin_field.cget("fg") == "grey"):
                self.interface.blink_info_register()
            else:

                success, message = i_db_con.register_user(self.interface.register_username_text.get(), self.interface.register_pin_text.get(),
                                                          self.interface.register_bank_text.get(), self.interface.register_calendar_field.selection_get())

                if success:

                    self.interface.destroy_register()

                    self.interface.current_scenario = Scenario.LOGIN
                    self.interface.update_scenario()

                else:
                    self.interface.set_warning_message_register(message)

        elif self.interface.current_scenario == Scenario.MAIN:
            # logout

            self.interface.current_scenario = Scenario.LOGIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.WHITHDRAWOTHERAMOUNT:
            # whithdraw other amount

            pass

        elif self.interface.current_scenario == Scenario.BALANCE:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.BALANCE1:
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
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()
