from rich.console import Console
from rich.table import Table

def clean():
    Console().clear()

def line():
    Console().rule(style="White")

def heat_menu():
    heat_menu_table = Table(show_header=False, expand=True)

    heat_menu_table.add_column(justify="left",   ratio=1)
    heat_menu_table.add_column(justify="center", ratio=1)
    heat_menu_table.add_column(justify="right",  ratio=1)

    heat_menu_table.add_row("F1: Load CSV", "F2: Save CSV", "f3: Exit")

    Console().print(heat_menu_table)
    
def commands_menu():
    commands_menu_rich = Table(show_header=False, expand=True)

    commands_menu_rich.add_column(justify="left",   ratio=1)
    commands_menu_rich.add_column(justify="center", ratio=1)
    commands_menu_rich.add_column(justify="right",  ratio=1)

    commands_menu_rich.add_row("Use 'arrows' to move", "Use 'control + arrows' to add or remove column or row", "coming soon")

    Console().print(commands_menu_rich)


def main_menu(matrix_to_print):
    line()
    heat_menu()
    line()
    matrix_to_print.see()
    line()
    commands_menu()
    line()



