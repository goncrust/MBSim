import json

# read languages.json content
languages = None
with open('assets/language.json') as languages_file:
    languages = json.load(languages_file)


class Scenario:

    # scenarios enumeration
    LOGIN = 0
    MAIN = 1
    MAINS = 2

    # languages.json
    LANGUAGES = languages

    # return active buttons in the scene
    @staticmethod
    def get_scenario_active(scenario):

        if scenario == Scenario.LOGIN:
            return [True, True, True, True, True, False, False, True]

    # return buttons's text in the scene
    @staticmethod
    def get_scenario_text(scenario):

        result = []

        for i in range(8):
            result.append(languages[str(scenario)][str(i)]["Portuguese"])

        return result
