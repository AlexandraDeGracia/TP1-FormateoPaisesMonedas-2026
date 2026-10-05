"""
Módulo Principal - TP1.
Sistema de Formateo y Análisis de Datos de Países y Monedas.
Proporciona la interfaz de consola, menú de navegación y flujo de ejecución principal.
"""

import datetime
import datos
import formateo_strings as fs
import calculos as calc
import reportes


# Definición de función: mostrarMenu
def mostrarMenu():
    """Muestra el menú principal de opciones en la consola según la Sección 5 de la consigna."""
    print("\n==================================================")
    print("  SISTEMA DE PAISES Y MONEDAS (TP1)")
    print("==================================================")
    print("  1. Descargar datos de países (CSV)")
    print("  2. Procesar y normalizar nombres de países")
    print("  3. Procesar datos poblacionales y geográficos")
    print("  4. Procesar datos de monedas")
    print("  5. Generar reporte de países en TXT")
    print("  6. Generar reporte de monedas en HTML")
    print("  7. Generar reporte de densidad poblacional en HTML")
    print("  8. Submenú de bitácora")
    print("  9. Salir")
    print("--------------------------------------------------")


# Definición de función: solicitarRutaCsv
def solicitarRutaCsv():
    """Solicita al usuario la ruta del archivo CSV y retorna la ruta limpia."""
    rutaInput = input("Ingrese el nombre/ruta del archivo CSV (Presione Enter para 'paises.csv'): ")
    rutaLimpia = fs.limpiarEspaciosExtremos(rutaInput)
    if len(rutaLimpia) == 0:
        return "paises.csv"
    return rutaLimpia


# Definición de función: imprimirResultadosOpcion1
def imprimirResultadosOpcion1(totalPaises, top5Poblacion, top5Area, fechaHoy, totalMonedas, top5MayorValor, top5MenorValor):
    """Imprime en consola los resultados procesados de la Opción 1."""
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 1")
    print("==================================================")

    print("\n--- PAÍSES ---")
    print("• Cantidad de países cargados: " + str(totalPaises))

    print("\n• 5 Países con MAYOR población:")
    i = 0
    while i < len(top5Poblacion):
        p = top5Poblacion[i]
        print("  " + str(i + 1) + ". " + str(p[0]) + " (" + str(p[2]) + ") - Población: " + str(p[3]))
        i = i + 1

    print("\n• 5 Países con MENOR área (km²):")
    i = 0
    while i < len(top5Area):
        p = top5Area[i]
        print("  " + str(i + 1) + ". " + str(p[0]) + " (" + str(p[2]) + ") - Área: " + str(p[4]) + " km²")
        i = i + 1

    print("\n--- MONEDAS ---")
    print("• Fecha de la tasa de cambio: " + fechaHoy)
    print("• Cantidad de monedas cargadas: " + str(totalMonedas))

    print("\n• Top 5 monedas con MAYOR valor frente al USD (Tasa más baja):")
    i = 0
    while i < len(top5MayorValor):
        m = top5MayorValor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n• Top 5 monedas con MENOR valor frente al USD (Tasa más alta):")
    i = 0
    while i < len(top5MenorValor):
        m = top5MenorValor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n==================================================")


# Definición de función: ejecutarOpcion1
def ejecutarOpcion1():
    """Opción 1: Carga los datos del archivo CSV, los guarda en .toon y muestra estadísticas."""
    print("\n--- OPCIÓN 1: DESCARGAR DATOS DE PAÍSES (CSV) ---")
    rutaCsv = solicitarRutaCsv()

    print("Cargando datos desde: " + rutaCsv + " ...")
    listaPaises = datos.leerCsvPaises(rutaCsv)

    if listaPaises is None or len(listaPaises) == 0:
        print("No se pudieron cargar los datos. Regresando al menú principal.")
        return

    archivoToon = "paises_datos.toon"
    exitoToon = datos.guardarDatosToon(listaPaises, archivoToon)
    if exitoToon:
        print("Datos crudos guardados exitosamente en '" + archivoToon + "'.")

    totalPaises = len(listaPaises)
    paisesPorPob = calc.ordenarPaisesPorPoblacionDescendente(listaPaises)
    top5Poblacion = calc.obtenerPrimerosElementos(paisesPorPob, 5)

    paisesPorArea = calc.ordenarPaisesPorAreaAscendente(listaPaises)
    top5Area = calc.obtenerPrimerosElementos(paisesPorArea, 5)

    fechaHoy = str(datetime.date.today())

    monedasUnicas = calc.extraerMonedasUnicas(listaPaises)
    totalMonedas = len(monedasUnicas)

    monedasMayorValor = calc.ordenarMonedasPorTasa(monedasUnicas, descendente=False)
    top5MayorValor = calc.obtenerPrimerosElementos(monedasMayorValor, 5)

    monedasMenorValor = calc.ordenarMonedasPorTasa(monedasUnicas, descendente=True)
    top5MenorValor = calc.obtenerPrimerosElementos(monedasMenorValor, 5)

    imprimirResultadosOpcion1(totalPaises, top5Poblacion, top5Area, fechaHoy, totalMonedas, top5MayorValor, top5MenorValor)


# Definición de función: solicitarLetraBusqueda
def solicitarLetraBusqueda():
    """Solicita y valida una única letra alfabética al usuario."""
    letraValida = False
    letraIngresada = ""

    while not letraValida:
        letraInput = input("\nIngrese una letra para buscar en los nombres de países: ")
        letraLimpia = fs.limpiarEspaciosExtremos(letraInput)

        if len(letraLimpia) == 1 and fs.esLetraValida(letraLimpia):
            letraValida = True
            letraIngresada = letraLimpia
        else:
            print(" Error: Debe ingresar exactamente UNA letra alfabética válida.")

    return letraIngresada


# Definición de función: ejecutarOpcion2
def ejecutarOpcion2():
    """Opción 2: Lee países desde .toon, normaliza nombres, guarda y muestra métricas."""
    print("\n--- OPCIÓN 2: PROCESAR Y NORMALIZAR NOMBRES DE PAÍSES ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = []
    i = 0
    cantidad = len(listaPaises)

    while i < cantidad:
        p = listaPaises[i]
        nombreNormalizado = fs.normalizarNombre(p[0])
        paisNorm = (nombreNormalizado, p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        listaNormalizados.append(paisNorm)
        i = i + 1

    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")
    print("Nombres normalizados guardados correctamente en 'paises_datos.toon'.")

    letraIngresada = solicitarLetraBusqueda()

    promedioLen = calc.calcularLongitudPromedioNombres(listaNormalizados)
    nombreLargo, maxLen = calc.obtenerPaisNombreMasLargo(listaNormalizados)
    nombreCorto, minLen = calc.obtenerPaisNombreMasCorto(listaNormalizados)
    cantidadConLetra = calc.contarPaisesConLetra(listaNormalizados, letraIngresada)

    letraNormalizada = fs.quitarTildes(fs.aMayusculas(letraIngresada))

    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 2")
    print("==================================================")
    print("• Longitud promedio de los nombres (entero): " + str(promedioLen) + " caracteres")
    print("• País con nombre más largo: " + str(nombreLargo) + " (" + str(maxLen) + " caracteres)")
    print("• País con nombre más corto: " + str(nombreCorto) + " (" + str(minLen) + " caracteres)")
    print("• Países que contienen la letra '" + letraNormalizada + "': " + str(cantidadConLetra) + " países")
    print("==================================================")


# Definición de función: imprimirResultadosOpcion3
def imprimirResultadosOpcion3(pobTotal, pobPromedio, pobMediana, mega, grande, mediana, pequena, sumaCat, areaTotal, top10Mayor, top10Menor):
    """Imprime en consola los resultados procesados de la Opción 3."""
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 3")
    print("==================================================")

    promPobRed = calc.redondearManual(pobPromedio, 2)
    medianaPobRed = calc.redondearManual(pobMediana, 2)

    print("\n--- DATOS POBLACIONALES ---")
    print("• Población total mundial: " + str(pobTotal) + " habitantes")
    print("• Población promedio por país: " + str(promPobRed) + " habitantes")
    print("• Mediana de población: " + str(medianaPobRed) + " habitantes")

    print("\n• Clasificación de países por tamaño poblacional:")
    print("  - Megaciudad (> 10,000,000): " + str(mega) + " países")
    print("  - Ciudad grande (1,000,000 - 10,000,000): " + str(grande) + " países")
    print("  - Ciudad mediana (100,000 - 999,999): " + str(mediana) + " países")
    print("  - Ciudad pequeña (< 100,000): " + str(pequena) + " países")
    print("  - Total países clasificados: " + str(sumaCat))

    print("\n--- DATOS GEOGRÁFICOS Y DENSIDAD ---")
    print("• Área total mundial: " + str(areaTotal) + " km²")

    print("\n• Top 10 países con MAYOR densidad poblacional:")
    i = 0
    while i < len(top10Mayor):
        d = top10Mayor[i]
        densRed = calc.redondearManual(d[4], 2)
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(densRed) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("\n• Top 10 países con MENOR densidad poblacional:")
    i = 0
    while i < len(top10Menor):
        d = top10Menor[i]
        densRed = calc.redondearManual(d[4], 2)
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(densRed) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("==================================================")


# Definición de función: ejecutarOpcion3
def ejecutarOpcion3():
    """Opción 3: Procesar datos poblacionales y geográficos."""
    print("\n--- OPCIÓN 3: PROCESAR DATOS POBLACIONALES Y GEOGRÁFICOS ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = calc.normalizarDatosPaises(listaPaises)
    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")

    pobTotal = calc.calcularPoblacionTotal(listaNormalizados)
    pobPromedio = calc.calcularPoblacionPromedio(listaNormalizados)
    pobMediana = calc.calcularMedianaPoblacion(listaNormalizados)
    mega, grande, mediana, pequena = calc.clasificarPaisesPorPoblacion(listaNormalizados)
    sumaCat = mega + grande + mediana + pequena

    areaTotal = calc.calcularAreaTotal(listaNormalizados)
    listaDensidades = calc.calcularDensidadesPoblacionales(listaNormalizados)

    densidadesMayor = calc.ordenarPaisesPorDensidad(listaDensidades, descendente=True)
    top10Mayor = calc.obtenerPrimerosElementos(densidadesMayor, 10)

    densidadesMenor = calc.ordenarPaisesPorDensidad(listaDensidades, descendente=False)
    top10Menor = calc.obtenerPrimerosElementos(densidadesMenor, 10)

    imprimirResultadosOpcion3(pobTotal, pobPromedio, pobMediana, mega, grande, mediana, pequena, sumaCat, areaTotal, top10Mayor, top10Menor)


# Definición de función: solicitarNLetrasMoneda
def solicitarNLetrasMoneda():
    """Solicita y valida un entero N positivo mayor a 0 para buscar en nombres de monedas."""
    valido = False
    nLetras = 0

    while not valido:
        nInput = input("\nIngrese la cantidad de letras N a buscar en los nombres de monedas: ")
        if fs.esNumeroEnteroPositivo(nInput):
            nLetras = fs.convertirAEntero(nInput)
            valido = True
        else:
            print(" Error: Debe ingresar un número entero positivo mayor a 0.")

    return nLetras


# Definición de función: imprimirResultadosOpcion4
def imprimirResultadosOpcion4(monedasUnicas, nLetras, monedasConN, promedioTasa, monedaFuerte, monedaDebil, mayores1, iguales1, menores1, sumaConteos, monedasAsc, monedasDesc):
    """Imprime en consola los resultados procesados de la Opción 4."""
    totalMonedas = len(monedasUnicas)
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 4")
    print("==================================================")

    print("\n--- LISTA DE MONEDAS ÚNICAS (" + str(totalMonedas) + ") ---")
    i = 0
    while i < totalMonedas:
        m = monedasUnicas[i]
        formatoMoneda = fs.formatearMonedaCodigoNombre(m[0], m[1])
        print("  " + str(i + 1) + ". " + formatoMoneda + " (Tasa: " + str(m[2]) + ")")
        i = i + 1

    print("\n• Cantidad de monedas con exactamente " + str(nLetras) + " letras en su nombre: " + str(monedasConN) + " monedas")

    promTasaRed = calc.redondearManual(promedioTasa, 4)

    print("\n--- ESTADÍSTICAS Y OPERACIONES NUMÉRICAS ---")
    print("• Tasa de cambio promedio: " + str(promTasaRed))

    if monedaFuerte is not None:
        print("• Moneda más fuerte (Mayor tasa): " + str(monedaFuerte[1]) + " (" + str(monedaFuerte[0]) + ") con tasa " + str(monedaFuerte[2]))
    if monedaDebil is not None:
        print("• Moneda más débil (Menor tasa): " + str(monedaDebil[1]) + " (" + str(monedaDebil[0]) + ") con tasa " + str(monedaDebil[2]))

    print("\n• Clasificación según la tasa frente a 1 USD:")
    print("  - Monedas con tasa > 1 USD: " + str(mayores1))
    print("  - Monedas con tasa = 1 USD: " + str(iguales1))
    print("  - Monedas con tasa < 1 USD: " + str(menores1))
    print("  - Total monedas clasificadas: " + str(sumaConteos))

    print("\n--- MONEDAS ORDENADAS POR TASA (ASCENDENTE - De menor a mayor) ---")
    i = 0
    while i < totalMonedas:
        m = monedasAsc[i]
        print("  " + str(i + 1) + ". " + str(m[0]) + " - " + str(m[1]) + ": " + str(m[2]))
        i = i + 1

    print("\n--- MONEDAS ORDENADAS POR TASA (DESCENDENTE - De mayor a menor) ---")
    i = 0
    while i < totalMonedas:
        m = monedasDesc[i]
        print("  " + str(i + 1) + ". " + str(m[0]) + " - " + str(m[1]) + ": " + str(m[2]))
        i = i + 1

    print("==================================================")


# Definición de función: ejecutarOpcion4
def ejecutarOpcion4():
    """Opción 4: Procesar datos de monedas."""
    print("\n--- OPCIÓN 4: PROCESAR DATOS DE MONEDAS ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = calc.normalizarDatosPaises(listaPaises)
    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")

    monedasUnicas = calc.extraerMonedasUnicas(listaNormalizados)
    nLetras = solicitarNLetrasMoneda()
    monedasConN = calc.contarMonedasConNLetras(monedasUnicas, nLetras)

    promedioTasa = calc.calcularTasaPromedioMonedas(monedasUnicas)
    monedaFuerte = calc.obtenerMonedaMasFuerteOpcion4(monedasUnicas)
    monedaDebil = calc.obtenerMonedaMasDebilOpcion4(monedasUnicas)
    mayores1, iguales1, menores1 = calc.clasificarMonedasPorTasa(monedasUnicas)
    sumaConteos = mayores1 + iguales1 + menores1

    monedasAsc = calc.ordenarMonedasPorTasa(monedasUnicas, descendente=False)
    monedasDesc = calc.ordenarMonedasPorTasa(monedasUnicas, descendente=True)

    imprimirResultadosOpcion4(monedasUnicas, nLetras, monedasConN, promedioTasa, monedaFuerte, monedaDebil, mayores1, iguales1, menores1, sumaConteos, monedasAsc, monedasDesc)


# Definición de función: ejecutarOpcion5
def ejecutarOpcion5():
    """Opción 5: Generar reporte de países en TXT."""
    print("\n--- OPCIÓN 5: GENERAR REPORTE DE PAÍSES EN TXT ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = calc.normalizarDatosPaises(listaPaises)
    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")

    exito = reportes.generarReportePaisesTxt(listaNormalizados, "reporte_paises.txt")
    if exito:
        print(" Reporte TXT generado exitosamente en 'reporte_paises.txt'.")


# Definición de función: ejecutarOpcion6
def ejecutarOpcion6():
    """Opción 6: Generar reporte de monedas en HTML."""
    print("\n--- OPCIÓN 6: GENERAR REPORTE DE MONEDAS EN HTML ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = calc.normalizarDatosPaises(listaPaises)
    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")

    exito = reportes.generarReporteMonedasHtml(listaNormalizados, "reporte_monedas.html")
    if exito:
        print(" Reporte HTML de monedas generado exitosamente en 'reporte_monedas.html'.")


# Definición de función: ejecutarOpcion7
def ejecutarOpcion7():
    """Opción 7: Generar reporte de densidad poblacional en HTML."""
    print("\n--- OPCIÓN 7: GENERAR REPORTE DE DENSIDAD POBLACIONAL EN HTML ---")
    listaPaises = datos.leerDatosToon("paises_datos.toon")

    if listaPaises is None or len(listaPaises) == 0:
        return

    listaNormalizados = calc.normalizarDatosPaises(listaPaises)
    datos.guardarDatosToon(listaNormalizados, "paises_datos.toon")

    exito = reportes.generarReporteDensidadHtml(listaNormalizados, "reporte_densidad.html")
    if exito:
        print(" Reporte HTML de densidad generado exitosamente en 'reporte_densidad.html'.")


# Definición de función: main
def main():
    """Función principal para controlar el menú."""
    opcion = ""

    while opcion != "9":
        mostrarMenu()
        opcion = input("Seleccione una opción (1-9): ")
        opcion = fs.limpiarEspaciosExtremos(opcion)

        if opcion == "1":
            ejecutarOpcion1()
        elif opcion == "2":
            ejecutarOpcion2()
        elif opcion == "3":
            ejecutarOpcion3()
        elif opcion == "4":
            ejecutarOpcion4()
        elif opcion == "5":
            ejecutarOpcion5()
        elif opcion == "6":
            ejecutarOpcion6()
        elif opcion == "7":
            ejecutarOpcion7()
        elif opcion == "8":
            print("\n[Opción 8] - Submenú de bitácora (En desarrollo...)")
        elif opcion == "9":
            print("\n¡Gracias por utilizar el sistema!")
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 9.")


if __name__ == "__main__":
    main()
