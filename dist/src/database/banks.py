import random


class Bank:

    PORTUGAL_IDENTIFIER = "PT50"
    PORTUGAL_VERIFICATION = "54"

    CAIXA_IDENTIFIER = "0035"
    SANTANDER_IDENTIFIER = "0018"
    MILLENNIUM_IDENTIFIER = "0033"
    BPI_IDENTIFIER = "0010"
    NOVO_IDENTIFIER = "0007"
    BANKINTER_IDENTIFIER = "0269"
    EUROBIC_IDENTIFIER = "0079"
    POPULAR_IDENTIFIER = "0046"
    MONTEPIO_IDENTIFIER = "0036"
    BANCOCTT_IDENTIFIER = "0193"
    BBVA_IDENTIFIER = "0019"

    CAIXA_ABBREVIATION = "caixa"
    SANTANDER_ABBREVIATION = "santander"
    MILLENNIUM_ABBREVIATION = "millennium"
    BPI_ABBREVIATION = "bpi"
    NOVO_ABBREVIATION = "novo"
    BANKINTER_ABBREVIATION = "bankinter"
    EUROBIC_ABBREVIATION = "eurobic"
    POPULAR_ABBREVIATION = "popular"
    MONTEPIO_ABBREVIATION = "montepio"
    BANCOCTT_ABBREVIATION = "ctt"
    BBVA_ABBREVIATION = "bbva"

    @staticmethod
    def generate_account_number(bank):

        final_code = ""

        agency_code = str(random.randint(0, 9999))

        if len(agency_code) < 4:
            agency_code = "0"*(4-len(agency_code)) + agency_code

        account_code = str(random.randint(0, 99999999999))

        if len(account_code) < 11:
            account_code = "0"*(11-len(account_code)) + account_code

        if bank == "Caixa Geral de Depóstios":
            bank = Bank.CAIXA_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.CAIXA_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Santander Totta":
            bank = Bank.SANTANDER_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.SANTANDER_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Millennium BCP":
            bank = Bank.MILLENNIUM_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.MILLENNIUM_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "BPI":
            bank = Bank.BPI_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.BPI_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Novo Banco":
            bank = Bank.NOVO_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.NOVO_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Bankinter":
            bank = Bank.BANKINTER_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.BANKINTER_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "EuroBIC":
            bank = Bank.EUROBIC_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.EUROBIC_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Popular":
            bank = Bank.POPULAR_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.POPULAR_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Montepio":
            bank = Bank.MONTEPIO_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.MONTEPIO_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "Banco CTT":
            bank = Bank.BANCOCTT_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.BANCOCTT_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION
        elif bank == "BBVA":
            bank = Bank.BBVA_ABBREVIATION
            final_code = Bank.PORTUGAL_IDENTIFIER + " " + Bank.BBVA_IDENTIFIER + " " + \
                agency_code + " " + account_code + " " + Bank.PORTUGAL_VERIFICATION

        return bank, final_code
