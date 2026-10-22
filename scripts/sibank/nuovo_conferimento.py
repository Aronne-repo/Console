from utils.utils import ask_input, exists_window, open_edge, enter_sibank, click, close_window_by_name, wait_image, focus_window, press_button, enter_cag, open_gestione_raccomandazione, open_raccomandazioni_proposte, select_operation, select_the_DA2, wait_seconds, write, generate_recommendation_documents, confirm_new_deposit, alert_window
from utils.global_variables import (SPORTELLO_TITLE, MONITOR_DI_CONTROLLO_LETTORI_TITLE, VERSAMENTO_AGGIUNTIVO)

def nuovo_conferimento():
    cag = ask_input("Su quale CAG vuoi eseguire il versamento?", "Nuovo versamento")
    if cag is None:
        return
    cag = str(cag).strip()
    importo = ask_input("Quanto vuoi versare?", "Nuovo versamento")
    if importo is None:
        return
    importo = str(importo).strip()
    first_run = not exists_window(SPORTELLO_TITLE)

    if first_run:
        open_edge()
        enter_sibank()
        click(970, 20) # Clicca il pulsante "Finanza"
        click(470, 55) # Clicca il pulsante "Cruscotto"
        close_window_by_name(MONITOR_DI_CONTROLLO_LETTORI_TITLE)
        wait_image("cruscotto_finanza")
    else:
        focus_window(SPORTELLO_TITLE)
        click(1555, 175) # Chiude la finestra "Stampe finanza: Riepilogo"
        click(685, 190) # Riattiva la finestra "Cruscotto"
        press_button("del")
    
    enter_cag(cag)
    press_button("enter", 1, 10)
    wait_image("questionario_mifid")

    open_gestione_raccomandazione()
    open_raccomandazioni_proposte()
    select_operation(VERSAMENTO_AGGIUNTIVO)

    if select_the_DA2() == "Sì":
        focus_window(SPORTELLO_TITLE, "y")
        press_button("enter")
        click(760, 680) # Clicca sul campo di testo "Importo"
        wait_seconds(0.5)
        write(importo)
        wait_seconds(0.5)
        press_button("enter", 1, 3)

        generate_recommendation_documents()
        confirm_new_deposit()
        press_button("enter")

        print(f"Ho eseguito un versamento di {importo} € sul CAG {cag}.")
    else:
        alert_window("Interrompo il nuovo conferimento", SPORTELLO_TITLE)

if __name__ == "__main__":
    nuovo_conferimento()