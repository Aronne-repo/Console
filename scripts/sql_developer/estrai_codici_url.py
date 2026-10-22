from utils.utils import wait_seconds, wait_image, click, ask_input, ask_date, run_query, enter_sql_dev

def estrai_codici_url():
    utenza = ask_input("Quale utenza FK hai usato per creare i mandati?", "Estrai dati URL")
    if utenza is None:
        return
    utenza = str(utenza).strip().lower()
    if not utenza.startswith("fk"):
        utenza = "fk" + utenza
    data = ask_date("Quale giorno ti interessa estrarre?")
    if data is None:
        return
    GET_URL_CODES = f"select creation_date as data_creazione, id_number, user_code as utenza_creatrice, cag_id as cag, dossier as mandato, 'https://example.it/list/detail/' || to_char(cag_id) as url_mandato from prw_plan.agreement where user_code in ('{utenza}') and trunc(create_tms) = date '{data}' order by dossier asc;"

    enter_sql_dev()

    click(16, 274) # Apre la connessione al database
    wait_image("sql_clear", 0.7, 20)
    wait_seconds(3)
    click(1200, 600) # Clicca nel campo di testo

    run_query(GET_URL_CODES)
    print("Ho lanciato la query per vedere i codici per completare gli URL dei mandati.")
    
if __name__ == "__main__":
    estrai_codici_url()