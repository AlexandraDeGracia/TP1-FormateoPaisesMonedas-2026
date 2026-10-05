#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-05
"""
Módulo de Gestión y Persistencia de Datos.
Carga, valida y almacena datos de países y monedas desde y hacia archivos CSV y TOON
utilizando listas, tuplas y validaciones carácter por carácter.
"""

import formateo_strings as fs
import bitacora


# Definición de función: leerCsvPaises
def leerCsvPaises(rutaArchivo):
    """Lee el archivo CSV de países especificado. Omite líneas inválidas y retorna lista de tuplas."""
    try:
        archivo = open(rutaArchivo, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Error: El archivo '" + rutaArchivo + "' no existe.")
        print("Por favor, verifique la ruta del archivo e intente nuevamente.")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaArchivo + "' no existe.")
        return None

    lineas = archivo.readlines()
    archivo.close()

    cantidadLineas = len(lineas)
    if cantidadLineas <= 1:
        print("\n El archivo CSV está vacío o solo contiene encabezados.")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaArchivo + "' está vacío o solo contiene encabezados.")
        return None

    listaPaises = []
    lineasOmitidas = 0
    indice = 1

    while indice < cantidadLineas:
        lineaRaw = lineas[indice]
        lineaNum = indice + 1
        lineaLimpia = fs.limpiarEspaciosExtremos(lineaRaw)

        if len(lineaLimpia) > 0:
            columnas = fs.separarCadena(lineaLimpia, ";")

            if len(columnas) < 8:
                print("Advertencia: Línea " + str(lineaNum) + " ignorada por tener menos de 8 columnas.")
                lineasOmitidas = lineasOmitidas + 1
            else:
                pobStr = columnas[3]
                areaStr = columnas[4]
                tasaStr = columnas[7]

                if not fs.esEnteroValido(pobStr) or not fs.esEnteroValido(areaStr) or not fs.esFlotanteValido(tasaStr):
                    print("Advertencia: Línea " + str(lineaNum) + " ignorada por contener datos numéricos inválidos.")
                    lineasOmitidas = lineasOmitidas + 1
                else:
                    poblacion = fs.convertirAEntero(pobStr)
                    area = fs.convertirAEntero(areaStr)
                    tasaUsd = fs.convertirAFlotante(tasaStr)

                    if poblacion <= 0 or area <= 0:
                        print("Advertencia: Línea " + str(lineaNum) + " ignorada por tener población o área menor o igual a 0.")
                        lineasOmitidas = lineasOmitidas + 1
                    else:
                        nombre = fs.limpiarEspaciosExtremos(columnas[0])
                        capital = fs.limpiarEspaciosExtremos(columnas[1])
                        codigo = fs.limpiarEspaciosExtremos(columnas[2])
                        moneda = fs.limpiarEspaciosExtremos(columnas[5])
                        codigoMoneda = fs.limpiarEspaciosExtremos(columnas[6])

                        paisTuple = (nombre, capital, codigo, poblacion, area, moneda, codigoMoneda, tasaUsd)
                        listaPaises.append(paisTuple)

        indice = indice + 1

    if lineasOmitidas > 0:
        print("Se omitieron " + str(lineasOmitidas) + " líneas por contener datos inválidos.")
        bitacora.registrarEventoBitacora("Advertencia: Se omitieron " + str(lineasOmitidas) + " líneas por datos inválidos en '" + rutaArchivo + "'.")

    if len(listaPaises) == 0:
        print("Error: No se encontró ningún país válido en el archivo.")
        bitacora.registrarEventoBitacora("Error: No se encontró ningún país válido en '" + rutaArchivo + "'.")
        return None

    return listaPaises


# Definición de función: guardarDatosToon
def guardarDatosToon(listaPaises, rutaSalidaToon):
    """Guarda los datos de los países en un archivo con formato TOON."""
    try:
        archivo = open(rutaSalidaToon, "w", encoding="utf-8")
    except OSError:
        print("Error: No se pudo crear el archivo TOON en '" + rutaSalidaToon + "'.")
        bitacora.registrarEventoBitacora("Error: No se pudo crear el archivo TOON '" + rutaSalidaToon + "'.")
        return False

    archivo.write("paises:\n")

    cantidad = len(listaPaises)
    i = 0
    while i < cantidad:
        p = listaPaises[i]
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


# Definición de función: removerComillas
def removerComillas(texto):
    """Remueve comillas dobles al inicio y final de un texto usando un ciclo while."""
    textoLimpio = fs.limpiarEspaciosExtremos(texto)
    longitud = len(textoLimpio)
    if longitud >= 2 and textoLimpio[0] == '"' and textoLimpio[longitud - 1] == '"':
        resultado = ""
        i = 1
        while i < longitud - 1:
            resultado = resultado + textoLimpio[i]
            i = i + 1
        return resultado
    return textoLimpio


# Definición de función: obtenerValorClaveToon
def obtenerValorClaveToon(lineaLimpia):
    """Dada una línea del TOON tipo 'nombre: "Argentina"', retorna (clave, valorLimpio)."""
    partes = fs.separarCadena(lineaLimpia, ":")
    if len(partes) >= 2:
        clave = fs.limpiarEspaciosExtremos(partes[0])
        valorRaw = partes[1]
        k = 2
        while k < len(partes):
            valorRaw = valorRaw + ":" + partes[k]
            k = k + 1

        valorLimpio = removerComillas(fs.limpiarEspaciosExtremos(valorRaw))
        return clave, valorLimpio
    return "", ""


# Definición de función: leerDatosToon
def leerDatosToon(rutaToon):
    """Lee los países desde el archivo paises_datos.toon sin diccionarios."""
    try:
        archivo = open(rutaToon, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Primero ejecute la Opción 1")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaToon + "' no existe. Primero ejecute la Opción 1.")
        return None

    lineas = archivo.readlines()
    archivo.close()

    listaPaises = []
    cantidadLineas = len(lineas)
    i = 0

    nombre = ""
    capital = ""
    codigo = ""
    poblacion = 0
    area = 0
    moneda = ""
    codigoMoneda = ""
    tasaUsd = 0.0
    tieneDatos = False

    while i < cantidadLineas:
        lineaRaw = lineas[i]
        lineaLimpia = fs.limpiarEspaciosExtremos(lineaRaw)

        if lineaLimpia == "-":
            if tieneDatos:
                if len(nombre) > 0 and poblacion > 0 and area > 0:
                    paisTuple = (nombre, capital, codigo, poblacion, area, moneda, codigoMoneda, tasaUsd)
                    listaPaises.append(paisTuple)
                nombre = ""
                capital = ""
                codigo = ""
                poblacion = 0
                area = 0
                moneda = ""
                codigoMoneda = ""
                tasaUsd = 0.0
                tieneDatos = False
        else:
            clave, valor = obtenerValorClaveToon(lineaLimpia)
            if clave == "nombre":
                nombre = valor
                tieneDatos = True
            elif clave == "capital":
                capital = valor
            elif clave == "codigo":
                codigo = valor
            elif clave == "poblacion":
                if fs.esEnteroValido(valor):
                    poblacion = fs.convertirAEntero(valor)
                else:
                    poblacion = 0
            elif clave == "area":
                if fs.esEnteroValido(valor):
                    area = fs.convertirAEntero(valor)
                else:
                    area = 0
            elif clave == "moneda":
                moneda = valor
            elif clave == "codigo_moneda":
                codigoMoneda = valor
            elif clave == "tasa_usd":
                if fs.esFlotanteValido(valor):
                    tasaUsd = fs.convertirAFlotante(valor)
                else:
                    tasaUsd = 0.0

        i = i + 1

    if tieneDatos and len(nombre) > 0 and poblacion > 0 and area > 0:
        paisTuple = (nombre, capital, codigo, poblacion, area, moneda, codigoMoneda, tasaUsd)
        listaPaises.append(paisTuple)

    if len(listaPaises) == 0:
        print("\n No se encontraron datos válidos de países.")
        bitacora.registrarEventoBitacora("Error: No se encontraron datos válidos de países en '" + rutaToon + "'.")
        return None

    return listaPaises
