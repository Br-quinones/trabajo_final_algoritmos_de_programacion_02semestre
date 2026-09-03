import menu
from the_matrix import MyTable

main_table = MyTable(8,2)
while True:
    main_table.see()

    what_add = input("Ingrese a agregar (r/c): ")

    if what_add == "r":
        main_table.add_row()
    if what_add == "c":
        main_table.add_col()

    menu.clean()