'''
MBSim (https://github.com/goncrust/MBSim)

Scenarios scheme and language/labels handler.

Copyright (c) 2021 by goncrust and contributors
Released under the GPL v3.0
https://github.com/goncrust/MBSim/blob/main/LICENSE.md
'''

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
    WITHDRAW = 3
    BALANCE = 4
    TRANSFERS = 5
    PAYMENTS = 6
    MBWAY = 7
    VOUCHERS = 8
    VOUCHERS1 = 9
    VOUCHERS2 = 10
    WITHDRAWOTHERAMOUNT = 11
    BALANCE1 = 12
    BALANCE2 = 13
    MBWAY1 = 14
    CONFIRMWITHDRAW = 15
    ADMIN = 16
    ADMIN1 = 17
    IBAN = 18

    # languages.json
    LANGUAGES = languages

    # languages
    PORTUGUESE = "pt"
    ENGLISH = "en"

    # specific language cases
    login_username_pt = languages[str(LOGIN)]["Username"]["Portuguese"]
    login_username_en = languages[str(LOGIN)]["Username"]["English"]

    login_pin_pt = languages[str(LOGIN)]["PIN"]["Portuguese"]
    login_pin_en = languages[str(LOGIN)]["PIN"]["English"]

    login_warning_pt = languages[str(LOGIN)]["Warning"]["Portuguese"]
    login_warning_en = languages[str(LOGIN)]["Warning"]["English"]

    register_username_pt = languages[str(REGISTER)]["Username"]["Portuguese"]
    register_username_en = languages[str(REGISTER)]["Username"]["English"]

    register_pin_pt = languages[str(REGISTER)]["PIN"]["Portuguese"]
    register_pin_en = languages[str(REGISTER)]["PIN"]["English"]

    register_pin_confirm_pt = languages[str(
        REGISTER)]["PIN Confirm"]["Portuguese"]
    register_pin_confirm_en = languages[str(
        REGISTER)]["PIN Confirm"]["English"]

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

    register_pin_match_pt = languages[str(
        REGISTER)]["PIN Match"]["Portuguese"]
    register_pin_match_en = languages[str(
        REGISTER)]["PIN Match"]["English"]

    register_age_pt = languages[str(REGISTER)]["Age"]["Portuguese"]
    register_age_en = languages[str(REGISTER)]["Age"]["English"]

    withdraw_current_balance_pt = languages[str(
        CONFIRMWITHDRAW)]["CBalance"]["Portuguese"]
    withdraw_current_balance_en = languages[str(
        CONFIRMWITHDRAW)]["CBalance"]["English"]

    withdraw_amount_pt = languages[str(
        CONFIRMWITHDRAW)]["WAmount"]["Portuguese"]
    withdraw_amount_en = languages[str(CONFIRMWITHDRAW)]["WAmount"]["English"]

    withdraw_final_balance_pt = languages[str(
        CONFIRMWITHDRAW)]["FBalance"]["Portuguese"]
    withdraw_final_balance_en = languages[str(
        CONFIRMWITHDRAW)]["FBalance"]["English"]

    withdraw_insufficient_balance_pt = languages[str(
        CONFIRMWITHDRAW)]["IBalance"]["Portuguese"]
    withdraw_insufficient_balance_en = languages[str(
        CONFIRMWITHDRAW)]["IBalance"]["English"]

    withdraw_other_default_text_pt = languages[str(
        WITHDRAWOTHERAMOUNT)]["Amount"]["Portuguese"]
    withdraw_other_default_text_en = languages[str(
        WITHDRAWOTHERAMOUNT)]["Amount"]["English"]

    withdraw_error_pt = languages[str(
        WITHDRAWOTHERAMOUNT)]["0 Error"]["Portuguese"]
    withdraw_error_en = languages[str(
        WITHDRAWOTHERAMOUNT)]["0 Error"]["English"]

    mbway_error_pt = languages[str(MBWAY1)]["Error Message"]["Portuguese"]
    mbway_error_en = languages[str(MBWAY1)]["Error Message"]["English"]

    voucher_checkout_pt = languages[str(VOUCHERS2)]["Amount"]["Portuguese"]
    voucher_checkout_en = languages[str(VOUCHERS2)]["Amount"]["English"]

    voucher_code_pt = languages[str(VOUCHERS2)]["Code"]["Portuguese"]
    voucher_code_en = languages[str(VOUCHERS2)]["Code"]["English"]

    voucher_warning_pt = languages[str(VOUCHERS2)]["Warning"]["Portuguese"]
    voucher_warning_en = languages[str(VOUCHERS2)]["Warning"]["English"]

    voucher_games_pt = languages[str(VOUCHERS2)]["Games"]["Portuguese"]
    voucher_games_en = languages[str(VOUCHERS2)]["Games"]["English"]

    voucher_movies_pt = languages[str(VOUCHERS2)]["Movies"]["Portuguese"]
    voucher_movies_en = languages[str(VOUCHERS2)]["Movies"]["English"]

    voucher_music_pt = languages[str(VOUCHERS2)]["Music"]["Portuguese"]
    voucher_music_en = languages[str(VOUCHERS2)]["Music"]["English"]

    transfers_iban_pt = languages[str(TRANSFERS)]["IBAN"]["Portuguese"]
    transfers_iban_en = languages[str(TRANSFERS)]["IBAN"]["English"]

    transfers_amount_pt = languages[str(TRANSFERS)]["Amount"]["Portuguese"]
    transfers_amount_en = languages[str(TRANSFERS)]["Amount"]["English"]

    transfers_zero_warning_pt = languages[str(
        TRANSFERS)]["0 Error"]["Portuguese"]
    transfers_zero_warning_en = languages[str(TRANSFERS)]["0 Error"]["English"]

    iban_default_text_pt = languages[str(
        TRANSFERS)]["Default NIB"]["Portuguese"]
    iban_default_text_en = languages[str(
        TRANSFERS)]["Default NIB"]["English"]

    amount_default_text_pt = languages[str(
        TRANSFERS)]["Default Amount"]["Portuguese"]
    amount_default_text_en = languages[str(
        TRANSFERS)]["Default Amount"]["English"]

    tranfers_warning_message_pt = languages[str(
        TRANSFERS)]["Warning Message"]["Portuguese"]
    tranfers_warning_message_en = languages[str(
        TRANSFERS)]["Warning Message"]["English"]

    payments_entity_pt = languages[str(PAYMENTS)]["Entity"]["Portuguese"]
    payments_entity_en = languages[str(PAYMENTS)]["Entity"]["English"]

    payments_reference_pt = languages[str(PAYMENTS)]["Reference"]["Portuguese"]
    payments_reference_en = languages[str(PAYMENTS)]["Reference"]["English"]

    payments_amount_pt = languages[str(PAYMENTS)]["Amount"]["Portuguese"]
    payments_amount_en = languages[str(PAYMENTS)]["Amount"]["English"]

    payments_warning_message_pt = languages[str(
        PAYMENTS)]["Warning Message"]["Portuguese"]
    payments_warning_message_en = languages[str(
        PAYMENTS)]["Warning Message"]["English"]

    payments_zero_warning_pt = languages[str(
        PAYMENTS)]["0 Error"]["Portuguese"]
    payments_zero_warning_en = languages[str(PAYMENTS)]["0 Error"]["English"]

    payments_entity_size_pt = languages[str(
        PAYMENTS)]["Entity size"]["Portuguese"]
    payments_entity_size_en = languages[str(
        PAYMENTS)]["Entity size"]["English"]

    payments_reference_size_pt = languages[str(
        PAYMENTS)]["Reference size"]["Portuguese"]
    payments_reference_size_en = languages[str(
        PAYMENTS)]["Reference size"]["English"]

    movements_withdraws_pt = languages[str(
        BALANCE2)]["Withdraws"]["Portuguese"]
    movements_withdraws_en = languages[str(BALANCE2)]["Withdraws"]["English"]

    movements_transfers_pt = languages[str(
        BALANCE2)]["Transfers"]["Portuguese"]
    movements_transfers_en = languages[str(BALANCE2)]["Transfers"]["English"]

    movements_payments_pt = languages[str(BALANCE2)]["Payments"]["Portuguese"]
    movements_payments_en = languages[str(BALANCE2)]["Payments"]["English"]

    movements_vouchers_pt = languages[str(BALANCE2)]["Vouchers"]["Portuguese"]
    movements_vouchers_en = languages[str(BALANCE2)]["Vouchers"]["English"]

    iban_pt = languages[str(IBAN)]["IBAN"]["Portuguese"]
    iban_en = languages[str(IBAN)]["IBAN"]["English"]

    admin_new_pin_pt = languages[str(ADMIN1)]["New PIN"]["Portuguese"]
    admin_new_pin_en = languages[str(ADMIN1)]["New PIN"]["English"]

    @staticmethod
    def get_label(label):
        if Scenario.get_current_language() == Scenario.PORTUGUESE:
            return eval("Scenario." + label + "_pt")
        elif Scenario.get_current_language() == Scenario.ENGLISH:
            return eval("Scenario." + label + "_en")

    @staticmethod
    def get_current_language():
        return languages["Current Language"]

    @staticmethod
    def set_current_language(language):
        languages["Current Language"] = language

        with open('assets/language.json', 'w', encoding='utf-8') as languages_file:
            json.dump(languages, languages_file, ensure_ascii=False, indent=4)

    # return active buttons in the scene
    @staticmethod
    def get_scenario_active(scenario, admin):

        if scenario == Scenario.LOGIN:
            return [False, False, False, True, True, False, False, True]
        elif scenario == Scenario.MAIN:
            if admin:
                return [True, True, True, True, True, True, True, True]
            else:
                return [True, True, True, True, True, False, True, True]
        elif scenario == Scenario.REGISTER:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.WITHDRAW:
            return [True, True, True, True, True, False, True, True]
        elif scenario == Scenario.BALANCE:
            return [True, True, True, False, False, False, False, True]
        elif scenario == Scenario.TRANSFERS:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.PAYMENTS:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.MBWAY:
            return [True, False, False, True, False, False, False, False]
        elif scenario == Scenario.VOUCHERS:
            return [True, True, False, False, True, False, False, True]
        elif scenario == Scenario.VOUCHERS1:
            return [True, True, True, True, False, False, False, True]
        elif scenario == Scenario.VOUCHERS2:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.WITHDRAWOTHERAMOUNT:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.BALANCE1:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.BALANCE2:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.MBWAY1:
            return [False, False, False, False, False, False, False, True]
        elif scenario == Scenario.CONFIRMWITHDRAW:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.ADMIN:
            return [False, False, False, True, False, False, False, True]
        elif scenario == Scenario.ADMIN1:
            return [False, False, False, True, False, False, True, True]
        elif scenario == Scenario.IBAN:
            return [False, False, False, False, False, False, False, True]

    # return buttons's text in the scene
    @staticmethod
    def get_scenario_text(scenario):

        result = []

        for i in range(8):
            if Scenario.get_current_language() == Scenario.PORTUGUESE:
                result.append(languages[str(scenario)][str(i)]["Portuguese"])
            elif Scenario.get_current_language() == Scenario.ENGLISH:
                result.append(languages[str(scenario)][str(i)]["English"])

        return result
