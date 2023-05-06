##       **Parcial II (Programación)**     \:tongue\:

### *Santiago Aguilar Cardenas*


 ### **¿Qué hacen los códigos?**



> Para el primer código:

    Este código define una clase CSVReader que permite al usuario seleccionar y leer uno o varios archivos CSV en una ubicación dada. A continuación, se explica cada método de la clase:

     __init__(self, file_path=None): El constructor de la clase inicializa el atributo file_path con la ruta proporcionada por el usuario o la ruta actual si no se proporciona una. Si se proporciona una ruta que no existe, se genera una excepción ValueError.

    prompt_file_path(self): Este método le pide al usuario que ingrese una ruta de archivo. Si el usuario presiona Enter sin ingresar una ruta, se utiliza la ruta actual. Si se ingresa una ruta que no existe, se genera una excepción ValueError.

    choose_file(self): Este método enumera los archivos en la ubicación especificada y solicita al usuario que seleccione uno o varios archivos CSV de la lista. Si no se encuentran archivos CSV, se genera una excepción ValueError. Si se selecciona un índice de archivo inválido, también se genera una excepción ValueError. El método devuelve una lista de rutas de archivo seleccionadas por el usuario.

    read_csv_files(self): Este método utiliza el método choose_file() para obtener una lista de rutas de archivo seleccionadas por el usuario. Luego, lee cada archivo CSV en la lista utilizando la biblioteca Pandas y lo agrega a una lista de DataFrames. Si un archivo está vacío o no se pudo leer, se genera una excepción ValueError. El método devuelve la lista de DataFrames.

    Después de definir la clase CSVReader, se crea una instancia de ella (csv_reader = CSVReader()) y se le solicita al usuario que proporcione la ruta del archivo utilizando el método prompt_file_path(). Luego, se llama al método read_csv_files() para leer uno o varios archivos CSV en la ubicación proporcionada y se imprime el resultado.

> Para el segundo código:

Este código crea y administra una base de datos SQLite que contiene dos tablas, VENTAS y PORCENTAJE. A continuación, se unen estas dos tablas mediante una consulta SQL y se imprimen los resultados.

Aquí se muestra un desglose del código:

- Primero, se importa la biblioteca SQLite3.

- Se crea una conexión a la base de datos "Homecenter" utilizando la función `connect()` y se crea un objeto cursor que permite ejecutar comandos SQL.

- A continuación, se crea la tabla VENTAS utilizando la función `execute()` del objeto cursor. La tabla tiene cuatro columnas: id, Familia, Presupuesto y Cumplimiento. La columna id se define como clave primaria. 

- A continuación, se insertan datos en la tabla VENTAS utilizando la función `executemany()` del objeto cursor y se proporcionan los datos en forma de una lista de tuplas llamada `datosVentas`. 

- Luego, se crea la tabla PORCENTAJE utilizando la función `execute()` del objeto cursor. La tabla tiene dos columnas: id y Porcentaje. La columna id se define como clave primaria.

- A continuación, se insertan datos en la tabla PORCENTAJE utilizando la función `executemany()` del objeto cursor y se proporcionan los datos en forma de una lista de tuplas llamada `datosPorcentaje`. 

- Luego, se une las tablas VENTAS y PORCENTAJE mediante una consulta SQL utilizando la función `execute()` del objeto cursor. Se seleccionan todas las columnas de ambas tablas y se unen las filas donde el id es igual en ambas tablas.

- Se obtienen los resultados de la consulta utilizando la función `fetchall()` del objeto cursor y se almacenan en una variable llamada `resultados`.

- Se imprimen los resultados de la consulta utilizando un bucle for y se utilizan tabulaciones para organizar la salida. Primero, se imprimen los encabezados de las columnas y luego se imprimen las filas de datos de la consulta.

- Finalmente, se cierra la conexión a la base de datos utilizando la función `close()`.


> Para el tercer código:

    Este código importa la biblioteca matplotlib.pyplot para crear una gráfica de dispersión con una línea de regresión. También importa la biblioteca numpy para realizar el ajuste de la regresión lineal. Los datos son dados por dos arrays x y y que representan la concentración de alcohol en la sangre y en el músculo, respectivamente.

    Se definen dos decoradores show_plot y add_grid. show_plot es un decorador que recibe una función y devuelve otra función wrapper que llama a la función original y luego muestra la gráfica utilizando plt.show(). add_grid es otro decorador que recibe una función y devuelve otra función wrapper que llama a la función original y luego agrega una grilla a la gráfica utilizando plt.grid().

    Se realiza el ajuste de la regresión lineal utilizando np.polyfit(x, y, 1). Esto ajusta los datos x e y a una línea recta y devuelve los valores de la pendiente y la intercepción de la línea.

    La función plot_data utiliza los decoradores definidos anteriormente para mostrar la gráfica. Dentro de la función, se utiliza plt.scatter para crear una gráfica de dispersión con los datos x e y, y plt.plot para agregar la línea de regresión utilizando los valores de la pendiente e intercepción calculados anteriormente. También se establecen las etiquetas de los ejes y el título de la gráfica utilizando plt.xlabel, plt.ylabel y plt.title.

    Por último, se llama a la función plot_data para mostrar la gráfica.

> Para el cuarto código:

El código define una función llamada `encontrar_cortes_ejex` que utiliza el método de bisección para encontrar las raíces de una función matemática en un intervalo dado. La función toma como entrada la función matemática `funcion` definida a partir de una lambda, los límites del intervalo de búsqueda `a` y `b`, la tolerancia `tol` y el número máximo de iteraciones `max_iter`. La función devuelve una lista con las raíces encontradas.

Luego, se define una función lambda `f` que define una función lineal `y = x + 0.9`. Se llama a la función `encontrar_cortes_ejex` con los argumentos `f`, `-10` y `10` para encontrar las raíces de `f` en el intervalo `[-10,10]`.

Finalmente, se grafica la función `f` en el intervalo `[-10,10]` utilizando `numpy` y `matplotlib`. Se agregan puntos rojos en el eje x en las ubicaciones de las raíces encontradas. El resultado es una gráfica de la función `y = x + 0.9` con los puntos donde la función corta el eje x resaltados en rojo.

