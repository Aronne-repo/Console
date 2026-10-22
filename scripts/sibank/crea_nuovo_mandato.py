from utils.global_variables import (SPORTELLO_TITLE, MONITOR_DI_CONTROLLO_LETTORI_TITLE, WIN2PDF_TITLE)
from utils.utils import (exists_window, focus_window, alert_window, close_window_by_name, wait_seconds, wait_image, click, press_button, ask_yes_no, open_edge,
enter_sibank, enter_customer_8883, enter_cointestation, open_gestione_raccomandazione, open_raccomandazioni_proposte, add_new_recommendation, generate_recommendation_documents,
confirm_new_recommendation, accept_anagrafica, uncheck_myGp, enter_questionario_antiriciclaggio, confirm_quadri_A_D_F, download_documents, sign_documents)

def crea_nuovo_mandato():
    coi = ask_yes_no("Vuoi che il nuovo mandato sia cointestato?")
    is_coi = (coi == "Sì")
    private = ask_yes_no("Vuoi che il nuovo mandato abbia una linea private?")
    is_private = (private == "Sì")
    if not is_private:
        pir = ask_yes_no("Vuoi che il nuovo mandato abbia un prodotto PIR?")
    else:
        pir = "No"
    is_pir = (pir == "Sì")
    myGp = ask_yes_no("Vuoi che il nuovo mandato abbia MyGP?")
    has_myGp = (myGp == "Sì")
    first_run = not exists_window(SPORTELLO_TITLE)

    if first_run:
        open_edge()
        enter_sibank()
        wait_seconds(1)
        click(970, 20) # Clicca il pulsante "Finanza"
        click(470, 55) # Clicca il pulsante "Cruscotto"
        close_window_by_name(MONITOR_DI_CONTROLLO_LETTORI_TITLE)
        wait_image("cruscotto_finanza")
    else:
        focus_window(SPORTELLO_TITLE)
        click(1555, 175) # Chiude la finestra "Stampe finanza: Riepilogo"
        click(685, 190) # Riattiva la finestra "Cruscotto"
        press_button("del")
    
    if is_coi:
        enter_cointestation()
    else:
        enter_customer_8883()
    wait_image("questionario_mifid")

    open_gestione_raccomandazione()
    open_raccomandazioni_proposte()
    add_new_recommendation(is_private, is_pir)
    generate_recommendation_documents()
    close_window_by_name(WIN2PDF_TITLE, 90)
    confirm_new_recommendation()

    wait_seconds(15)
    accept_anagrafica()
    wait_image("toggle_my_gp", 0.7, 20)

    if not has_myGp:
        uncheck_myGp()
    
    continua = ask_yes_no("Posso continuare?", "Seleziona")
    if continua == "No":
        alert_window("Mi sto fermando")
        return
    click(1755, 280) # Clicca su "Continua"
    enter_questionario_antiriciclaggio()
    confirm_quadri_A_D_F()
    if is_coi:
        enter_questionario_antiriciclaggio(False)
        confirm_quadri_A_D_F()
    download_documents()
    sign_documents()

    log_product = "Private" if is_private else "PIR" if is_pir else "standard"
    log_myGp = "con" if has_myGp else "senza"
    log_coi = "cointestato " if is_coi else ""
    print(f"Ho creato un nuovo mandato {log_coi}con un prodotto {log_product} e {log_myGp} MyGP.")
    
if __name__ == "__main__":
    crea_nuovo_mandato()