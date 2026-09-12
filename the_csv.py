from the_matrix import MyTable
from csv import reader
import commands
import pathlib
import csv

matrix_base = MyTable(8, 8)

def slow_saved_file():
     new_name = input("Ingrese el nombre del archivo: ").strip()
     our_file = pathlib.Path(f"saved/{new_name}.csv")

     with open(file=our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)

     commands.task_complete()

def quick_saved_file():
     our_file = pathlib.Path("saved/current_file.csv")
     with open(file=our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)
     
     commands.task_complete()

def quick_load_file():
     our_file = pathlib.Path("saved/current_file.csv")
     with open(file=our_file, mode="r", encoding="utf-8") as f:
          read = csv.reader(f)
          convert_matrix = list(read)
