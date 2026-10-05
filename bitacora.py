#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-05
"""
Módulo de Gestión de Bitácora del Sistema.
Permite registrar eventos y errores en formato binario (bitacora.bin),
realizar búsquedas por fecha o palabra clave, y exportar la bitácora a CSV.
"""

import datetime
import formateo_strings as fs


# Definición de función: registrarEventoBitacora
def registrarEventoBitacora(descripcion):
    """Registra un evento con fecha, hora y descripción en bitacora.bin en formato binario."""
    fechaHora = fs.obtenerSubcadena(str(datetime.datetime.now()), 0, 19)
    linea = fechaHora + "|" + descripcion + "\n"
    try:
        archivo = open("bitacora.bin", "ab")
        archivo.write(linea.encode("utf-8"))
        archivo.close()
        return True
    except OSError:
        return False


# Definición de función: leerBitacoraBin
def leerBitacoraBin():
    """Lee los registros de bitacora.bin en modo binario (rb) y los retorna como lista de tuplas."""
    try:
        archivo = open("bitacora.bin", "rb")
        contenidoBytes = archivo.read()
        archivo.close()
    except FileNotFoundError:
        return []

    contenidoTexto = contenidoBytes.decode("utf-8", errors="ignore")
    lineas = fs.separarCadena(contenidoTexto, "\n")
    listaRegistros = []
    i = 0
    cantidad = len(lineas)

    while i < cantidad:
        linea = fs.limpiarEspaciosExtremos(lineas[i])
        if len(linea) > 0:
            partes = fs.separarCadena(linea, "|")
            if len(partes) >= 2:
                fechaHora = partes[0]
                desc = partes[1]
                k = 2
                while k < len(partes):
                    desc = desc + "|" + partes[k]
                    k = k + 1
                registroTuple = (fechaHora, desc)
                listaRegistros.append(registroTuple)
        i = i + 1

    return listaRegistros


# Definición de función: buscarBitacoraPorFecha
def buscarBitacoraPorFecha(fechaBuscar):
    """Retorna una lista de registros cuya fecha o timestamp coincida con fechaBuscar."""
    todos = leerBitacoraBin()
    resultados = []
    i = 0
    cantidad = len(todos)

    while i < cantidad:
        reg = todos[i]
        fechaHora = reg[0]
        if fs.contieneSubcadena(fechaHora, fechaBuscar):
            resultados.append(reg)
        i = i + 1

    return resultados


# Definición de función: buscarBitacoraPorPalabraClave
def buscarBitacoraPorPalabraClave(palabraBuscar):
    """Retorna una lista de registros cuya descripción contenga palabraBuscar."""
    todos = leerBitacoraBin()
    resultados = []
    i = 0
    cantidad = len(todos)

    while i < cantidad:
        reg = todos[i]
        desc = reg[1]
        if fs.contieneSubcadena(desc, palabraBuscar):
            resultados.append(reg)
        i = i + 1

    return resultados


# Definición de función: exportarBitacoraCsv
def exportarBitacoraCsv(rutaSalida="bitacora.csv"):
    """Exporta todos los registros de la bitácora a un archivo CSV."""
    todos = leerBitacoraBin()
    try:
        archivo = open(rutaSalida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo CSV '" + rutaSalida + "'.")
        return False

    archivo.write("Fecha_Hora;Descripcion\n")
    i = 0
    cantidad = len(todos)

    while i < cantidad:
        reg = todos[i]
        lineaCsv = str(reg[0]) + ";" + str(reg[1]) + "\n"
        archivo.write(lineaCsv)
        i = i + 1

    archivo.close()
    return True


# Definición de función: mostrarMenuBitacora
def mostrarMenuBitacora():
    """Muestra el submenú de bitácora en la consola."""
    print("\n==================================================")
    print("  SUBMENÚ DE BITÁCORA DEL SISTEMA")
    print("==================================================")
    print("  A. Buscar por fecha")
    print("  B. Buscar por palabra clave")
    print("  C. Mostrar todos los registros")
    print("  D. Exportar bitácora a CSV")
    print("  E. Salir del submenú")
    print("--------------------------------------------------")


# Definición de función: ejecutarBuscarPorFecha
def ejecutarBuscarPorFecha():
    """Opción A del submenú: solicita fecha y muestra los registros coincidentes."""
    fechaInput = input("\nIngrese la fecha a buscar (AAAA-MM-DD): ")
    fechaLimpia = fs.limpiarEspaciosExtremos(fechaInput)
    resultados = buscarBitacoraPorFecha(fechaLimpia)
    cantidad = len(resultados)

    print("\n==================================================")
    print("  RESULTADOS DE BÚSQUEDA POR FECHA ('" + fechaLimpia + "')")
    print("==================================================")

    if cantidad == 0:
        print("No se encontraron registros para la fecha ingresada.")
    else:
        i = 0
        while i < cantidad:
            reg = resultados[i]
            print("  " + str(i + 1) + ". [" + str(reg[0]) + "] " + str(reg[1]))
            i = i + 1

    print("==================================================")
    registrarEventoBitacora("Submenú Bitácora: Búsqueda por fecha '" + fechaLimpia + "', Coincidencias: " + str(cantidad))


# Definición de función: ejecutarBuscarPorPalabraClave
def ejecutarBuscarPorPalabraClave():
    """Opción B del submenú: solicita palabra clave y muestra registros coincidentes."""
    palabraInput = input("\nIngrese la palabra clave a buscar en la descripción: ")
    palabraLimpia = fs.limpiarEspaciosExtremos(palabraInput)
    resultados = buscarBitacoraPorPalabraClave(palabraLimpia)
    cantidad = len(resultados)

    print("\n==================================================")
    print("  RESULTADOS DE BÚSQUEDA POR PALABRA CLAVE ('" + palabraLimpia + "')")
    print("==================================================")

    if cantidad == 0:
        print("No se encontraron registros con la palabra clave ingresada.")
    else:
        i = 0
        while i < cantidad:
            reg = resultados[i]
            print("  " + str(i + 1) + ". [" + str(reg[0]) + "] " + str(reg[1]))
            i = i + 1

    print("==================================================")
    registrarEventoBitacora("Submenú Bitácora: Búsqueda por palabra clave '" + palabraLimpia + "', Coincidencias: " + str(cantidad))


# Definición de función: ejecutarMostrarTodos
def ejecutarMostrarTodos():
    """Opción C del submenú: muestra todos los registros almacenados en bitacora.bin."""
    todos = leerBitacoraBin()
    cantidad = len(todos)

    print("\n==================================================")
    print("          REGISTROS DE LA BITÁCORA")
    print("==================================================")

    if cantidad == 0:
        print("No hay registros en la bitácora.")
    else:
        i = 0
        while i < cantidad:
            reg = todos[i]
            print("  " + str(i + 1) + ". [" + str(reg[0]) + "] " + str(reg[1]))
            i = i + 1

    print("==================================================")
    registrarEventoBitacora("Submenú Bitácora: Mostrar todos los registros (Total: " + str(cantidad) + ")")


# Definición de función: ejecutarExportarCsv
def ejecutarExportarCsv():
    """Opción D del submenú: exporta los registros a bitacora.csv."""
    exito = exportarBitacoraCsv("bitacora.csv")
    if exito:
        todos = leerBitacoraBin()
        total = len(todos)
        print("\n Bitácora exportada exitosamente a 'bitacora.csv'.")
        registrarEventoBitacora("Submenú Bitácora: Exportar bitácora a CSV ('bitacora.csv'). Total exportados: " + str(total))


# Definición de función: ejecutarSubmenuBitacora
def ejecutarSubmenuBitacora():
    """Opción 8 del menú principal: controla el submenú de la bitácora."""
    opcionSub = ""
    registrarEventoBitacora("Opción 8: El usuario ingresó al submenú de bitácora.")

    while opcionSub != "E":
        mostrarMenuBitacora()
        opcionInput = input("Seleccione una opción (A-E): ")
        opcionSub = fs.aMayusculas(fs.limpiarEspaciosExtremos(opcionInput))

        if opcionSub == "A":
            ejecutarBuscarPorFecha()
        elif opcionSub == "B":
            ejecutarBuscarPorPalabraClave()
        elif opcionSub == "C":
            ejecutarMostrarTodos()
        elif opcionSub == "D":
            ejecutarExportarCsv()
        elif opcionSub == "E":
            print("\nRegresando al menú principal...")
            registrarEventoBitacora("Submenú Bitácora: El usuario regresó al menú principal.")
        else:
            print("\nOpción no válida. Por favor, ingrese una letra de la A a la E.")
            registrarEventoBitacora("Error: Opción no válida en el submenú de bitácora: '" + opcionInput + "'")
