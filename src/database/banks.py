

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
        if bank == "Caixa Geral de Depóstios":
            pass
        elif bank == "Santander Totta":
            pass
        elif bank == "Millennium BCP":
            pass
        elif bank == "BPI":
            pass
        elif bank == "Novo Banco":
            pass
        elif bank == "Bankinter":
            pass
        elif bank == "EuroBIC":
            pass
        elif bank == "Popular":
            pass
        elif bank == "Montepio":
            pass
        elif bank == "Banco CTT":
            pass
        elif bank == "BBVA":
            pass
