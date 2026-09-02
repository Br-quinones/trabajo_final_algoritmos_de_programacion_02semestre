###
import csv
from csv import reader

###
import pathlib


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