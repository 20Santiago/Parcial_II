import os
import pandas as pd


#Para el punto número 1:
class CSVReader:
    def _init_(self, file_path=None):
        if file_path is None:
            self.file_path = os.getcwd()  # Si no se proporciona una ruta, usar la ruta actual
        else:
            self.file_path = file_path
            if not os.path.exists(file_path):
                raise ValueError(f"La ruta proporcionada '{file_path}' no existe")

    def prompt_file_path(self):
        file_path = input("Por favor, ingrese la ruta del archivo o presione Enter para usar la ruta actual:\n")
        if file_path == "":
            self.file_path = os.getcwd()
        else:
            self.file_path = file_path
            if not os.path.exists(file_path):
                raise ValueError(f"La ruta proporcionada '{file_path}' no existe")

    def choose_file(self):
        files = os.listdir(self.file_path)
        csv_files = [f for f in files if f.endswith('.csv')]
        if not csv_files:
            raise ValueError("No se encontraron archivos CSV en la ruta especificada")
        print("Archivos CSV encontrados:")
        for i, file in enumerate(csv_files):
            print(f"{i+1}. {file}")
        file_indexes = input("Seleccione los archivos que desea abrir separados por comas: ").split(",")
        selected_files = []
        for index in file_indexes:
            file_index = int(index) - 1
            if file_index < 0 or file_index >= len(csv_files):
                raise ValueError("Índice de archivo inválido")
            selected_files.append(os.path.join(self.file_path, csv_files[file_index]))
        return selected_files

    def read_csv_files(self):
        csv_files = self.choose_file()
        list_data = []
        for csv_file in csv_files:
            data = pd.read_csv(csv_file)
            list_data.append(data)
        return list_data
    
csv_reader = CSVReader()
csv_reader.prompt_file_path()  # Preguntar al usuario por la ruta del archivo
data = csv_reader.read_csv_files()
print(data)


import sqlite3

miConexion = sqlite3.connect("Homecenter")
miCursor = miConexion.cursor()

# create VENTAS table
miCursor.execute("""
    CREATE TABLE VENTAS (
        id INTEGER PRIMARY KEY,
        Familia VARCHAR(10),
        Presupuesto DECIMAL,
        Cumplimiento DECIMAL
        )
""")

# insert data into VENTAS table
datosVentas = [
    (1, "Muebles", "15.45", "19.60"),
    (2, "Organizadores", "6.38", "4.47"),
    (3, "Menaje", "9.68", "5.05"),
    (4, "Decoración", "12.91", "9.45"),
    (5, "Aire Libre", "8.84", "5.23")
]
miCursor.executemany("INSERT INTO VENTAS VALUES (?,?,?,?)", datosVentas)

# create PORCENTAJE table
miCursor.execute("""
    CREATE TABLE PORCENTAJE (
        id INTEGER PRIMARY KEY,
        Porcentaje DECIMAL
        )
""")

# insert data into PORCENTAJE table
datosPorcentaje = [
    (1, "126.00"),
    (2, "70.00"),
    (3, "52.00"),
    (4, "73.00"),
    (5, "59.00")
]
miCursor.executemany("INSERT INTO PORCENTAJE VALUES (?,?)", datosPorcentaje)

# join tables using SQL query
miCursor.execute("""
    SELECT VENTAS.id, VENTAS.Familia, VENTAS.Presupuesto, VENTAS.Cumplimiento, PORCENTAJE.Porcentaje
    FROM VENTAS JOIN PORCENTAJE ON VENTAS.id = PORCENTAJE.id
""")

# get results and print them
resultados = miCursor.fetchall()

# print headers
print("ID".ljust(4), "Familia".ljust(15), "Presupuesto".ljust(15), "Cumplimiento".ljust(15), "Porcentaje".ljust(15))

for fila in resultados:
    # print row data
    print(str(fila[0]).ljust(4), fila[1].ljust(15), str(fila[2]).ljust(15), str(fila[3]).ljust(15), str(fila[4]).ljust(15))

# close connection
miConexion.close()








