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

    # specific language cases
    login_username_pt = languages[str(LOGIN)]["Username"]["Portuguese"]
    login_username_en = languages[str(LOGIN)]["Username"]["English"]

    login_pin_pt = languages[str(LOGIN)]["PIN"]["Portuguese"]
    login_pin_en = languages[str(LOGIN)]["PIN"]["English"]

    warning_pin_pt = languages[str(LOGIN)]["Warning"]["Portuguese"]
    warning_pin_en = languages[str(LOGIN)]["Warning"]["English"]

    register_username_pt = languages[str(REGISTER)]["Username"]["Portuguese"]
    register_username_en = languages[str(REGISTER)]["Username"]["English"]

    register_pin_pt = languages[str(REGISTER)]["PIN"]["Portuguese"]
    register_pin_en = languages[str(REGISTER)]["PIN"]["English"]

    register_info_pt = languages[str(REGISTER)]["Info"]["Portuguese"]
    register_info_en = languages[str(REGISTER)]["Info"]["English"]

    register_only_letters_pt = languages[str(
        REGISTER)]["Only Letters"]["Portuguese"]
    register_only_letters_en = languages[str(
        REGISTER)]["Only Letters"]["English"]

    register_short_username_pt = languages[str(
        REGISTER)]["Short Username"]["Portuguese"]
    register_short_username_en = languages[str(
        REGISTER)]["Short Username"]["English"]

    register_only_numbers_pt = languages[str(
        REGISTER)]["Only numbers"]["Portuguese"]
    register_only_numbers_en = languages[str(
        REGISTER)]["Only numbers"]["English"]

    register_pin_size_pt = languages[str(REGISTER)]["PIN Size"]["Portuguese"]
    register_pin_size_en = languages[str(REGISTER)]["PIN Size"]["English"]

    register_username_exists_pt = languages[str(
        REGISTER)]["Username exists"]["Portuguese"]
    register_username_exists_en = languages[str(
        REGISTER)]["Username exists"]["English"]

    register_calendar_field_pt = languages[str(
        REGISTER)]["Birthday"]["Portuguese"]
    register_calendar_field_en = languages[str(
        REGISTER)]["Birthday"]["English"]

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
