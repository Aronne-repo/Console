from utils.utils import wait_seconds, focus_window, alert_window, ask_input, press_as400, write_as400, enter_as400, enter_as400_environment_and_libraries
from utils.global_variables import (AS400_TITLE, AS400_IMPOSTAZIONI, AS400_I, AS400_M, AS400_T0, AS400_CC, AS400_BJ, AS400_KB, AS400_Z, AS400_ZT99, AS400_X, AS400_USERNAME, AS400_2)

def cambia_ambiente_e_classe():
    scelta = ask_input("Quale ambiente vuoi impostare?\n 1. M T0 / 2. I CC / 3. I BJ / 4. I KB", "Ambiente dati")
    if scelta is None:
        return
    scelta = str(scelta).strip()
    classe_abilitazione = ask_input("Quale classe vuoi impostare? GP1-6 / FCO", "Abilitazione")
    if classe_abilitazione is None:
        return
    classe_abilitazione = str(classe_abilitazione).strip()

    if enter_as400() == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_IMPOSTAZIONI)
        press_as400("f4")

        enter_as400_environment_and_libraries(scelta)

        write_as400(AS400_Z)
        press_as400("enter")

        write_as400(AS400_ZT99)
        press_as400("enter")

        write_as400(AS400_X)
        press_as400("enter")

        for _ in range(2):
            press_as400("+tab")

        write_as400(str(AS400_USERNAME).upper().strip())
        press_as400("enter")

        write_as400(AS400_2)
        press_as400("enter")

        press_as400("enter")

        write_as400(classe_abilitazione.strip())
        press_as400("enter")

        press_as400("enter")
        wait_seconds(1)

        ambiente = ""
        if scelta == "1":
            ambiente = "M T0"
        elif scelta == "2":
            ambiente = "I CC"
        elif scelta == "3":
            ambiente = "I BJ"
        else:
            ambiente = "I KB"
        print(f"Ho impostato l'ambiente '{ambiente}' e la classe '{classe_abilitazione.upper()}' sull'utenza {AS400_USERNAME.upper().strip()}.")
        
        alert_window("Ho completato l'istruzione, ora chiudo AS400", AS400_TITLE)
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)
        return

if __name__ == "__main__":
    cambia_ambiente_e_classe()