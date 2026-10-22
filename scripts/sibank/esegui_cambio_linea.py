from utils.utils import (alert_window, ask_input, click, close_window_by_name, enter_cag, enter_sibank, exists_window, focus_window, generate_recommendation_documents, open_edge, open_gestione_raccomandazione, open_raccomandazioni_proposte, press_button, select_operation, select_line_to_change, select_the_DA2, confirm_new_recommendation, wait_image, wait_seconds)
from utils.global_variables import (MONITOR_DI_CONTROLLO_LETTORI_TITLE, MONITOR_MANDATI_TITLE, SPORTELLO_TITLE, CAMBIO_LINEA, WIN2PDF_TITLE)

def esegui_cambio_linea():
    cag = ask_input("Su quale CAG vuoi eseguire il cambio linea?", "Cambio linea")
    if cag is None:
        return
    cag = str(cag).strip()
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
    select_operation(CAMBIO_LINEA)

    if select_the_DA2() == "Sì":
        focus_window(SPORTELLO_TITLE, "y")
        press_button("enter")
        click(820, 730) # Clicca sul pulsante "Prodotto"
        select_line_to_change()
        press_button("enter", 1, 3)

        generate_recommendation_documents()
        close_window_by_name(WIN2PDF_TITLE, 90)
        confirm_new_recommendation()

        wait_seconds(15)
        focus_window(MONITOR_MANDATI_TITLE)

        print("Ho concluso il flusso.")

    else:
        alert_window("Interrompo il cambio linea", SPORTELLO_TITLE)
        return

if __name__ == "__main__":
    esegui_cambio_linea()