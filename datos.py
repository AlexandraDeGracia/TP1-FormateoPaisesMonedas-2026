"""
Módulo de Datos.
Estilo de código: Estudiante de primer año de programación.

RESTRICCIONES STRICTAS:
- Sin diccionarios. Uso exclusivo de listas y tuplas.
- Carga de datos desde archivo CSV local y generación de archivo .toon.
"""

import formateo_strings as fs

# Variable global para almacenar los países cargados en memoria
PAISES_CARGADOS = []


def obtener_paises():
    """Retorna la lista de países cargados en memoria."""
    return PAISES_CARGADOS


def leer_csv_paises(ruta_archivo):
    """
    Lee el archivo CSV de países especificado.
    Recorre las líneas una por una, las separa por ';' usando separar_cadena
    y almacena cada país como una tupla con código ISO de 2 letras, población y área como enteros:
    (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
    """
    global PAISES_CARGADOS

    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Error: El archivo '" + ruta_archivo + "' no existe.")
        print("Por favor, verifique la ruta del archivo e intente nuevamente.")
        return None

    lineas = archivo.readlines()
    archivo.close()

    cantidad_lineas = len(lineas)
    if cantidad_lineas <= 1:
        print("\n El archivo CSV está vacío o solo contiene encabezados.")
        return None

    lista_paises = []
    indice = 1  # Iniciar en 1 para saltar la línea de encabezado (línea 0)

    while indice < cantidad_lineas:
        linea_raw = lineas[indice]
        linea_limpia = fs.limpiar_espacios_extremos(linea_raw)

        if len(linea_limpia) > 0:
            columnas = fs.separar_cadena(linea_limpia, ";")

            # Verificar que la línea tenga al menos 8 campos (Nombre a TasaCambioUSD)
            if len(columnas) >= 8:
                nombre = fs.limpiar_espacios_extremos(columnas[0])
                capital = fs.limpiar_espacios_extremos(columnas[1])
                codigo = fs.limpiar_espacios_extremos(columnas[2])
                poblacion = fs.convertir_a_entero(columnas[3])
                area = fs.convertir_a_entero(columnas[4])  # Área como entero
                moneda = fs.limpiar_espacios_extremos(columnas[5])
                codigo_moneda = fs.limpiar_espacios_extremos(columnas[6])
                tasa_usd = fs.convertir_a_flotante(columnas[7])

                pais_tuple = (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
                lista_paises.append(pais_tuple)

        indice = indice + 1

    PAISES_CARGADOS = lista_paises
    return lista_paises


def guardar_datos_toon(lista_paises, ruta_salida_toon):
    """
    Guarda los datos crudos de los países en un archivo con formato TOON.
    Estructura TOON:
    - 'paises:' en nivel 0 (0 espacios)
    - '-' solo en su línea en nivel 1 (4 espacios)
    - Todos los campos debajo en nivel 2 (8 espacios)
    - Textos entre comillas dobles, números enteros y flotantes sin comillas.
    """
    try:
        archivo = open(ruta_salida_toon, "w", encoding="utf-8")
    except OSError:
        print("Error: No se pudo crear el archivo TOON en '" + ruta_salida_toon + "'.")
        return False

    archivo.write("paises:\n")

    cantidad = len(lista_paises)
    i = 0
    while i < cantidad:
        p = lista_paises[i]
        # p es la tupla: (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
        archivo.write("    -\n")
        archivo.write('        nombre: "' + str(p[0]) + '"\n')
        archivo.write('        capital: "' + str(p[1]) + '"\n')
        archivo.write('        codigo: "' + str(p[2]) + '"\n')
        archivo.write('        poblacion: ' + str(p[3]) + '\n')
        archivo.write('        area: ' + str(p[4]) + '\n')
        archivo.write('        moneda: "' + str(p[5]) + '"\n')
        archivo.write('        codigo_moneda: "' + str(p[6]) + '"\n')
        archivo.write('        tasa_usd: ' + str(p[7]) + '\n')
        i = i + 1

    archivo.close()
    return True
