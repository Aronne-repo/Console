from utils.utils import wait_seconds, wait_image, click, press_button, ask_input, run_query, commit_query, alert_window, enter_sql_dev, confirm_exit_sql_dev
from utils.global_variables import SQL_DEVELOPER_WINDOW_TITLE

def cambia_abi_utenza():
    utenza = ask_input("Quale utenza FK vuoi modificare?", "Cambio ABI")
    if utenza is None:
        return
    utenza = str(utenza).strip().lower()
    if not utenza.startswith("fk"):
        utenza = "fk" + utenza
    scelta = ask_input("Quale ABI vuoi impostare?\n 1. 8883 / 2. 3599 / 3. 8587 / 4. 8852", "Cambio ABI")
    if scelta is None:
        return
    scelta = str(scelta).strip()
    
    abi = ""
    if scelta == "1":
        abi = "8528"
    elif scelta == "2":
        abi = "2002"
    elif scelta == "3":
        abi = "1111"
    elif scelta == "4":
        abi = "0709"
    else:
        alert_window("Scelta non valida", "Errore")
        return

    CHANGE_ABI = f"update users set abi = '{abi}' where user_code = '{utenza}';"

    enter_sql_dev()

    click(16, 247) # Apre la connessione al database
    wait_image("sql_clear", 0.7, 20)
    wait_seconds(3)
    click(1200, 600) # Clicca nel campo di testo

    run_query(CHANGE_ABI)
    wait_seconds(3)
    commit_query()
    alert_window(f"Ho impostato l'ABI '{abi}' sull'utenza '{utenza}', sto per chiudere SQL Developer", SQL_DEVELOPER_WINDOW_TITLE)
    
    wait_seconds(1.5)
    confirm_exit_sql_dev()
    print("Ho chiuso SQL Developer.")

if __name__ == "__main__":
    cambia_abi_utenza()