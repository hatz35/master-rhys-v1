#===================== MASTER =====================
from internal.basic import clear_screen, prompt, wait
from customize import customize_menu
from analyze import analyze_menu
from matches import matches_menu
import os

#STARTING MENU

menu_text = ('''\n\n~~~~~~~~~~~~ ALPHRID - THE MASTER MENU ~~~~~~~~~~~~
    1. Customize Database         - Press 1
    2. Arena                      - Press 2
    3. Analyze Database           - Press 3
''')

def main_menu():
    clear_screen()
    try:
        print(menu_text)
        p = prompt(True, "Press a Number: ")
        if p == 1:
            customize_menu()
        elif p == 2:
            matches_menu()
        elif p == 3:
            analyze_menu()
        else:
            print("Try Again. Type 1, 2 or 3")
            wait(2)
            main_menu()

    except ValueError as err:
        clear_screen()
        print(err)
        print("Try Again\n\n\n")
        wait(1)
        main_menu()

main_menu()
