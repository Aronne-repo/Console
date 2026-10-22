from utils.utils import ask_input, focus_window, alert_window, enter_as400, press_as400, set_day_as400, today, write_as400, yesterday
from utils.global_variables import (AS400_A, AS400_B, AS400_CM08, AS400_D, AS400_DEPOSITO, AS400_PRELIEVO, AS400_TITLE, AS400_TK45, AS400_Z)

def esegui_nuovo_conferimento():
    scelta = ask_input("Vuoi eseguire un deposito o un prelievo?\n 1. Deposito / 2. Prelievo", "Nuovo conferimento")
    if scelta is None:
        return
    scelta = str(scelta).strip()
    amount = ask_input("Di quanto deve essere il conferimento?", "Nuovo conferimento")
    if amount is None:
        return
    amount = str(amount).strip()
    mandato = ask_input("Su quale mandato vuoi fare il nuovo conferimento?", "Nuovo conferimento")
    if mandato is None:
        return
    mandato = str(mandato).strip()
    
    ieri = yesterday().replace(".", "")
    oggi = today().replace(".", "")
    
    if enter_as400(AS400_B) == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_Z)
        press_as400("enter")

        set_day_as400(ieri)

        write_as400(AS400_CM08)
        press_as400("enter")

        press_as400("tab")
        write_as400("0" + mandato)
        press_as400("enter")

        if scelta == "1":
            write_as400(AS400_DEPOSITO)
        else:
            write_as400(AS400_PRELIEVO)
        press_as400("tab")

        write_as400(amount)
        press_as400("tab")

        if scelta == "1":
            write_as400(AS400_A)
        else:
            write_as400(AS400_D)
        
        write_as400(ieri)
        press_as400("enter")

        press_as400("f3")

        write_as400(AS400_TK45)
        press_as400("enter")

        write_as400(mandato)
        press_as400("enter", 2)

        set_day_as400(oggi)

        tipo_conferimento = "deposito" if scelta == "1" else "prelievo"
        print(f"Ho eseguito un {tipo_conferimento} di {amount} € sul mandato {mandato}.")
        alert_window("Ho completato l'istruzione, ora chiudo AS400", AS400_TITLE)
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)

if __name__ == "__main__":
    esegui_nuovo_conferimento()