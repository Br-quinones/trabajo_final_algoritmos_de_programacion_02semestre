from the_matrix import MyTable
import commands
import pathlib
import csv

matrix_base = MyTable(8, 8)

def create_path():
     pathlib.Path("saved").mkdir(parents=True, exist_ok=True)

#### Cargar archivos
def slow_load_file():
     try:
          name_file = input("Ingrese el nombre del archivo: ").strip()
          our_file = pathlib.Path(f"saved/{name_file}.csv")

          with open(file=our_file, mode="r", encoding="utf-8") as f:
               read = csv.reader(f)
               convert_matrix = list(read)
               matrix_base.replace_table(convert_matrix)

          matrix_base.apply_numeration()
          commands.task_complete()
     except Exception as e:
          commands.task_complete(e)

def quick_load_file():
     try:
          our_file = pathlib.Path("saved/current_file.csv")
          with open(file=our_file, mode="r", encoding="utf-8") as f:
               read = csv.reader(f)
               convert_matrix = list(read)
               matrix_base.replace_table(convert_matrix)

          matrix_base.apply_numeration()
          commands.task_complete()
     except Exception as e:
          commands.task_complete(e)

### Guardar archivos
def slow_saved_file():
     name_file = input("Ingrese el nombre del archivo: ").strip()
     our_file = pathlib.Path(f"saved/{name_file}.csv")

     with open(file=our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)

     matrix_base.apply_numeration()
     commands.task_complete()

def quick_saved_file():
     our_file = pathlib.Path("saved/current_file.csv")
     with open(file=our_file, mode="w", newline="", encoding="utf-8") as f:
          writer = csv.writer(f)
          writer.writerows(matrix_base.my_table)

     matrix_base.apply_numeration()
     commands.task_complete()



