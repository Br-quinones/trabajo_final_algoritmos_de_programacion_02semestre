import menu
from the_matrix import MyTable

my_table = MyTable(2,2)
while True:
    my_table.see()

    ###
    what_add = str(input("Que desea agregar (r/c): "))

    if what_add == "c":
        my_table.add_col()
    if what_add == "r":
        my_table.add_row()

    menu.clean()
 