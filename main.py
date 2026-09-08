from the_matrix import MyTable
import keyboard
import time 
import menu

main_table = MyTable(8,2)

while True:
    menu.main_menu(main_table)
    
    ####
    key_pressed = keyboard.read_key()

    if key_pressed == "down":
        main_table.add_row()
        time.sleep(0.20)
    if key_pressed == "right":
        main_table.add_col()
        time.sleep(0.20)
    if key_pressed == "up":
        main_table.remove_row()
        time.sleep(0.20)
    if key_pressed == "left":
        main_table.remove_col()
        time.sleep(0.20)
