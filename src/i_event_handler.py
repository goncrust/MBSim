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
            pass

    def click_1(self, event):
        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.BALANCE
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            pass

    def click_2(self, event):
        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.TRANSFERS
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            pass

    def click_3(self, event):
        if self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.PAYMENTS
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            pass

    def click_4(self, event):
        if self.interface.current_scenario == Scenario.LOGIN:
            self.interface.current_scenario = Scenario.REGISTER
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.MAIN:
            self.interface.current_scenario = Scenario.MBWAY
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.WHITHDRAW:
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
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()
        elif self.interface.current_scenario == Scenario.WHITHDRAW:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()
