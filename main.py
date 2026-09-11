from the_csv import matrix_base
import the_csv
import keyboard
import time 
import menu
import sys

main_table = matrix_base

while True:
    menu.print_main_menu(main_table)
    
    #### Captura de tecla 
    key_pressed = keyboard.read_key()
    key_pressed.lower()
    time.sleep(0.20)

    if key_pressed == "down":
        main_table.add_row()
    if key_pressed == "right":
        main_table.add_col()
    if key_pressed == "up":
        main_table.remove_row()
    if key_pressed == "left":
        main_table.remove_col()

    if key_pressed == "shift":
        main_table.entry_procotol()

    if key_pressed == "esc":
        sys.exit()

    ### Guardar y Cargar archivos
    if key_pressed == "f1":
        while True:
            menu.print_menu_save_csv()

            key_pressed = keyboard.read_key()
            key_pressed.lower()
            time.sleep(0.20)

            if key_pressed == "shift":
                the_csv.slow_saved_file()
            if key_pressed == "space":
                the_csv.quick_saved_file()
            if key_pressed == "esc":
                break

    if key_pressed == "f2":
        while True:
            menu.print_menu_load_csv()

            key_pressed = keyboard.read_key()
            key_pressed.lower()


        
    
