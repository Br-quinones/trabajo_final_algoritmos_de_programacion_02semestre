from the_matrix import MyTable
from csv import reader
import pathlib
import csv

matrix_base = MyTable(8,8)
our_file = pathlib.Path("saved/current_file.csv")

def slow_saved_file():
     new_name = input("Ingrese el nombre del archivo: ")
     our_file = pathlib.Path(f"saved/{new_name}.csv")

     with open(our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)

def quick_saved_file():
     with open(our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)

def quick_load_file():
     with open(our_file, mode="r", encoding="utf-8") as f:
          read = csv.reader(f)
          convert_matrix = list(read)
