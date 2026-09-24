from the_csv import matrix_base
import commands
import the_csv
import keyboard
import menu

the_csv.create_path()
main_table = matrix_base

while True:
    ### Imprimir de forma limpia el tablero
    menu.print_main_menu(main_table)

    #### Captura de tecla
    # Una limpiada de buffer
    commands.clean_buffer()

    # Captamos la tecla entrada
    key_pressed = keyboard.read_event()

    # Verificamos
    if key_pressed.event_type == keyboard.KEY_UP:
        continue

    key_pressed = key_pressed.name.lower()

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
            ### Imprimir de forma limpia el tablero
            menu.print_menu_load_csv()

            #### Captura de tecla
            # Una limpiada de buffer
            commands.clean_buffer()

            # Captamos la tecla entrada
            key_pressed = keyboard.read_event()

            # Verificamos
            if key_pressed.event_type == keyboard.KEY_UP:
                continue

            key_pressed = key_pressed.name.lower()

            if key_pressed == "shift":
                the_csv.slow_saved_file()
            if key_pressed == "space":
                the_csv.quick_saved_file()
            if key_pressed == "esc":
                break

    if key_pressed == "f2":
        while True:
            ### Imprimir de forma limpia el tablero
            menu.print_menu_load_csv()

            #### Captura de tecla
            # Una limpiada de buffer
            commands.clean_buffer()

            # Captamos la tecla entrada
            key_pressed = keyboard.read_event()

            # Verificamos
            if key_pressed.event_type == keyboard.KEY_UP:
                continue

            key_pressed = key_pressed.name.lower()

            if key_pressed == "shift":
                the_csv.slow_load_file()
            if key_pressed == "space":
                the_csv.quick_load_file()
            if key_pressed == "esc":
                break


