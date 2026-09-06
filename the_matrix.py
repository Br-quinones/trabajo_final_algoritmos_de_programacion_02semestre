from rich.table import Table
from rich.console import Console

class MyTable():
    def __init__(self, size_col, size_row):
        self.my_table = [["x" for col in range(size_col)]for row in range(size_row)]

    def convert_to_rich(self):
        self.my_table_rich = Table(show_header=False, show_lines=True)

        for col in self.my_table:
            self.my_table_rich.add_column()
        
        for row in self.my_table:
            self.my_table_rich.add_row(*row)

        return self.my_table_rich

    def see(self):
        Console().print(self.convert_to_rich())
    
    def add_row(self):
        self.my_table.append(["x" for cell in self.my_table[0]])
 
    def add_col(self):
        for row in self.my_table:
            row.append("x")

    def remove_row(self):
        self.my_table.pop()

    def remove_col(self):
        for row in self.my_table:
            row.pop()