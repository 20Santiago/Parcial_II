# I N I C I A M O S  C O N  L A  1:

import os
import pandas as pd

class CSVReader:
    def __init__(self, file_path=None):
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
            raise ValueError("Lo sentimos, no hemos encontrado ninguna ruta CSV")
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
        selected_files = self.choose_file()
        list_data = []
        for csv_file in selected_files:
            data = pd.read_csv(csv_file)
            if data.empty:
                raise ValueError(f"El archivo CSV '{csv_file}' está vacío o no se pudo leer")
            list_data.append(data)
        return list_data

csv_reader = CSVReader()
csv_reader.prompt_file_path()  # Preguntar al usuario por la ruta del archivo
data = csv_reader.read_csv_files()
print(data)

# I N I C I A M O S  C O N  L A  3 : (Como la hice con SQL, omito la 6, 7 y 11)

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



# I N I C I A M O S  C O N  L A  1 2 :

import matplotlib.pyplot as plt
import numpy as np

def show_plot(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        plt.show()
    return wrapper

def add_grid(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        plt.grid()
    return wrapper

# Datos arbitrarios
x = np.array([18, 105, 140, 160, 180, 186, 200, 198, 180, 178, 210, 355, 320, 304, 184, 152, 278, 292, 397, 470])
y = np.array([13, 101, 132, 120, 130, 150, 110, 170, 150, 135,  90,  70, 190, 205, 160,  48, 100, 170, 260, 280])

# Ajuste de la regresión lineal
slope, intercept = np.polyfit(x, y, 1)
line = slope * x + intercept

# Gráfica de dispersión con línea de regresión
@show_plot
@add_grid
def plot_data():
    plt.scatter(x, y)
    plt.plot(x, line, color='red')

    # Etiquetas de los ejes y título
    plt.xlabel("Concentración de alcohol en la sangre [mg/100 mL]")
    plt.ylabel("Concentración de alcohol en el músculo [mg/100 g]")
    plt.title("Concentración de alcohol en el músculo [mg/100 g] vs. Concentración de alcohol en la sangre [mg/100 mL]")

plot_data()


# I N I C I A M O S  C O N  L A  1 4 :

import numpy as np
import matplotlib.pyplot as plt

def encontrar_cortes_ejex(funcion, a, b, tol=1e-6, max_iter=1000, *args, **kwargs):
    """
    Encuentra los cortes con el eje x de una función matemática definida a partir de una lambda.

    Parámetros:
        - funcion: función matemática definida a partir de una lambda.
        - a, b: límites del intervalo de búsqueda.
        - tol: tolerancia para la precisión del resultado (por defecto, 1e-6).
        - max_iter: número máximo de iteraciones (por defecto, 1000).
        - *args, **kwargs: argumentos adicionales para la función matemática.

    Retorna:
        - Una lista con las raíces encontradas.
    """
    roots = []
    fa = funcion(a, *args, **kwargs)
    fb = funcion(b, *args, **kwargs)
    if fa == 0:
        roots.append(a)
    if fb == 0:
        roots.append(b)
    if fa * fb > 0:
        raise ValueError("No hay raíces en el intervalo dado")
    c = (a + b) / 2
    i = 0
    while abs(funcion(c, *args, **kwargs)) > tol and i < max_iter:
        fc = funcion(c, *args, **kwargs)
        if fc == 0:
            roots.append(c)
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        c = (a + b) / 2
        i += 1
    roots.append(c)
    return roots

f = lambda x: x + 0.9 
roots = encontrar_cortes_ejex(f, -10, 10)

x = np.linspace(-10, 10, 100)
y = f(x)
plt.plot(x, y)
plt.scatter(roots, np.zeros_like(roots), c='r', s=50)
plt.show()




