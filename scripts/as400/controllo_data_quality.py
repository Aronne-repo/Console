from utils.utils import ask_input, enter_as400, focus_window, press_as400, write_as400, save_text_in_clipboard, paste_as400, alert_window
from utils.global_variables import (AS400_B, AS400_TITLE, AS400_IMPOSTA_I_CC, AS400_Z, AS400_WRKQRY, AS400_1, AS400_LBCCIUDT)

def controllo_data_quality():
    archivio = ask_input("Quale archivio vuoi consultare?", "Scelta archivio")
    if archivio is None:
        return
    archivio = str(archivio).upper().strip()

    if enter_as400(AS400_B) == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_IMPOSTA_I_CC)
        press_as400("enter")

        write_as400(AS400_Z)
        press_as400("enter")

        press_as400("+f9")
        write_as400(AS400_WRKQRY)
        press_as400("enter")

        write_as400(AS400_1)
        press_as400("enter", 2)

        write_as400(archivio)
        press_as400("tab")
        save_text_in_clipboard(AS400_LBCCIUDT)
        paste_as400()
        press_as400("enter", 2)

        press_as400("down", 3)
        write_as400(AS400_1)
        press_as400("enter")
        press_as400("f11")

        print("Ora puoi costruire la query.")
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)

if __name__ == "__main__":
    controllo_data_quality()