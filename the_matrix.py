from rich.table import Table
from rich.console import Console
import commands

class MyTable():
    def __init__(self, size_col, size_row):        
        #### Creacion
        self.my_table = []

        for row in range(size_row):
            self.my_table.append([])

        for col in self.my_table:
            for cell in range(size_col):
                col.append("x")

        ### Numeracion 
        cont = 0
        for i in range(len(self.my_table[0])):
            self.my_table[0][i] = str(cont)
            cont += 1

        cont = 0
        for j in range(len(self.my_table)):
            self.my_table[j][0] = str(cont)
            cont += 1

    ### Mostrar la tabla en formato rich 
    def see(self):
        self.my_table_rich = Table(show_header=False, show_lines=True)

        for col in self.my_table[0]:
            self.my_table_rich.add_column()
        
        for row in self.my_table: 
            self.my_table_rich.add_row(*row)

        Console().print(self.my_table_rich)

    ### Entrada de datos a la tabla
    def entry_procotol(self):
        # Entrada de datos por el usuario
        axis_row = input("Ingrese la posicion en filas: ").strip()
        axis_col = input("Ingrese la posicion en columnas: ").strip()
        data = str(input("Ingrese su dato a colocar en la tabla: "))

        # Proteccion al codigo
        try:
            axis_row, axis_col = int(axis_row), int(axis_col)
        except:
            return None
        if axis_row == 0 or axis_col == 0:
            return None
        if len(self.my_table) < axis_row:
            return None
        if len(self.my_table[0]) < axis_col:
            return None

        # Si pasa todos los filtros
        self.my_table[(axis_row)][(axis_col)] = data
        commands.task_complete()

    ### Metodos para añadir filas y columnas
    def add_row(self):
        self.my_table.append([])

        for current_cell in range(len(self.my_table[0])):
            if current_cell == 0:
                number_to_add = int(self.my_table[-2][0]) + 1
                self.my_table[-1].append(str(number_to_add))
            else:
                self.my_table[-1].append("x")
 
    def add_col(self):
        for current_row in range(len(self.my_table)):
            if current_row == 0:
                number_to_add = int(self.my_table[0][-1]) + 1
                self.my_table[current_row].append(str(number_to_add))
            else:
                self.my_table[current_row].append("x")

    ### Metodo para remover filas y columnas
    def remove_row(self):
        if not len(self.my_table) <= 1:
            self.my_table.pop()
 
    def remove_col(self):
        if not len(self.my_table[0]) <= 1:
            for row in self.my_table:
                row.pop()