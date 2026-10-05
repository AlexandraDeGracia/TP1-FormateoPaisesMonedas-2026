"""
Módulo de Gestión y Persistencia de Datos.
Carga, valida y almacena datos de países y monedas desde y hacia archivos CSV y TOON
utilizando listas, tuplas y validaciones carácter por carácter.
"""

import formateo_strings as fs


def leer_csv_paises(ruta_archivo):
    """
    Lee el archivo CSV de países especificado.
    Valida que cada línea contenga al menos 8 columnas y datos numéricos válidos (población > 0, área > 0).
    Omite líneas inválidas imprimiendo un mensaje con el número de línea.
    Retorna una lista de tuplas o None si el archivo no existe o no contiene datos válidos.
    """
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
    lineas_omitidas = 0
    indice = 1  # Iniciar en 1 para saltar la línea de encabezado (línea 0)

    while indice < cantidad_lineas:
        linea_raw = lineas[indice]
        linea_num = indice + 1
        linea_limpia = fs.limpiar_espacios_extremos(linea_raw)

        if len(linea_limpia) > 0:
            columnas = fs.separar_cadena(linea_limpia, ";")

            if len(columnas) < 8:
                print("Advertencia: Línea " + str(linea_num) + " ignorada por tener menos de 8 columnas.")
                lineas_omitidas = lineas_omitidas + 1
            else:
                pob_str = columnas[3]
                area_str = columnas[4]
                tasa_str = columnas[7]

                if not fs.es_entero_valido(pob_str) or not fs.es_entero_valido(area_str) or not fs.es_flotante_valido(tasa_str):
                    print("Advertencia: Línea " + str(linea_num) + " ignorada por contener datos numéricos inválidos.")
                    lineas_omitidas = lineas_omitidas + 1
                else:
                    poblacion = fs.convertir_a_entero(pob_str)
                    area = fs.convertir_a_entero(area_str)
                    tasa_usd = fs.convertir_a_flotante(tasa_str)

                    if poblacion <= 0 or area <= 0:
                        print("Advertencia: Línea " + str(linea_num) + " ignorada por tener población o área menor o igual a 0.")
                        lineas_omitidas = lineas_omitidas + 1
                    else:
                        nombre = fs.limpiar_espacios_extremos(columnas[0])
                        capital = fs.limpiar_espacios_extremos(columnas[1])
                        codigo = fs.limpiar_espacios_extremos(columnas[2])
                        moneda = fs.limpiar_espacios_extremos(columnas[5])
                        codigo_moneda = fs.limpiar_espacios_extremos(columnas[6])

                        pais_tuple = (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
                        lista_paises.append(pais_tuple)

        indice = indice + 1

    if lineas_omitidas > 0:
        print("Se omitieron " + str(lineas_omitidas) + " líneas por contener datos inválidos.")

    if len(lista_paises) == 0:
        print("Error: No se encontró ningún país válido en el archivo.")
        return None

    return lista_paises


def guardar_datos_toon(lista_paises, ruta_salida_toon):
    """
    Guarda los datos de los países en un archivo con formato TOON.
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


def remover_comillas(texto):
    """Remueve comillas dobles al inicio y final de un texto usando un ciclo while."""
    texto_limpio = fs.limpiar_espacios_extremos(texto)
    longitud = len(texto_limpio)
    if longitud >= 2 and texto_limpio[0] == '"' and texto_limpio[longitud - 1] == '"':
        resultado = ""
        i = 1
        while i < longitud - 1:
            resultado = resultado + texto_limpio[i]
            i = i + 1
        return resultado
    return texto_limpio


def obtener_valor_clave_toon(linea_limpia):
    """
    Dada una línea del TOON tipo 'nombre: "Argentina"',
    separa por ':' y retorna (clave, valor_limpio).
    """
    partes = fs.separar_cadena(linea_limpia, ":")
    if len(partes) >= 2:
        clave = fs.limpiar_espacios_extremos(partes[0])
        valor_raw = partes[1]
        k = 2
        while k < len(partes):
            valor_raw = valor_raw + ":" + partes[k]
            k = k + 1

        valor_limpio = remover_comillas(fs.limpiar_espacios_extremos(valor_raw))
        return clave, valor_limpio
    return "", ""


def leer_datos_toon(ruta_toon):
    """
    Lee los países desde el archivo paises_datos.toon.
    Parsea y valida las líneas de forma manual sin diccionarios.
    Retorna una lista de tuplas con los datos de cada país o None si el archivo no existe o no tiene países válidos.
    """
    try:
        archivo = open(ruta_toon, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Primero ejecute la Opción 1")
        return None

    lineas = archivo.readlines()
    archivo.close()

    lista_paises = []
    cantidad_lineas = len(lineas)
    i = 0

    nombre = ""
    capital = ""
    codigo = ""
    poblacion = 0
    area = 0
    moneda = ""
    codigo_moneda = ""
    tasa_usd = 0.0
    tiene_datos = False

    while i < cantidad_lineas:
        linea_raw = lineas[i]
        linea_limpia = fs.limpiar_espacios_extremos(linea_raw)

        if linea_limpia == "-":
            if tiene_datos:
                if len(nombre) > 0 and poblacion > 0 and area > 0:
                    pais_tuple = (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
                    lista_paises.append(pais_tuple)
                nombre = ""
                capital = ""
                codigo = ""
                poblacion = 0
                area = 0
                moneda = ""
                codigo_moneda = ""
                tasa_usd = 0.0
                tiene_datos = False
        else:
            clave, valor = obtener_valor_clave_toon(linea_limpia)
            if clave == "nombre":
                nombre = valor
                tiene_datos = True
            elif clave == "capital":
                capital = valor
            elif clave == "codigo":
                codigo = valor
            elif clave == "poblacion":
                if fs.es_entero_valido(valor):
                    poblacion = fs.convertir_a_entero(valor)
                else:
                    poblacion = 0
            elif clave == "area":
                if fs.es_entero_valido(valor):
                    area = fs.convertir_a_entero(valor)
                else:
                    area = 0
            elif clave == "moneda":
                moneda = valor
            elif clave == "codigo_moneda":
                codigo_moneda = valor
            elif clave == "tasa_usd":
                if fs.es_flotante_valido(valor):
                    tasa_usd = fs.convertir_a_flotante(valor)
                else:
                    tasa_usd = 0.0

        i = i + 1

    if tiene_datos and len(nombre) > 0 and poblacion > 0 and area > 0:
        pais_tuple = (nombre, capital, codigo, poblacion, area, moneda, codigo_moneda, tasa_usd)
        lista_paises.append(pais_tuple)

    if len(lista_paises) == 0:
        print("\n No se encontraron datos válidos de países.")
        return None

    return lista_paises
