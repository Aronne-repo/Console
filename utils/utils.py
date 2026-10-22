import time, subprocess, random
from datetime import datetime, timedelta
import pyautogui, pyperclip, pygetwindow as gw
import tkinter as tk
from tkcalendar import Calendar
from utils.global_variables import (AS400_A, AS400_M, AS400_I, AS400_T0, AS400_CC, AS400_BJ, AS400_KB, AS400_LBL, AS400_LIB1, AS400_LIB2, AS400_LIB3, AS400_TITLE, AS400_ZG07, CAMBIO_LINEA, CITRIX_URL, CMD_EXE, DESKTOP_TITLE, BROWSER, MONITOR_MANDATI_TITLE, NUOVA_SOTTOSCRIZIONE, PNG_DIR, RETROSPORTELLO_TITLE, SCELTA_NO, SESSIONI_TITLE, SPORTELLO_TITLE, THIS_PC_TITLE, UTENZA)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# Logica
def today():
    return datetime.today().strftime("%d.%m.%Y")

def yesterday():
    return (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")

def wait_seconds(seconds):
    time.sleep(seconds)

def click(x, y, rep=1, right=False, wait=0.4):
    button = "right" if right else "left"
    tasto = " con il tasto destro" if right else ""

    for _ in range(rep):
        pyautogui.click(x, y, button=button)
        wait_seconds(0.1)

    volte = "volta" if rep == 1 else "volte"

    print(f"Ho cliccato{tasto} {rep} {volte} nel punto ({x}, {y}).")
    wait_seconds(wait)

def save_text_in_clipboard(text):
    pyperclip.copy(str(text))
    print(f"Ho copiato il testo '{text}'.")

def ask_yes_no(message, title="Conferma"):
    popup = tk.Toplevel()
    popup.title(title)
    result = {"value": "No"}
    tk.Label(popup, text=message).pack(padx=20, pady=(20, 10))

    def yes():
        result["value"] = "Sì"
        print(f"Ho confermato il pop-up '{message}'.")
        popup.destroy()
    def no():
        result["value"] = "No"
        print(f"Ho annullato il pop-up '{message}'.")
        popup.destroy()

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=(0, 20))
    tk.Button(button_frame, text="Sì", command=yes).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="No", command=no).pack(side=tk.LEFT, padx=5)

    popup.bind("<Return>", lambda event: yes())
    popup.bind("<Escape>", lambda event: no())

    popup.transient(popup.master)
    popup.grab_set()
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")
    popup.wait_window()

    return result["value"]

def ask_input(message, title="Input"):
    popup = tk.Toplevel()
    popup.title(title)
    result = {"value": None}
    tk.Label(popup,text=message).pack(padx=20, pady=(20, 5))
    entry = tk.Entry(popup, width=30)
    entry.pack(padx=20, pady=(0, 20))

    def confirm():
        result["value"] = entry.get()
        print(f"Ho confermato il valore '{entry.get()}' nel pop-up '{message}'.")
        popup.destroy()
    def cancel():
        print(f"Ho annullato il pop-up '{message}'.")
        popup.destroy()

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=(0, 20))

    tk.Button(button_frame, text="Conferma", command=confirm).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Annulla", command=cancel).pack(side=tk.LEFT, padx=5)

    popup.bind("<Return>", lambda event: confirm())
    popup.bind("<Escape>", lambda event: cancel())
    popup.transient(popup.master)
    popup.grab_set()
    entry.focus_force()

    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")

    popup.wait_window()
    return result["value"]

def ask_date(title="Seleziona una data", sql_format=True):
    popup = tk.Toplevel()
    popup.title(title)
    result = {"value": None}
    date_pattern = "yyyy-mm-dd" if sql_format else "dd.mm.yyyy"
    cal = Calendar(popup, selectmode="day", date_pattern=date_pattern)
    cal.pack(padx=10, pady=10)

    def confirm():
        result["value"] = cal.get_date()
        popup.destroy()

    tk.Button(popup, text="Conferma", command=confirm).pack(pady=10)
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")
    popup.grab_set()
    popup.wait_window()

    return result["value"]

def alert_window(message, window_name=None):
    popup = tk.Toplevel()
    popup.title("Interruzione processo")
    tk.Label(popup, text=message).pack(padx=20, pady=20)
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")
    popup.after(1000, popup.destroy)
    popup.wait_window()
    if window_name:
        print(f"{message}.")
        close_window_by_name(window_name)

# Metodi per le finestre
def wait_window(window_name, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        for window in gw.getAllWindows():
            if window_name.lower().strip() in window.title.lower():
                print(f"Ho trovato la finestra '{window_name}'.")
                return window
        wait_seconds(0.3)

    print(f"Non ho trovato la finestra '{window_name}'.")
    return None

def exists_window(window_name, timeout=3):
    return wait_window(window_name, timeout) is not None

def focus_window(window_name, maximize="n"):
    window = wait_window(window_name)
    if not window:
        print(f"Non ho trovato la finestra '{window_name}'.")
        return False

    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        wait_seconds(0.2)
        if maximize.lower().strip() == "y":
            window.maximize()

        print(f"Ho portato in primo piano la finestra '{window_name}'.")
        return True
    except Exception as e:
        print(f"Ho un problema nel gestire la finestra '{window_name}': {e}")
        return False

def close_window_by_name(window_name, timeout=5):
    window = wait_window(window_name, timeout)
    if window:
        window.close()
        print(f"Ho chiuso la finestra '{window_name}'.")
        return True

    print(f"La finestra '{window_name}' non era aperta.")
    return False

# Metodi per gli elementi dello schermo
def click_image(image_name, confidence=0.7, timeout=10):
    start_time = time.time()
    image_path = PNG_DIR / f"{image_name}.png"
    
    while time.time() - start_time < timeout:
        try:
            position = pyautogui.locateCenterOnScreen(str(image_path), confidence=confidence)
            if position:
                pyautogui.click(position.x, position.y)
                print(f"Ho cliccato sull'elemento '{image_name}'.")
                return True
        except Exception:
            print(f"Non ho trovato l'elemento '{image_name}'.")

        wait_seconds(0.5)
    return False

def wait_image(image_name, confidence=0.9, timeout=10):
    start_time = time.time()
    image_path = PNG_DIR / f"{image_name}.png"

    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(str(image_path), confidence=confidence)
            if location:
                print(f"Ho trovato l'immagine '{image_name}'.")
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.2)

    print(f"Non ho trovato l'immagine '{image_name}' entro {timeout} secondi.")
    return False

# Azioni
def go_to_url(url):
    save_text_in_clipboard(url)
    press_button("^l")
    press_button("del")
    press_button("^v")
    press_button("enter")

def open_edge():
    if not exists_window(BROWSER):
        subprocess.Popen(["msedge.exe", CITRIX_URL], shell=False)
        print("Ho aperto una nuova finestra di Edge.")
    return focus_window(BROWSER)

def choose_as400_session(sessione):
    if sessione == "A":
        click(790, 362, 2)
    elif sessione == "B":
        click(790, 392, 2)
    else:
        click(790, 419, 2)

def enter_as400(sessione=AS400_A):
    open_edge()
    click_image("as400")
    focus_window(SESSIONI_TITLE)
    wait_seconds(0.5)
    choose_as400_session(sessione)
    focus_window(AS400_TITLE)
    close_window_by_name(SESSIONI_TITLE)
    wait_seconds(0.5)

    write_as400(UTENZA)
    press_as400("tab")

    continua = ask_yes_no("Hai inserito la password corretta?", "Autenticazione")
    return continua

def enter_as400_environment_and_libraries(scelta):
    if scelta == "1":
        save_text_in_clipboard(f"{AS400_M}{AS400_T0}{AS400_LIB2}{AS400_LIB1}{AS400_LBL}")
    elif scelta == "2":
        save_text_in_clipboard(f"{AS400_I}{AS400_CC}{AS400_LIB2}{AS400_LIB1}{AS400_LBL}")
    elif scelta == "3":
        save_text_in_clipboard(f"{AS400_I}{AS400_BJ}{AS400_LIB2}{AS400_LIB1}{AS400_LBL}")
    else:
        save_text_in_clipboard(f"{AS400_I}{AS400_KB}{AS400_LIB2}{AS400_LIB1}{AS400_LBL}")
    paste_as400()
    press_as400("enter")

def set_day_as400(day):
    write_as400(AS400_ZG07)
    press_as400("enter")
    write_as400(day)
    press_as400("enter", 2)

def write_as400(text):
    write(text, 0.8)

def press_as400(button, rep=1, wait=0.8):
    press_button(button, rep, wait)

def paste_as400():
    click(270, 100, 1, False, 0.8)

def enter_sql_dev():
    open_edge()
    click_image("sql_developer")
    if exists_window(CMD_EXE):
        focus_window(CMD_EXE)
        write("y")
        press_button("enter")
    wait_image("sql_new_connection", 0.7, 50)
    wait_seconds(5)

def enter_sibank(legacy=True):
    # Apre l'explorer
    click_image("explorer")
    wait_window(THIS_PC_TITLE)
    focus_window(THIS_PC_TITLE)

    # Entra nella cartella "Desktop"
    press_button("down")
    press_button("up")
    press_button("enter")

    # Avvia Sibank.exe
    press_button("down")
    press_button("enter")
    wait_window(RETROSPORTELLO_TITLE, 90)
    focus_window(RETROSPORTELLO_TITLE)
    wait_seconds(0.5)
    # Chiude i pop up di errore se l'utenza è 3359
    press_button("enter", 2)

    if legacy:
        click(45, 1075) # Clicca il pulsante bianco un basso a sinistra
        press_button("up", 2)
        press_button("enter")
        wait_window(SPORTELLO_TITLE)
        close_window_by_name(DESKTOP_TITLE)
        close_window_by_name(RETROSPORTELLO_TITLE)
        focus_window(SPORTELLO_TITLE)
        click(1500, 100)  # Chiude la finestra "Giornale di sportello"
        press_button("enter", 1, 1)

def enter_customer_8883():
    choices = ["00010729", "00165550", "00146922", "00227376", "00001700", "00299173"]
    write(random.choice(choices))
    press_button("enter", 1, 10)

def enter_cag(cag):
    write(cag)
    press_button("enter", 1, 10)

def enter_customer_3359():
    choices = ["00960493"]
    write(random.choice(choices))
    press_button("enter", 1, 10)

def enter_cointestation():
    choices = ["00366266"]
    write(random.choice(choices))
    click(750, 190) # Clicca sulla checkbox "Anche cointestazioni"
    wait_seconds(9)
    press_button("enter", 1, 10)

def enter_amount(pir):
    if pir:
        write(str(40000))
    else:
        values = [250000, 300000, 350000, 400000, 450000, 500000, 550000]
        write(str(random.choice(values)))
    wait_seconds(1)

def select_subscription(private, pir):
    if private:
        press_button("enter", 1, 3)  # Seleziona "PRIVATE"
        for _ in range(random.randint(0, 4)):
            press_button("tab")

        percentuale_1 = random.choice(range(0, 101, 5))
        write(str(percentuale_1).strip())

        for _ in range(random.randint(1, 3)):
            press_button("tab")

        percentuale_2 = 100 - percentuale_1
        write(str(percentuale_2).strip())

        print(f"Ho impostato le percentuali {percentuale_1}% e {percentuale_2}%.")
        press_button("enter", 2) # Conferma le percentuali dell'investimento
    elif pir:
        click(580, 325)  # Clicca il radio button "Prodotti: PIR"
        for _ in range(random.randint(0, 3)):
            press_button("down")
        press_button("enter")
    else:
        for _ in range(random.randint(1, 15)):
            press_button("down")
    press_button("enter")

def select_line_to_change():
    for _ in range(random.randint(4, 8)):
        press_button("down")
    press_button("enter")

def run_query(query):
    save_text_in_clipboard(query)
    press_button("^v")
    press_button("^enter")

def commit_query():
    press_button("f11")

def confirm_exit_sql_dev():
    press_button("right")
    press_button("enter")

# Keyboard helpers
def write(text, wait=0.5):
    pyautogui.write(str(text))
    wait_seconds(wait)
    print(f"Ho scritto '{text}'.")

def press_button(button, rep=1, wait=0.5):
    button = str(button).lower().strip()
    for _ in range(rep):
        if button == "win+down":
            pyautogui.hotkey("win", "down")
            print("Ho premuto WIN+DOWN.")
        elif button == "win+up":
            pyautogui.hotkey("win", "up")
            print("Ho premuto WIN+UP.")
        elif button.startswith("+"):
            pyautogui.hotkey("shift", button[1:])
            print(f"Ho premuto SHIFT+{button[1:].upper()}.")
        elif button.startswith("^"):
            pyautogui.hotkey("ctrl", button[1:])
            print(f"Ho premuto CTRL+{button[1:].upper()}.")
        elif button.startswith("!"):
            pyautogui.hotkey("alt", button[1:])
            print(f"Ho premuto ALT+{button[1:].upper()}.")
        else:
            pyautogui.press(button)
            print(f"Ho premuto {button.upper()}.")
        wait_seconds(wait)

def scroll_down(rep=3, scroll=-200, wait=0.5):
    for _ in range(rep):
        pyautogui.scroll(scroll)
        print(f"Ho eseguito uno scroll verso il basso di {abs(scroll)}.")
        wait_seconds(wait)

def scroll_up(rep=3, scroll=200, wait=0.5):
    for _ in range(rep):
        pyautogui.scroll(scroll)
        print(f"Ho eseguito uno scroll verso l'alto di {abs(scroll)}.")
        wait_seconds(wait)

# Parti di flusso
def open_gestione_raccomandazione():
    click(1030, 135) # Clicca su "Consulenza"
    click(1120, 200) # Clicca su "Nuova raccomandazione"
    wait_image("avanti")
    wait_seconds(1.5)

def open_raccomandazioni_proposte():
    click(750, 670, 1, True) # Fa click destro sul campo bianco
    press_button("down", 2) # Seleziona "Nuova proposta - Gestione patrimoniale"
    press_button("enter")
    wait_image("conferma")
    wait_seconds(0.5)

def add_new_recommendation(private, pir):
    click(700, 365) # Clicca il campo "Tipo Operazione"
    write(NUOVA_SOTTOSCRIZIONE)
    press_button("enter")
    wait_seconds(3)
    enter_amount(pir)
    click(830, 670) # Mette il focus sulla finestra
    click(830, 730) # Clicca su "Prodotto"
    select_subscription(private, pir)
    press_button("enter", 1, 3)

def select_operation(operazione):
    click(700, 365) # Clicca il campo "Tipo Operazione"
    write(operazione)
    press_button("enter")
    wait_seconds(2)

def select_the_DA2():
    click(1070, 440) # Clicca su "..."
    click_image("ricerca")
    continua = ask_yes_no("Hai selezionato il codice DA2?", "Seleziona")
    return continua

def generate_recommendation_documents():
    click(750, 670) # Mette il focus sulla finestra
    click(1044, 957) # Clicca sul pulsante "Avanti"
    wait_seconds(0.5)
    click(1044, 954) # Clicca di nuovo sul pulsante "Avanti"
    wait_seconds(20)
    click(1200, 954) # Clicca sul pulsante "Consegna"
    wait_seconds(0.5)
    click(1200, 957) # Clicca di nuovo sul pulsante "Consegna"

def confirm_new_recommendation():
    wait_image("conferma_creazione_mandato")
    wait_seconds(1)
    press_button("enter", 1, 5)

def confirm_new_deposit():
    click_image("chiudi_btn", 0.7, 90)
    press_button("enter", 2, 1.5)
    click(1213, 539) # Clicca sulla checkbox "Forza chiusura"
    press_button("enter")
    confirm_new_recommendation()

def accept_anagrafica():
    focus_window(MONITOR_MANDATI_TITLE, "y")
    wait_image("browser_annulla", 0.6, 15)
    wait_seconds(1)
    click(1760, 290) # Clicca su "Continua"
    wait_seconds(0.5)
    press_button("win+down", 1, 1)
    press_button("win+up", 1, 1)
    click_image("browser_conferma", 0.7) # click(1080, 650)

def uncheck_myGp():
    click_image("toggle_my_gp", 0.7)
    wait_seconds(0.5)
    click(812, 770) # Sposta il cursore in un punto vuoto
    scroll_down(5)
    click(812, 830) # Clicca il dropdown degli indirizzi
    press_button("down")
    press_button("enter")

def enter_questionario_antiriciclaggio(first=True):
    if first:
        wait_image("questionario_antiriciclaggio", 0.6, 15)
        wait_seconds(0.5)
    else:
        wait_seconds(10)
    click(800, 350) # Clicca su "Questionario antiriciclaggio"
    wait_image("stato_da_inserire", 0.6, 15)
    wait_seconds(1)
    if first:
        click(1596, 613) # Clicca il primo ">" del questionario
    else:
        click(1596, 663) # Clicca il secondo ">" del questionario
    wait_seconds(10)

def confirm_quadri_A_D_F():
    click(1848, 268) # Clicca il pulsante "Avanti"
    wait_seconds(2)
    click(400, 695) # Clicca le checkbox 1 e 2
    click(1165, 695)
    click(1848, 268) # Clicca il pulsante "Avanti"
    wait_seconds(2)
    click(420, 645) # Clicca il radio button
    click(1848, 268) # Clicca il pulsante "Conferma"
    wait_seconds(1.5)
    click(1160, 480) # Clicca sul dropdown della modale dell'antiriciclaggio
    press_button("down")
    press_button("enter")
    click(1060, 760) # Clicca il pulsante "OK" della modale con il dropdown
    wait_image("questionario_ok", 0.7, 10)
    wait_seconds(8)
    click(960, 660) # Clicca il pulsante "OK" della modale "Profilo di rischio non rilevante"
    wait_seconds(2)
    click_image("browser_indietro", 0.6)
    wait_seconds(15)

def download_documents():
    click(1700, 280) # Clicca il pulsante "Gestisci documenti"
    wait_seconds(3)
    click(1120, 685) # Clicca il pulsante "Conferma" nella modale
    wait_image("inserito", 0.7, 20)
    wait_seconds(5)
    click(1800, 375) # Clicca il pulsante "Seleziona tutti"
    click(1315, 375) # Clicca il pulsante "Stampa"
    wait_seconds(1)
    click(1080, 650) # Clicca il pulsante "Conferma"
    wait_seconds(30)
    click(1887, 400) # Chiude la finestra dei download

def sign_documents():
    click(1800, 375) # Clicca su "Seleziona tutti"
    click(1555, 380) # Clicca su "Segna come firmato"
    click(1070, 645) # Clicca su "Conferma" nella modale

    if not wait_image("browser_visualizza_contratti", 0.7, 20):
        click(1352, 690)
        click(1400, 375) # Clicca su "Carica scansione"
        wait_seconds(3)
        click(795, 570) # Clicca su "Carica scansione" nella modale
        wait_seconds(3)
        
        click(363, 434)
        press_button("enter")
        click(1115, 695)
        wait_image("browser_visualizza_contratti", 0.7, 20)
        wait_seconds(1)

def enter_gestione_questionari_banca():
    click(1400, 20) # Clicca il pulsante "Segnalazioni"
    click(850, 60) # Clicca il pulsante "Antiriciclaggio"
    press_button("down")
    press_button("enter")
    press_button("down", 5) # Seleziona "Gestione questionari (banca)"
    press_button("enter")

def start_verifica_questionario():
    click(1300, 630) # Clicca il pulsante "Verifica"
    press_button("enter")
    wait_seconds(8)

def enter_questionario_information():
    click(440, 650) # Spunta la checkbox "Documentazione Quadro F valutata"
    click(450, 215) # Clicca sul tab "Altre valutazioni"
    write(SCELTA_NO)
    press_button("tab", 2, 0.3)
    write(SCELTA_NO)
    press_button("tab")
    click(1160, 215) # Clicca sul tab "Adeguata verifica"
    for _ in range(3):
        write("s")
        press_button("tab", 1, 0.2)
    click(1010, 925) # Clicca su "Conferma"