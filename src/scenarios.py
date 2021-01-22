

class Scenario:

    LOGIN = 0
    MAIN = 1
    MAINS = 2

    @staticmethod
    def get_scenario_active(scenario):

        if scenario == Scenario.LOGIN:
            return [True, True, True, True, True, False, False, True]

    @staticmethod
    def get_scenario_text(scenario):

        if scenario == Scenario.LOGIN:
            return ["", "", "", "", "", "", "", ""]
