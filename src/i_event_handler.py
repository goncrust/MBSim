

class IEventHandler:

    def __init__(self, interface):
        self.interface = interface

    def click(self, event):
        self.interface.cenario(
            [True, False, True, False, True, True, False, False], "")
