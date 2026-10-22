from utils.utils import focus_window, alert_window, press_as400, write_as400, enter_as400, enter_as400_environment_and_libraries
from utils.global_variables import (AS400_TITLE, AS400_IMPOSTAZIONI, AS400_I, AS400_CC, AS400_ZINAVSTR, AS400_TM81)

def esegui_batch():
    if enter_as400() == "Sì":
        focus_window(AS400_TITLE)
        press_as400("enter")
        write_as400(AS400_IMPOSTAZIONI)
        press_as400("f4")
        
        enter_as400_environment_and_libraries(scelta="2")

        write_as400(AS400_ZINAVSTR)
        press_as400("enter")
        write_as400(AS400_TM81)
        
        print("Sono arrivato alla conferma del processo.")
    else:
        alert_window("Interrompo l'autenticazione su AS/400", AS400_TITLE)

if __name__ == "__main__":
    esegui_batch()