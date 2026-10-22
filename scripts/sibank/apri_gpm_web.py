from utils.utils import open_edge, enter_sibank, wait_seconds, click, press_button, close_window_by_name
from utils.global_variables import (DESKTOP_TITLE, RETROSPORTELLO_TITLE)

def apri_gpm_web():
    open_edge()
    enter_sibank(False)

    click(970, 20) # Clicca il pulsante "Finanza"
    click(1115, 60) # Clicca il pulsante "GPM"
    press_button("up")
    press_button("enter")
    wait_seconds(5)
    close_window_by_name(DESKTOP_TITLE)
    close_window_by_name(RETROSPORTELLO_TITLE)
    print("Ho aperto GPM web.")

if __name__ == "__main__":
    apri_gpm_web()