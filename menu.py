from rich.console import Console
from rich.table import Table
from pathlib import Path
import commands

def print_main_menu(matrix_to_print):
    ######## Limpiar pantalla y definir variable
    commands.clean_display()
    line_rule = Console().rule

    ######## Menu superior (Barra de tareas)
    line_rule(style="White")
    heat_menu_table = Table(show_header=False, expand=True)

    heat_menu_table.add_column(justify="left",   ratio=1)
    heat_menu_table.add_column(justify="center", ratio=1)
    heat_menu_table.add_column(justify="right",  ratio=1)

    heat_menu_table.add_row("F1: Save CSV", "F2: Load CSV", "ESC: Exit")

    Console().print(heat_menu_table)

    ######## Mostrar Tabla principal
    line_rule(style="White")
    matrix_to_print.see()

    ######## Menu inferior (Area de trabajo)
    line_rule(style="White")
    commands_menu_rich = Table(show_header=False, expand=True)

    commands_menu_rich.add_column(justify="left",   ratio=1)
    commands_menu_rich.add_column(justify="center", ratio=1)
    commands_menu_rich.add_column(justify="right",  ratio=1)

    commands_menu_rich.add_row("Use 'arrows' to add or remove rows or columns", "Use 'shift' to enter data", "Use 'backspace' to reset table")

    Console().print(commands_menu_rich)

def print_menu_save_csv():
    ######## Limpiar pantalla y definir variable
    commands.clean_display()
    line_rule = Console().rule

    ######## Menu superior (El titulo)
    line_rule(style="White")
    heat_menu_table = Table(show_header=False, expand=True)

    heat_menu_table.add_column(justify="center", ratio=1)

    heat_menu_table.add_row("Menu para guardar o sobreescribir archivos")

    Console().print(heat_menu_table)

    ######## Menu del medio (Archivos existentes)
    line_rule(style="White")
    print_list_csv()

    ######## Menu inferior (Area de comandos)
    line_rule(style="White")
    commands_menu_rich = Table(show_header=False, expand=True)

    commands_menu_rich.add_column(justify="left",   ratio=1)
    commands_menu_rich.add_column(justify="center",   ratio=1)
    commands_menu_rich.add_column(justify="right",  ratio=1)

    commands_menu_rich.add_row("Use 'shift' to enter the name", "Use 'space' to saved as 'current_file'", "Use 'esc' to exit to menu",)

    Console().print(commands_menu_rich)

def print_menu_load_csv():
    ######## Limpiar pantalla y definir variable
    commands.clean_display()
    line_rule = Console().rule

    ######## Menu superior (El titulo)
    line_rule(style="White")
    heat_menu_table = Table(show_header=False, expand=True)

    heat_menu_table.add_column(justify="center", ratio=1)

    heat_menu_table.add_row("Menu para cargar archivos")

    Console().print(heat_menu_table)

    ######## Menu del medio (Archivos existentes)
    line_rule(style="White")
    print_list_csv()

    ######## Menu inferior (Area de comandos)
    line_rule(style="White")
    commands_menu_rich = Table(show_header=False, expand=True)

    commands_menu_rich.add_column(justify="left",   ratio=1)
    commands_menu_rich.add_column(justify="center",   ratio=1)
    commands_menu_rich.add_column(justify="right",  ratio=1)

    commands_menu_rich.add_row("Use 'shift' to enter the name", "Use 'space' to load 'current_file'", "Use 'esc' to exit to menu",)

    Console().print(commands_menu_rich)

def print_list_csv():
    the_path = Path("saved")

    if the_path.exists() and the_path.is_dir():
        cont = 0
        for item in the_path.iterdir():
            print(f"{cont}. {item.name}")
            cont += 1
