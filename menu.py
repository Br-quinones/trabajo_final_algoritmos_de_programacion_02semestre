from rich.console import Console
from rich.table import Table

def main_menu(matrix_to_print):
    #### Limpiar pantalla y definir variable 
    Console().clear()
    line_rule = Console().rule

    #####
    line_rule(style="White")
    heat_menu_table = Table(show_header=False, expand=True)

    heat_menu_table.add_column(justify="left",   ratio=1)
    heat_menu_table.add_column(justify="center", ratio=1)
    heat_menu_table.add_column(justify="right",  ratio=1)

    heat_menu_table.add_row("F1: Load CSV", "F2: Save CSV", "f3: Exit")
    #####

    line_rule(style="White")
    matrix_to_print.see()

    ###
    line_rule(style="White")
    commands_menu_rich = Table(show_header=False, expand=True)

    commands_menu_rich.add_column(justify="left",   ratio=1)
    commands_menu_rich.add_column(justify="center", ratio=1)
    commands_menu_rich.add_column(justify="right",  ratio=1)

    commands_menu_rich.add_row("Use 'arrows' to move", "Use 'control' to change to mode add or remove", "Use 'Enter' to input")

    Console().print(commands_menu_rich)


