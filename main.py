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
    while True:
        # Una limpiada de buffer
        commands.clean_buffer()

        # Captamos la tecla entrada
        key_pressed = keyboard.read_event()

        # Verificamosf
        if key_pressed.event_type == keyboard.KEY_UP:
            continue
        else:
            key_pressed = key_pressed.name.lower()
            break

    if key_pressed in ["down", "flecha abajo", "abajo"]:
        main_table.add_row()
    if key_pressed in ["right", "flecha derecha", "derecha"]:
        main_table.add_col()
    if key_pressed in ["up", "flecha arriba", "arriba"]:
        main_table.remove_row()
    if key_pressed in ["left", "flecha izquierda", "izquierda"]:
        main_table.remove_col()

    if key_pressed in ["shift", "mayúsculas", "mayusculas", "shift izquierdo", "shift derecho", "mayús", "mayus"]:
        main_table.entry_procotol()
    if key_pressed in ["backspace", "retroceso"]:
        main_table.__init__(8,8)
    if key_pressed in ["esc", "escape"]:
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

            if key_pressed in ["shift", "mayúsculas", "mayusculas", "shift izquierdo", "shift derecho", "mayús", "mayus"]:
                the_csv.slow_saved_file()
            if key_pressed in ["space", "espacio", "barra espaciadora"]:
                the_csv.quick_saved_file()
            if key_pressed in ["esc", "escape"]:
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

            if key_pressed in ["shift", "mayúsculas", "mayusculas", "shift izquierdo", "shift derecho", "mayús", "mayus"]:
                the_csv.slow_load_file()
            if key_pressed in ["space", "espacio", "barra espaciadora"]:
                the_csv.quick_load_file()
            if key_pressed in ["esc", "escape"]:
                break