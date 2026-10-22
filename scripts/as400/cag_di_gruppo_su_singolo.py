from utils.utils import wait_seconds, focus_window, alert_window, ask_input, ask_yes_no, press_as400, write_as400, enter_as400, enter_as400_environment_and_libraries
from utils.global_variables import (AS400_TITLE, AS400_IMPOSTAZIONI, AS400_M, AS400_T0, AS400_CC, AS400_Z, AS400_UPDDTA, AS400_A01A, AS400_Y)

def cag_di_gruppo_su_singolo():
    ambiente_dati = ask_input("Quale ambiente vuoi impostare? M / I", "Ambiente dati")
    if ambiente_dati is None:
        return
    ambiente_dati = str(ambiente_dati).upper().strip()
    cag_1 = ask_input("Su quale CAG vuoi impostare il gruppo?", "Imposta CAG di gruppo")
    if cag_1 is None:
        return
    cag_1 = str(cag_1).strip()
    cag_2 = ask_yes_no("Il CAG del campo 'CAG Ind. Spedizione' è lo stesso di prima?", "Imposta CAG Ind. Spedizione 1")
    if cag_2 == "Sì":
        cag_2 = cag_1
    else:
        cag_2 = ask_input("Qual è il CAG da scrivere nel campo 'CAG Ind. Spedizione'?", "Imposta CAG Ind. Spedizione 2")
        if cag_2 is None:
            return
        cag_2 = str(cag_2).strip()

    if enter_as400() == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_IMPOSTAZIONI)
        press_as400("f4")
        write_as400(ambiente_dati)

        if ambiente_dati == AS400_M:
            enter_as400_environment_and_libraries(scelta="1")
        else:
            enter_as400_environment_and_libraries(scelta="2")

        write_as400(AS400_Z)
        press_as400("enter")

        press_as400("+f9")

        write_as400(f"{AS400_UPDDTA} {AS400_A01A}")
        press_as400("enter")

        write_as400(cag_1)
        press_as400("enter")

        press_as400("enter")

        for _ in range(9):
            press_as400("down")

        write_as400(cag_2)
        press_as400("enter")

        press_as400("f3")
        write_as400(AS400_Y)
        press_as400("enter")

        press_as400("f12")

        for _ in range(2):
            press_as400("f3")
        wait_seconds(3)

        if cag_1 == cag_2:
            print(f"Ho impostato il CAG di gruppo su '{cag_1}'.")
        else:
            print(f"Ho impostato il CAG di gruppo su '{cag_1}' e su '{cag_2}'.")
        
        alert_window("Ho completato l'istruzione, ora chiudo AS400", AS400_TITLE)
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)
        return

if __name__ == "__main__":
    cag_di_gruppo_su_singolo()