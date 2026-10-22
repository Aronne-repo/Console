from utils.utils import save_text_in_clipboard, focus_window, ask_date, alert_window, press_as400, write_as400, paste_as400, enter_as400, enter_as400_environment_and_libraries
from utils.global_variables import (AS400_TITLE, AS400_IMPOSTAZIONI, AS400_M, AS400_T0, AS400_Z, AS400_STRSQL)

def estrai_codici_da2():
    data = ask_date("Quale giorno ti interessa estrarre?", False)
    if data is None:
        return
    QUERY_DA2_CODES = f"Select SUBSTR(D11CER, 5, 8) CODICE_MANDATO, D11RAP CODICE_DA2, D11JAC from D11 where D11SER = 'DA2' and D11JAC = '{data}' and D11SRC = ' '"

    if enter_as400() == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_IMPOSTAZIONI)
        press_as400("f4")

        enter_as400_environment_and_libraries(scelta="1")

        write_as400(AS400_Z)
        press_as400("enter")

        press_as400("+f9")
        write_as400(AS400_STRSQL)
        press_as400("enter")

        save_text_in_clipboard(QUERY_DA2_CODES)
        paste_as400()
        press_as400("enter")
        print("Ho eseguito la query per estrarre i codici DA2.")
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)

if __name__ == "__main__":
    estrai_codici_da2()