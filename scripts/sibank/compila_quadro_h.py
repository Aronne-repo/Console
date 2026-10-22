from utils.utils import (exists_window, focus_window, close_window_by_name, ask_yes_no, alert_window, open_edge, enter_sibank, enter_gestione_questionari_banca, start_verifica_questionario, enter_questionario_information)
from utils.global_variables import DESKTOP_TITLE, RETROSPORTELLO_TITLE

def compila_quadro_h():
    first_run = not exists_window(RETROSPORTELLO_TITLE)

    if first_run:
        open_edge()
        enter_sibank(False)
        close_window_by_name(DESKTOP_TITLE)
        focus_window(RETROSPORTELLO_TITLE)
        enter_gestione_questionari_banca()
    else:
        focus_window(RETROSPORTELLO_TITLE)

    continua = ask_yes_no("Hai selezionato il questionario da compilare?", "Seleziona")
    if continua == "Sì":
        start_verifica_questionario()
        enter_questionario_information()
        print("Ho compilato il Quadro H per il CAG selezionato.")
    else:
        alert_window("Interrompo la compilazione del Quadro H")
        return

if __name__ == "__main__":
    compila_quadro_h()