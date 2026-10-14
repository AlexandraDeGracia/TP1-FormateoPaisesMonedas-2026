#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-14
"""
Módulo de Gestión y Persistencia de Datos.
Carga, valida y almacena datos de países y monedas desde y hacia archivos CSV y TOON
(paises.toon y tasas_cambio.toon) utilizando listas, tuplas y ciclos while.
"""

import time
import formateo_strings as fs
import formatos as fmt
import bitacora


# Definición de función: validarFilaCsv
def validarFilaCsv(columnas, lineaNum):
    """Valida los campos de una fila del CSV. Retorna (paisTuple, advertencia)."""
    if len(columnas) < 8:
        msg = "Advertencia: Línea " + str(lineaNum) + " ignorada por tener menos de 8 columnas."
        return None, msg

    pobStr = columnas[3]
    areaStr = columnas[4]
    tasaStr = columnas[7]

    if not fs.esEnteroValido(pobStr) or not fs.esEnteroValido(areaStr) or not fs.esFlotanteValido(tasaStr):
        msg = "Advertencia: Línea " + str(lineaNum) + " ignorada por contener datos numéricos inválidos."
        return None, msg

    poblacion = fs.convertirAEntero(pobStr)
    area = fs.convertirAEntero(areaStr)
    tasaUsd = fs.convertirAFlotante(tasaStr)

    nombre = fs.limpiarEspaciosExtremos(columnas[0])
    capital = fs.limpiarEspaciosExtremos(columnas[1])
    codigo = fs.limpiarEspaciosExtremos(columnas[2])
    moneda = fs.limpiarEspaciosExtremos(columnas[5])
    codigoMoneda = fs.limpiarEspaciosExtremos(columnas[6])

    if poblacion <= 0 or area <= 0 or tasaUsd <= 0 or len(nombre) == 0:
        msg = "Advertencia: Línea " + str(lineaNum) + " ignorada por datos inválidos (población, área o tasa <= 0, o nombre vacío)."
        return None, msg

    paisTuple = (nombre, capital, codigo, poblacion, area, moneda, codigoMoneda, tasaUsd)
    return paisTuple, None


# Definición de función: procesarLineasCsv
def procesarLineasCsv(lineas):
    """Procesa cada línea del archivo CSV a partir de la línea 1 omitiendo inválidas."""
    listaPaises = []
    lineasOmitidas = 0
    cantidadLineas = len(lineas)
    indice = 1

    while indice < cantidadLineas:
        lineaLimpia = fs.limpiarEspaciosExtremos(lineas[indice])
        lineaNum = indice + 1

        if len(lineaLimpia) > 0:
            columnas = fs.separarCadena(lineaLimpia, ";")
            paisTuple, advertencia = validarFilaCsv(columnas, lineaNum)
            if advertencia is not None:
                print(advertencia)
                lineasOmitidas = lineasOmitidas + 1
            else:
                listaPaises.append(paisTuple)

        indice = indice + 1

    return listaPaises, lineasOmitidas


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

    if len(lineas) <= 1:
        print("\n El archivo CSV está vacío o solo contiene encabezados.")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaArchivo + "' está vacío o solo contiene encabezados.")
        return None

    listaPaises, lineasOmitidas = procesarLineasCsv(lineas)

    if lineasOmitidas > 0:
        print("Se omitieron " + str(lineasOmitidas) + " líneas por contener datos inválidos.")
        bitacora.registrarEventoBitacora("Advertencia: Se omitieron " + str(lineasOmitidas) + " líneas por datos inválidos en '" + rutaArchivo + "'.")

    if len(listaPaises) == 0:
        print("Error: No se encontró ningún país válido en el archivo.")
        bitacora.registrarEventoBitacora("Error: No se encontró ningún país válido en '" + rutaArchivo + "'.")
        return None

    return listaPaises


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


# Definición de función: guardarPaisesToon
def guardarPaisesToon(listaPaises, rutaSalidaToon="paises.toon"):
    """Guarda los países en formato TOON (nombre, capital, codigo, poblacion, area, codigo_moneda)."""
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
        codMoneda = p[6] if len(p) >= 8 else p[5]
        archivo.write("    -\n")
        archivo.write('        nombre: "' + str(p[0]) + '"\n')
        archivo.write('        capital: "' + str(p[1]) + '"\n')
        archivo.write('        codigo: "' + str(p[2]) + '"\n')
        archivo.write('        poblacion: ' + str(p[3]) + '\n')
        archivo.write('        area: ' + str(p[4]) + '\n')
        archivo.write('        codigo_moneda: "' + str(codMoneda) + '"\n')
        i = i + 1

    archivo.close()
    return True


# Definición de función: extraerCamposPaisToon
def extraerCamposPaisToon(lineaLimpia, nombre, capital, codigo, poblacion, area, codigoMoneda):
    """Extrae y actualiza los campos de país según la clave encontrada en la línea TOON."""
    clave, valor = obtenerValorClaveToon(lineaLimpia)
    if clave == "nombre":
        nombre = valor
    elif clave == "capital":
        capital = valor
    elif clave == "codigo":
        codigo = valor
    elif clave == "poblacion":
        poblacion = fs.convertirAEntero(valor) if fs.esEnteroValido(valor) else 0
    elif clave == "area":
        area = fs.convertirAEntero(valor) if fs.esEnteroValido(valor) else 0
    elif clave == "codigo_moneda":
        codigoMoneda = valor
    return nombre, capital, codigo, poblacion, area, codigoMoneda


# Definición de función: procesarLineasPaisesToon
def procesarLineasPaisesToon(lineas):
    """Procesa las líneas de paises.toon y retorna la lista de tuplas de países."""
    listaPaises = []
    i = 0
    cantidad = len(lineas)
    nombre = ""
    capital = ""
    codigo = ""
    poblacion = 0
    area = 0
    codigoMoneda = ""
    tieneDatos = False

    while i < cantidad:
        lineaLimpia = fs.limpiarEspaciosExtremos(lineas[i])
        if lineaLimpia == "-":
            if tieneDatos and len(nombre) > 0 and poblacion > 0 and area > 0:
                listaPaises.append((nombre, capital, codigo, poblacion, area, codigoMoneda))
            nombre, capital, codigo, poblacion, area, codigoMoneda = "", "", "", 0, 0, ""
            tieneDatos = False
        else:
            nombre, capital, codigo, poblacion, area, codigoMoneda = extraerCamposPaisToon(
                lineaLimpia, nombre, capital, codigo, poblacion, area, codigoMoneda
            )
            if len(nombre) > 0:
                tieneDatos = True
        i = i + 1

    if tieneDatos and len(nombre) > 0 and poblacion > 0 and area > 0:
        listaPaises.append((nombre, capital, codigo, poblacion, area, codigoMoneda))

    return listaPaises


# Definición de función: leerPaisesToon
def leerPaisesToon(rutaToon="paises.toon"):
    """Lee países desde paises.toon y registra la métrica en la bitácora."""
    tiempoInicio = time.time()
    try:
        archivo = open(rutaToon, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Primero ejecute la Opción 1")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaToon + "' no existe. Primero ejecute la Opción 1.")
        return None

    lineas = archivo.readlines()
    archivo.close()

    listaPaises = procesarLineasPaisesToon(lineas)
    tiempoFin = time.time()
    duracion = fmt.formatear4Decimales(tiempoFin - tiempoInicio)
    total = len(listaPaises)

    if total == 0:
        print("\n No se encontraron datos válidos de países.")
        bitacora.registrarEventoBitacora("Error: No se encontraron datos válidos en '" + rutaToon + "'.")
        return None

    bitacora.registrarEventoBitacora("Lectura TOON: " + rutaToon + ", Registros: " + str(total) + ", Tiempo de respuesta: " + duracion + " s")
    return listaPaises


# Definición de función: guardarTasasCambioToon
def guardarTasasCambioToon(fechaTasa, listaMonedas, rutaSalidaToon="tasas_cambio.toon"):
    """Guarda la fecha y la lista de monedas únicas en tasas_cambio.toon."""
    try:
        archivo = open(rutaSalidaToon, "w", encoding="utf-8")
    except OSError:
        print("Error: No se pudo crear el archivo TOON en '" + rutaSalidaToon + "'.")
        bitacora.registrarEventoBitacora("Error: No se pudo crear el archivo TOON '" + rutaSalidaToon + "'.")
        return False

    archivo.write('fecha_tasa: "' + str(fechaTasa) + '"\n')
    archivo.write("monedas:\n")
    cantidad = len(listaMonedas)
    i = 0
    while i < cantidad:
        m = listaMonedas[i]
        archivo.write("    -\n")
        archivo.write('        codigo: "' + str(m[0]) + '"\n')
        archivo.write('        nombre: "' + str(m[1]) + '"\n')
        archivo.write('        tasa_usd: ' + str(m[2]) + '\n')
        i = i + 1

    archivo.close()
    return True


# Definición de función: extraerCamposMonedaToon
def extraerCamposMonedaToon(lineaLimpia, codigo, nombre, tasaUsd):
    """Extrae y actualiza los campos de moneda según la clave encontrada en la línea TOON."""
    clave, valor = obtenerValorClaveToon(lineaLimpia)
    if clave == "codigo":
        codigo = valor
    elif clave == "nombre":
        nombre = valor
    elif clave == "tasa_usd":
        tasaUsd = fs.convertirAFlotante(valor) if fs.esFlotanteValido(valor) else 0.0
    return codigo, nombre, tasaUsd


# Definición de función: procesarLineasTasasToon
def procesarLineasTasasToon(lineas):
    """Procesa las líneas de tasas_cambio.toon extrayendo fecha_tasa y lista de monedas."""
    fechaTasa = ""
    listaMonedas = []
    i = 0
    cantidad = len(lineas)
    codigo = ""
    nombre = ""
    tasaUsd = 0.0
    tieneDatos = False

    while i < cantidad:
        lineaLimpia = fs.limpiarEspaciosExtremos(lineas[i])
        clave, valor = obtenerValorClaveToon(lineaLimpia)
        if clave == "fecha_tasa":
            fechaTasa = valor
        elif lineaLimpia == "-":
            if tieneDatos and len(codigo) > 0 and len(nombre) > 0 and tasaUsd > 0.0:
                listaMonedas.append((codigo, nombre, tasaUsd))
            codigo, nombre, tasaUsd = "", "", 0.0
            tieneDatos = False
        else:
            codigo, nombre, tasaUsd = extraerCamposMonedaToon(lineaLimpia, codigo, nombre, tasaUsd)
            if len(codigo) > 0:
                tieneDatos = True
        i = i + 1

    if tieneDatos and len(codigo) > 0 and len(nombre) > 0 and tasaUsd > 0.0:
        listaMonedas.append((codigo, nombre, tasaUsd))

    return fechaTasa, listaMonedas


# Definición de función: leerTasasCambioToon
def leerTasasCambioToon(rutaToon="tasas_cambio.toon"):
    """Lee tasas de cambio desde tasas_cambio.toon y registra la métrica en la bitácora."""
    tiempoInicio = time.time()
    try:
        archivo = open(rutaToon, "r", encoding="utf-8")
    except FileNotFoundError:
        print("\n Primero ejecute la Opción 1")
        bitacora.registrarEventoBitacora("Error: El archivo '" + rutaToon + "' no existe. Primero ejecute la Opción 1.")
        return None, None

    lineas = archivo.readlines()
    archivo.close()

    fechaTasa, listaMonedas = procesarLineasTasasToon(lineas)
    tiempoFin = time.time()
    duracion = fmt.formatear4Decimales(tiempoFin - tiempoInicio)
    total = len(listaMonedas)

    if total == 0:
        print("\n No se encontraron datos válidos de monedas.")
        bitacora.registrarEventoBitacora("Error: No se encontraron datos válidos en '" + rutaToon + "'.")
        return None, None

    bitacora.registrarEventoBitacora("Lectura TOON: " + rutaToon + ", Registros: " + str(total) + ", Tiempo de respuesta: " + duracion + " s")
    return fechaTasa, listaMonedas


# Definición de función: combinarPaisesConTasas
def combinarPaisesConTasas(listaPaises, listaMonedas):
    """Combina los datos de países con sus tasas de cambio según el código de moneda."""
    resultado = []
    cantPaises = len(listaPaises)
    cantMonedas = len(listaMonedas)
    i = 0

    while i < cantPaises:
        p = listaPaises[i]
        codBuscado = p[5] if len(p) == 6 else p[6]
        nombreMoneda = ""
        tasaUsd = 0.0

        j = 0
        while j < cantMonedas:
            m = listaMonedas[j]
            if m[0] == codBuscado:
                nombreMoneda = m[1]
                tasaUsd = m[2]
                j = cantMonedas
            else:
                j = j + 1

        tupla = (p[0], p[1], p[2], p[3], p[4], nombreMoneda, codBuscado, tasaUsd)
        resultado.append(tupla)
        i = i + 1

    return resultado
