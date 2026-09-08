from rich.table import Table
from rich.console import Console

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

    def convert_to_rich(self):
        self.my_table_rich = Table(show_header=False, show_lines=True)

        for col in self.my_table[0]:
            self.my_table_rich.add_column()
        
        for row in self.my_table:
            self.my_table_rich.add_row(*row)

        return self.my_table_rich


    # Mostrar la tabla en formato rich 
    def see(self):
        Console().print(self.convert_to_rich())
    
    ### Metodos para añadir filas y columnas
    def add_row(self):
        self.my_table.append(["x" for cell in self.my_table[0]])
 
    def add_col(self):
        for row in self.my_table:
            row.append("x")

    ### Metodo para remover filas y columnas
    def remove_row(self):
        if not len(self.my_table) <= 1:
            self.my_table.pop()

    def remove_col(self):
        if not len(self.my_table[0]) <= 1:
            for row in self.my_table:
                row.pop()