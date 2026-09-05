from the_matrix import MyTable
import menu

main_table = MyTable(8,2)

while True:
    menu.main_menu(main_table)
    
    what_add = input("Ingrese a agregar (r/c): ")

    if what_add == "r":
        main_table.add_row()
    if what_add == "c":
        main_table.add_col()

    menu.clean()