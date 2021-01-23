from scenarios import *


# button events
class IEventHandler:

    def __init__(self, interface):
        self.interface = interface

    def click_0(self, event):
        pass

    def click_1(self, event):
        pass

    def click_2(self, event):
        pass

    def click_3(self, event):
        pass

    def click_4(self, event):
        pass

    def click_5(self, event):
        pass

    def click_6(self, event):
        pass

    def click_7(self, event):
        if self.interface.current_scenario == Scenario.LOGIN:
            self.interface.current_scenario = Scenario.MAIN
            self.interface.update_scenario()
