from the_csv import matrix_base
import commands
import the_csv
import keyboard
import time 
import menu

main_table = matrix_base

while True:
    time.sleep(0.05)
    menu.print_main_menu(main_table)
    time.sleep(0.25)
    
    #### Captura de tecla 
    commands.clean_buffer()
    key_pressed = keyboard.read_key()
    key_pressed = key_pressed.lower()

    if key_pressed == "down":
        main_table.add_row()
    if key_pressed == "right":
        main_table.add_col()####
    if key_pressed == "up":
        main_table.remove_row()
    if key_pressed == "left":
        main_table.remove_col()

    if key_pressed == "shift":
        main_table.entry_procotol()
    if key_pressed == "backspace":
        main_table.__init__(8,8)
    if key_pressed == "esc":
        import sys
        the_csv.quick_saved_file()
        sys.exit()
        
    ### Guardar y Cargar archivos
    if key_pressed == "f1":
        while True:
            #### Mostar el menu suavemente
            time.sleep(0.05)
            menu.print_menu_save_csv()
            time.sleep(0.25)

            #### Captura de tecla 
            commands.clean_buffer()
            key_pressed = keyboard.read_key()
            key_pressed.lower()

            if key_pressed == "shift":
                the_csv.slow_saved_file()
            if key_pressed == "space":
                the_csv.quick_saved_file()
            if key_pressed == "esc":
                break

    if key_pressed == "f2":
        while True:
            menu.print_menu_load_csv()
            
            commands.clean_buffer()
            key_pressed = keyboard.read_key()
            key_pressed.lower()

            if key_pressed == "shift":
                the_csv.slow_load_file()
            if key_pressed == "space":
                the_csv.quick_load_file()
            if key_pressed == "esc":
                break
        
    
