from rich.table import Table
from rich.console import Console

class MyTable():
    def __init__(self, size_x, size_y):
        self.my_table = Table(show_header=False, show_lines=True)

        for col in range(size_x):
            self.my_table.add_column()
        for row in range(size_y):
            self.my_table.add_row(f"{row}.row" + "a")

    def see_matrix(self):
        Console().print(self.my_table)