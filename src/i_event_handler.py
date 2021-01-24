from scenarios import *


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
            self.interface.current_scenario = Scenario.REGISTER
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.REGISTER:
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

            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()

        elif self.interface.current_scenario == Scenario.REGISTER:
            # account register

            pass

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
