###
import csv
from csv import reader

###
import pathlib

###
from rich.console import Console
from rich.table import Table

###
clean_console = Console().clear
my_table = Table(title="Main_matrix")

####
matrix_base = [[1,2,3],
               [4,5,6],
               [7,8,10],]

###
date_base = pathlib.Path("one.csv")
with open(date_base, mode="w", newline="", encoding="utf-8") as f:
     writer = csv.writer(f)
     writer.writerows(matrix_base)

###
with open(date_base, mode="r", encoding="utf-8") as f:
     read = csv.reader(f)
     convert_matrix = list(read)

### columnas
for cell in range(len(convert_matrix[0])):
     my_table.add_column(f"Col {cell}")

### Filas
for row in convert_matrix:
     my_table.add_row(*row)

###
Console().print(my_table)