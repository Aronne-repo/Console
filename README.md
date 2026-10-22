# Desktop Automation Framework

Framework di automazione desktop sviluppato in Python per automatizzare applicazioni Windows tramite simulazione di input utente, riconoscimento immagini e interazione con controlli UI.

## Technical Stack
- Python 3.x
- PyAutoGUI
- Pywinauto
- UIAutomation
- OpenCV
- Tkinter / TkCalendar
- NumPy
- PyInstaller
- Features
- Automazione di applicazioni Windows
- Click, digitazione e movimento del mouse
- Gestione finestre e controlli UI
- Riconoscimento immagini tramite OpenCV
- Automazione basata su coordinate o controlli nativi
- Creazione di eseguibili standalone con PyInstaller
- Installation

## Create virtual environment and install dependencies:

```
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
```

## Project Launch

- Run the main application:
```
python main.py
```

- Run a specific automation script:
```
python scripts/my_automation.py
```

## Generate standalone executable with PyInstaller:
```
pyinstaller main.py --onefile
```

## Main Dependencies
- PyAutoGUI
- Pywinauto
- UIAutomation
- OpenCV
- NumPy
- TkCalendar
- PyInstaller

## Project Structure
```
project/
│
├── main.py
├── requirements.txt
├── resources/
├── screenshots/
├── scripts/
├── utils/
├── tests/
└── venv/
```

### Notes
Sistema operativo supportato: Windows
La risoluzione e lo zoom dello schermo possono influenzare la precisione del riconoscimento dei file .png
