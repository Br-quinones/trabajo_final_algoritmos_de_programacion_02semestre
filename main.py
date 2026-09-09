from the_matrix import MyTable
import keyboard
import time 
import menu
import sys

main_table = MyTable(8,8)

while True:
    menu.main_menu(main_table)
    
    #### Captura de tecla 
    key_pressed = keyboard.read_key()
    key_pressed.lower()

    ### Una minusia para evitar teclas fantasmas
    time.sleep(0.20)

    if key_pressed == "down":
        main_table.add_row()
    if key_pressed == "right":
        main_table.add_col()
    if key_pressed == "up":
        main_table.remove_row()
    if key_pressed == "left":
        main_table.remove_col()

    if key_pressed == "ctrl":
        main_table.entry_procotol()

    if key_pressed == "f3":
        sys.exit()
