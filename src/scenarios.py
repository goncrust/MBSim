import json

# read languages.json content
languages = None
with open('assets/language.json', encoding='utf-8') as languages_file:
    languages = json.load(languages_file)


class Scenario:

    # scenarios enumeration
    LOGIN = 0
    MAIN = 1
    REGISTER = 2
    WHITHDRAW = 3
    BALANCE = 4
    TRANSFERS = 5
    PAYMENTS = 6
    MBWAY = 7
    VOUCHERS = 8
    VOUCHERS1 = 9
    VOUCHERS2 = 10
    WHITHDRAWOTHERAMOUNT = 11
    BALANCE1 = 12
    BALANCE2 = 13
    MBWAY1 = 14

    # languages.json
    LANGUAGES = languages

    # return active buttons in the scene
    @staticmethod
    def get_scenario_active(scenario):

        if scenario == Scenario.LOGIN:
            return [False, False, False, True, True, False, False, True]
        elif scenario == Scenario.MAIN:
            return [True, True, True, True, True, False, False, True]
        elif scenario == Scenario.REGISTER:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.WHITHDRAW:
            return [True, True, True, True, True, False, True, True]
        elif scenario == Scenario.BALANCE:
            return [True, True, False, False, False, False, False, True]
        elif scenario == Scenario.TRANSFERS:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.PAYMENTS:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.MBWAY:
            return [True, False, False, True, False, False, False, False]
        elif scenario == Scenario.VOUCHERS:
            return [True, True, False, False, True, False, False, False]
        elif scenario == Scenario.VOUCHERS1:
            return [True, True, True, True, False, False, False, False]
        elif scenario == Scenario.VOUCHERS2:
            return [False, False, False, False, False, False, True, True]
        elif scenario == Scenario.WHITHDRAWOTHERAMOUNT:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.BALANCE1:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.BALANCE2:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.MBWAY1:
            return [False, False, False, False, False, False, False, True]

    # return buttons's text in the scene
    @staticmethod
    def get_scenario_text(scenario):

        result = []

        for i in range(8):
            result.append(languages[str(scenario)][str(i)]["Portuguese"])

        return result
