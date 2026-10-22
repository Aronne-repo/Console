import tkinter as tk
from scripts.as400.cambio_ambiente_e_classe import cambia_ambiente_e_classe
from scripts.as400.cag_di_gruppo_su_singolo import cag_di_gruppo_su_singolo
from scripts.as400.esegui_batch import esegui_batch
from scripts.as400.estrai_codici_da2 import estrai_codici_da2
from scripts.as400.controllo_data_quality import controllo_data_quality
from scripts.as400.esegui_nuovo_conferimento import esegui_nuovo_conferimento
from scripts.sql_developer.cambia_abi_utenza import cambia_abi_utenza
from scripts.sql_developer.estrai_codici_url import estrai_codici_url
from scripts.sibank.apri_gpm_web import apri_gpm_web
from scripts.sibank.crea_nuovo_mandato import crea_nuovo_mandato
from scripts.sibank.esegui_cambio_linea import esegui_cambio_linea
from scripts.sibank.compila_quadro_h import compila_quadro_h
from scripts.sibank.nuovo_conferimento import nuovo_conferimento

ROOT = None

def on_closing():
    print("Ho chiuso la console.")
    ROOT.destroy()

def main():
    global ROOT
    ROOT = tk.Tk()
    ROOT.title("Seleziona il processo da avviare")
    ROOT.protocol("WM_DELETE_WINDOW", on_closing)

    buttons = [("[SQL Developer] Cambia ABI dell'utenza", cambia_abi_utenza),
               ("[SQL Developer] Estrai codici per URL mandati", estrai_codici_url),
               ("[AS/400] Cambia ambiente e classe dell'utenza", cambia_ambiente_e_classe),
               ("[AS/400] Imposta CAG di gruppo su CAG singolo", cag_di_gruppo_su_singolo),
               ("[AS/400] Esegui il batch", esegui_batch),
               ("[AS/400] Estrai codici DA2", estrai_codici_da2),
               ("[AS/400] Esegui controllo di data quality", controllo_data_quality),
               ("[AS/400] Esegui un nuovo conferimento", esegui_nuovo_conferimento),
               ("[Sibank Legacy] Crea nuovo mandato", crea_nuovo_mandato),
               ("[Sibank Legacy] Esegui cambio linea", esegui_cambio_linea),
               ("[Sibank Legacy] Compila il Quadro H", compila_quadro_h),
               ("[Sibank Legacy] Esegui un nuovo conferimento", nuovo_conferimento),
               ("[Sibank Modernizzato] Apri GPM web", apri_gpm_web)]

    for text, command in buttons:
        btn = tk.Button(ROOT, text=text, width=50, command=command)
        btn.pack(padx=10, pady=5)

    ROOT.update_idletasks()
    width = ROOT.winfo_width()
    height = ROOT.winfo_height()
    x = (ROOT.winfo_screenwidth() // 2) - (width // 2)
    y = (ROOT.winfo_screenheight() // 2) - (height // 2)
    ROOT.geometry(f"+{x}+{y}")

    ROOT.mainloop()

if __name__ == "__main__":
    main()