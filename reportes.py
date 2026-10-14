#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-14
"""
Módulo de Generación de Reportes (TXT y HTML).
Genera reportes detallados en formato de texto plano (TXT) y páginas web (HTML)
utilizando listas, tuplas, concatenación de cadenas y funciones modulares.
"""

import datetime
import formateo_strings as fs
import calculos as calc
import formatos as fmt


# Definición de funciones de formateo delegadas a formatos.py
def formatear4Decimales(numero):
    """Delegado a formatos.formatear4Decimales."""
    return fmt.formatear4Decimales(numero)


def formatear2Decimales(numero):
    """Delegado a formatos.formatear2Decimales."""
    return fmt.formatear2Decimales(numero)


def formatearNumeroLimpio(numero):
    """Delegado a formatos.formatearNumeroLimpio."""
    return fmt.formatearNumeroLimpio(numero)


# Definición de función: generarGraficoAsciiVertical
def generarGraficoAsciiVertical(mega, grande, mediana, pequena):
    """Genera una representación gráfica vertical en arte ASCII de las 4 categorías poblacionales."""
    maxCat = mega
    if grande > maxCat:
        maxCat = grande
    if mediana > maxCat:
        maxCat = mediana
    if pequena > maxCat:
        maxCat = pequena

    maxVal = maxCat
    if maxVal < 10:
        maxVal = 10
    elif maxVal % 5 != 0:
        maxVal = maxVal + (5 - (maxVal % 5))

    lineas = []
    lineas.append("DISTRIBUCIÓN DE CATEGORÍAS POBLACIONALES (GRÁFICO ASCII VERTICAL)")
    lineas.append("")

    nivel = maxVal
    while nivel >= 1:
        if nivel % 5 == 0 or nivel == maxVal or nivel == 1:
            eje = (" " + str(nivel) + " |") if nivel < 10 else (str(nivel) + " |")
        else:
            eje = "   |"

        colMega = "  |  " if mega >= nivel else "     "
        colGran = "  |  " if grande >= nivel else "     "
        colMed  = "  |  " if mediana >= nivel else "     "
        colPeq  = "  |  " if pequena >= nivel else "     "

        lineas.append(eje + colMega + colGran + colMed + colPeq)
        nivel = nivel - 1

    lineas.append(" 0 +-----+-----+-----+-----+")
    lineas.append("     Mega  Gran   Med   Peq ")
    lineas.append("     (" + str(mega) + ")   (" + str(grande) + ")   (" + str(mediana) + ")   (" + str(pequena) + ")")

    resultado = ""
    i = 0
    while i < len(lineas):
        resultado = resultado + lineas[i] + "\n"
        i = i + 1

    return resultado


# Definición de función: construirBloquePaisTxt
def construirBloquePaisTxt(p):
    """Construye el bloque de texto de 4 líneas para un país individual."""
    nombre = p[0]
    capital = p[1]
    codigo = p[2]
    poblacion = p[3]
    area = p[4]
    monedaSinTildes = fs.quitarTildes(p[5])
    codigoMoneda = p[6]
    tasaUsdStr = fmt.formatear2Decimales(p[7])

    densidad = (poblacion / area) if area > 0 else 0.0

    if poblacion > 10000000:
        categoria = "Megaciudad"
    elif poblacion >= 1000000:
        categoria = "Ciudad grande"
    elif poblacion >= 100000:
        categoria = "Ciudad mediana"
    else:
        categoria = "Ciudad pequeña"

    densidadStr = fmt.formatear2Decimales(densidad)

    linea1 = "El país " + nombre + " tiene como capital " + capital + ", su código ISO es " + codigo + ",\n"
    linea2 = "tiene " + str(poblacion) + " habitantes, un área de " + str(area) + "km2, su moneda es " + monedaSinTildes + ",\n"
    linea3 = "código " + codigoMoneda + ", y hay " + tasaUsdStr + " por cada dólar.\n"
    linea4 = "Densidad poblacional: " + densidadStr + " hab/km2. Categoría: " + categoria + ".\n\n"

    return linea1 + linea2 + linea3 + linea4


# Definición de función: construirResumenPaisesTxt
def construirResumenPaisesTxt(cantidad, pobTotal, areaTotal, promPob, promArea):
    """Construye la sección final de resumen general para el reporte TXT."""
    promPobStr = fmt.formatearNumeroLimpio(promPob)
    promAreaStr = fmt.formatearNumeroLimpio(promArea)

    resumen = "==================================================\n"
    resumen = resumen + "RESUMEN GENERAL:\n"
    resumen = resumen + "Total de países: " + str(cantidad) + "\n"
    resumen = resumen + "Población total: " + str(pobTotal) + "\n"
    resumen = resumen + "Área total: " + str(areaTotal) + " km2\n"
    resumen = resumen + "Promedio de población: " + promPobStr + " habitantes\n"
    resumen = resumen + "Promedio de área: " + promAreaStr + " km2\n"
    resumen = resumen + "==================================================\n"
    return resumen


# Definición de función: generarReportePaisesTxt
def generarReportePaisesTxt(listaPaises, rutaSalida="reporte_paises.txt"):
    """Opción 5: Genera un archivo de texto con el reporte detallado de cada país y resumen."""
    try:
        archivo = open(rutaSalida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo '" + rutaSalida + "'.")
        return False

    cantidad = len(listaPaises)
    i = 0
    poblacionTotal = 0
    areaTotal = 0

    while i < cantidad:
        p = listaPaises[i]
        poblacionTotal = poblacionTotal + p[3]
        areaTotal = areaTotal + p[4]
        bloque = construirBloquePaisTxt(p)
        archivo.write(bloque)
        i = i + 1

    if cantidad > 0:
        promedioPoblacion = poblacionTotal / cantidad
        promedioArea = areaTotal / cantidad
    else:
        promedioPoblacion = 0.0
        promedioArea = 0.0

    resumenFinal = construirResumenPaisesTxt(cantidad, poblacionTotal, areaTotal, promedioPoblacion, promedioArea)
    archivo.write(resumenFinal)
    archivo.close()
    return True


# Definición de función: obtenerCodigosPorClasificacion
def obtenerCodigosPorClasificacion(listaMonedas, condicion):
    """Retorna una cadena con los códigos de monedas separados por coma según su condición."""
    codigos = ""
    i = 0
    cantidad = len(listaMonedas)
    primero = True

    while i < cantidad:
        m = listaMonedas[i]
        codigo = m[0]
        tasa = m[2]

        cumple = False
        if condicion == "fuerte" and tasa > 1.0:
            cumple = True
        elif condicion == "igual" and tasa == 1.0:
            cumple = True
        elif condicion == "debil" and tasa < 1.0:
            cumple = True

        if cumple:
            if primero:
                codigos = str(codigo)
                primero = False
            else:
                codigos = codigos + ", " + str(codigo)

        i = i + 1

    return codigos


# Definición de función: construirCardEstadisticasMonedas
def construirCardEstadisticasMonedas(totalMonedas, promedioTasa, monedaFuerte, monedaDebil, stCard, stP):
    """Construye el HTML para la tarjeta de estadísticas generales de monedas con etiquetas exactas."""
    html = "<div " + stCard + ">\n"
    html = html + "<h2>Estadísticas Generales</h2>\n"
    html = html + "<p " + stP + "><strong>Cantidad total de monedas analizadas:</strong> " + str(totalMonedas) + "</p>\n"
    html = html + "<p " + stP + "><strong>Tasa de cambio promedio:</strong> " + fmt.formatear4Decimales(promedioTasa) + "</p>\n"

    if monedaFuerte is not None:
        html = html + "<p " + stP + "><strong>Moneda más fuerte (mayor tasa):</strong> " + str(monedaFuerte[1]) + " (" + str(monedaFuerte[0]) + ") con tasa " + fmt.formatear4Decimales(monedaFuerte[2]) + "</p>\n"
    if monedaDebil is not None:
        html = html + "<p " + stP + "><strong>Moneda más débil (menor tasa):</strong> " + str(monedaDebil[1]) + " (" + str(monedaDebil[0]) + ") con tasa " + fmt.formatear4Decimales(monedaDebil[2]) + "</p>\n"

    html = html + "<p " + stP + ' style="color: #7f8c8d; font-size: 0.9em; font-style: italic;"><strong>Nota metodológica (Criterio económico):</strong> En economía financiera, una menor cotización nominal por dólar denota mayor apreciación unitaria (ej. GBP/CHF vs USD). Por instrucción de la consigna oficial, la clasificación principal se basa directamente en la magnitud nominal de la tasa.</p>\n'
    html = html + "</div>\n"
    return html


# Definición de función: construirTablaDetalladaMonedas
def construirTablaDetalladaMonedas(monedasUnicas, stTable, stThL, stThC, stFuerte, stDebil, stIgual):
    """Construye el HTML para la tabla detallada de monedas únicas."""
    totalMonedas = len(monedasUnicas)
    html = "<h2>Tabla Detallada de Monedas</h2>\n"
    html = html + "<table " + stTable + ">\n<thead>\n<tr>\n"
    html = html + "<th " + stThC + ">Código</th>\n"
    html = html + "<th " + stThL + ">Nombre Normalizado</th>\n"
    html = html + "<th " + stThC + ">Tasa de Cambio (USD)</th>\n"
    html = html + "<th " + stThC + ">Relación con USD</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    i = 0
    while i < totalMonedas:
        m = monedasUnicas[i]
        codigoM = m[0]
        nombreM = fs.quitarTildes(m[1])
        tasaM = m[2]
        tasaStr = fmt.formatear4Decimales(tasaM)

        bg = "background-color: #f9f9f9;" if (i % 2 == 1) else "background-color: #ffffff;"
        stTdL = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; ' + bg + '"'
        stTdC = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; ' + bg + '"'

        if tasaM > 1.0:
            relacion = "<span " + stFuerte + ">Fuerte</span>"
        elif tasaM == 1.0:
            relacion = "<span " + stIgual + ">Igual</span>"
        else:
            relacion = "<span " + stDebil + ">Débil</span>"

        html = html + "<tr>\n"
        html = html + "<td " + stTdC + ">" + str(codigoM) + "</td>\n"
        html = html + "<td " + stTdL + ">" + str(nombreM) + "</td>\n"
        html = html + "<td " + stTdC + ">" + tasaStr + "</td>\n"
        html = html + "<td " + stTdC + ">" + relacion + "</td>\n"
        html = html + "</tr>\n"
        i = i + 1

    html = html + "</tbody>\n</table>\n"
    return html


# Definición de función: construirTablaClasificacionMonedas
def construirTablaClasificacionMonedas(mayores1, iguales1, menores1, cFuertes, cIguales, cDebiles, stTable, stThC, stFuerte, stDebil, stIgual):
    """Construye el HTML para la tabla de clasificación de monedas."""
    html = "<h2>Tabla de Clasificación</h2>\n"
    html = html + "<table " + stTable + ">\n<thead>\n<tr>\n"
    html = html + "<th " + stThC + ">Clasificación</th>\n"
    html = html + "<th " + stThC + ">Cantidad de monedas</th>\n"
    html = html + "<th " + stThC + ">Códigos de las monedas</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    stTdC1 = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; background-color: #ffffff;"'
    stTdC2 = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; background-color: #f9f9f9;"'

    html = html + "<tr>\n"
    html = html + "<td " + stTdC1 + "><span " + stFuerte + ">Fuerte</span></td>\n"
    html = html + "<td " + stTdC1 + ">" + str(mayores1) + "</td>\n"
    html = html + "<td " + stTdC1 + ">" + cFuertes + "</td>\n"
    html = html + "</tr>\n"

    html = html + "<tr>\n"
    html = html + "<td " + stTdC2 + "><span " + stIgual + ">Igual</span></td>\n"
    html = html + "<td " + stTdC2 + ">" + str(iguales1) + "</td>\n"
    html = html + "<td " + stTdC2 + ">" + cIguales + "</td>\n"
    html = html + "</tr>\n"

    html = html + "<tr>\n"
    html = html + "<td " + stTdC1 + "><span " + stDebil + ">Débil</span></td>\n"
    html = html + "<td " + stTdC1 + ">" + str(menores1) + "</td>\n"
    html = html + "<td " + stTdC1 + ">" + cDebiles + "</td>\n"
    html = html + "</tr>\n"

    html = html + "</tbody>\n</table>\n"
    return html


# Definición de función: generarReporteMonedasHtml
def generarReporteMonedasHtml(datosMonedasOPaises, rutaSalida="reporte_monedas.html"):
    """Opción 6: Genera un reporte en formato HTML con estadísticas y tablas de monedas."""
    try:
        archivo = open(rutaSalida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo HTML '" + rutaSalida + "'.")
        return False

    if len(datosMonedasOPaises) > 0 and len(datosMonedasOPaises[0]) >= 8:
        monedasUnicas = calc.extraerMonedasUnicas(datosMonedasOPaises)
    else:
        monedasUnicas = datosMonedasOPaises

    totalMonedas = len(monedasUnicas)
    promedioTasa = calc.calcularTasaPromedioMonedas(monedasUnicas)
    monedaFuerte = calc.obtenerMonedaMasFuerteOpcion4(monedasUnicas)
    monedaDebil = calc.obtenerMonedaMasDebilOpcion4(monedasUnicas)

    mayores1, iguales1, menores1 = calc.clasificarMonedasPorTasa(monedasUnicas)
    codigosFuertes = obtenerCodigosPorClasificacion(monedasUnicas, "fuerte")
    codigosIguales = obtenerCodigosPorClasificacion(monedasUnicas, "igual")
    codigosDebiles = obtenerCodigosPorClasificacion(monedasUnicas, "debil")

    fechaHora = str(datetime.datetime.now())
    fechaCorta = fs.obtenerSubcadena(fechaHora, 0, 19)

    stBody = 'style="font-family: Arial, sans-serif; margin: 30px; background-color: #f4f7f6; color: #333;"'
    stH1 = 'style="color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px;"'
    stSub = 'style="text-align: center; color: #7f8c8d; font-size: 0.95em; margin-bottom: 25px;"'
    stCard = 'style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 25px;"'
    stP = 'style="font-size: 1.05em; margin: 8px 0;"'
    stTable = 'style="width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 30px;"'
    stThL = 'style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #3498db; color: white; font-size: 0.85em;"'
    stThC = 'style="padding: 12px 15px; text-align: center; border-bottom: 1px solid #ddd; background-color: #3498db; color: white; font-size: 0.85em;"'
    stFuerte = 'style="color: #27ae60; font-weight: bold;"'
    stDebil = 'style="color: #e74c3c; font-weight: bold;"'
    stIgual = 'style="color: #f39c12; font-weight: bold;"'

    html = "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
    html = html + "<title>Reporte de Análisis de Monedas</title>\n</head>\n<body " + stBody + ">\n"
    html = html + "<h1 " + stH1 + ">Reporte de Análisis de Monedas</h1>\n"
    html = html + "<p " + stSub + ">Generado automáticamente el " + fechaCorta + "</p>\n"

    html = html + construirCardEstadisticasMonedas(totalMonedas, promedioTasa, monedaFuerte, monedaDebil, stCard, stP)
    html = html + construirTablaDetalladaMonedas(monedasUnicas, stTable, stThL, stThC, stFuerte, stDebil, stIgual)
    html = html + construirTablaClasificacionMonedas(mayores1, iguales1, menores1, codigosFuertes, codigosIguales, codigosDebiles, stTable, stThC, stFuerte, stDebil, stIgual)
    html = html + "</body>\n</html>\n"

    archivo.write(html)
    archivo.close()
    return True


# Definición de función: calcularEstadisticasDensidad
def calcularEstadisticasDensidad(listaDensidades):
    """Calcula densidad promedio, máxima, mínima y países correspondientes."""
    total = len(listaDensidades)
    if total == 0:
        return 0.0, 0.0, 0.0, "", ""

    sumaDensidad = 0.0
    maxDensidad = 0.0
    minDensidad = 999999999.0
    paisMax = ""
    paisMin = ""

    i = 0
    while i < total:
        d = listaDensidades[i]
        valDens = d[4]
        sumaDensidad = sumaDensidad + valDens

        if valDens > maxDensidad:
            maxDensidad = valDens
            paisMax = d[0]

        if valDens < minDensidad:
            minDensidad = valDens
            paisMin = d[0]

        i = i + 1

    densidadPromedio = sumaDensidad / total
    return densidadPromedio, maxDensidad, minDensidad, paisMax, paisMin


# Definición de función: calcularPorcentajesCategorias
def calcularPorcentajesCategorias(totalPaises, mega, grande, mediana, pequena):
    """Calcula los porcentajes de cada categoría respecto al total de países."""
    if totalPaises == 0:
        return 0.0, 0.0, 0.0, 0.0
    pctM = (mega / totalPaises) * 100.0
    pctG = (grande / totalPaises) * 100.0
    pctMed = (mediana / totalPaises) * 100.0
    pctP = (pequena / totalPaises) * 100.0
    return pctM, pctG, pctMed, pctP


# Definición de función: construirCardEstadisticasDensidad
def construirCardEstadisticasDensidad(promDens, maxDens, minDens, pMax, pMin, mega, grande, mediana, pequena, pctM, pctG, pctMed, pctP, stCard):
    """Construye el HTML para la tarjeta de estadísticas de densidad mundial."""
    html = "<div " + stCard + ">\n"
    html = html + "<h2>Estadísticas de Densidad Mundial</h2>\n"
    html = html + "<p><strong>Densidad Promedio Global:</strong> " + fmt.formatear2Decimales(promDens) + " hab/km²</p>\n"
    html = html + "<p><strong>Densidad Máxima:</strong> " + pMax + " (" + fmt.formatear2Decimales(maxDens) + " hab/km²)</p>\n"
    html = html + "<p><strong>Densidad Mínima:</strong> " + pMin + " (" + fmt.formatear2Decimales(minDens) + " hab/km²)</p>\n"
    html = html + "<hr>\n"
    html = html + "<h3>Distribución por Categorías Poblacionales:</h3>\n"
    html = html + "<p>• Megaciudades (> 10M): " + str(mega) + " países (" + fmt.formatear2Decimales(pctM) + "%)</p>\n"
    html = html + "<p>• Ciudades Grandes (1M - 10M): " + str(grande) + " países (" + fmt.formatear2Decimales(pctG) + "%)</p>\n"
    html = html + "<p>• Ciudades Medianas (100k - 999k): " + str(mediana) + " países (" + fmt.formatear2Decimales(pctMed) + "%)</p>\n"
    html = html + "<p>• Ciudades Pequeñas (< 100k): " + str(pequena) + " países (" + fmt.formatear2Decimales(pctP) + "%)</p>\n"
    html = html + "</div>\n"
    return html


# Definición de función: construirTablaDensidad
def construirTablaDensidad(top10, titulo, stTable, stThL, stThC):
    """Construye el HTML para una tabla de top 10 densidad (mayor o menor)."""
    html = "<h2>" + titulo + "</h2>\n"
    html = html + "<table " + stTable + ">\n<thead>\n<tr>\n"
    html = html + "<th " + stThC + ">#</th>\n"
    html = html + "<th " + stThL + ">País</th>\n"
    html = html + "<th " + stThC + ">ISO</th>\n"
    html = html + "<th " + stThC + ">Población</th>\n"
    html = html + "<th " + stThC + ">Área (km²)</th>\n"
    html = html + "<th " + stThC + ">Densidad (hab/km²)</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    i = 0
    while i < len(top10):
        d = top10[i]
        bg = "background-color: #f9f9f9;" if (i % 2 == 1) else "background-color: #ffffff;"
        stTdL = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; ' + bg + '"'
        stTdC = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; ' + bg + '"'

        html = html + "<tr>\n"
        html = html + "<td " + stTdC + ">" + str(i + 1) + "</td>\n"
        html = html + "<td " + stTdL + ">" + str(d[0]) + "</td>\n"
        html = html + "<td " + stTdC + ">" + str(d[1]) + "</td>\n"
        html = html + "<td " + stTdC + ">" + str(d[2]) + "</td>\n"
        html = html + "<td " + stTdC + ">" + str(d[3]) + "</td>\n"
        html = html + "<td " + stTdC + ">" + fmt.formatear2Decimales(d[4]) + "</td>\n"
        html = html + "</tr>\n"
        i = i + 1

    html = html + "</tbody>\n</table>\n"
    return html


# Definición de función: generarReporteDensidadHtml
def generarReporteDensidadHtml(listaPaises, rutaSalida="reporte_densidad.html"):
    """Opción 7: Genera reporte HTML de densidad poblacional dividido modularmente."""
    try:
        archivo = open(rutaSalida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo HTML '" + rutaSalida + "'.")
        return False

    totalPaises = len(listaPaises)
    listaDensidades = calc.calcularDensidadesPoblacionales(listaPaises)
    densMayor = calc.ordenarPaisesPorDensidad(listaDensidades, descendente=True)
    top10Mayor = calc.obtenerPrimerosElementos(densMayor, 10)
    densMenor = calc.ordenarPaisesPorDensidad(listaDensidades, descendente=False)
    top10Menor = calc.obtenerPrimerosElementos(densMenor, 10)

    mega, grande, mediana, pequena = calc.clasificarPaisesPorPoblacion(listaPaises)
    pctM, pctG, pctMed, pctP = calcularPorcentajesCategorias(totalPaises, mega, grande, mediana, pequena)
    promDens, maxDens, minDens, pMax, pMin = calcularEstadisticasDensidad(listaDensidades)
    graficoAscii = generarGraficoAsciiVertical(mega, grande, mediana, pequena)

    fechaCorta = fs.obtenerSubcadena(str(datetime.datetime.now()), 0, 19)
    stBody = 'style="font-family: Arial, sans-serif; margin: 30px; background-color: #f4f7f6; color: #333;"'
    stH1 = 'style="color: #2c3e50; text-align: center; border-bottom: 3px solid #27ae60; padding-bottom: 10px;"'
    stSub = 'style="text-align: center; color: #7f8c8d; font-size: 0.95em; margin-bottom: 25px;"'
    stCard = 'style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 25px;"'
    stTable = 'style="width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 30px;"'
    stThL = 'style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #27ae60; color: white; font-size: 0.85em;"'
    stThC = 'style="padding: 12px 15px; text-align: center; border-bottom: 1px solid #ddd; background-color: #27ae60; color: white; font-size: 0.85em;"'
    stPre = 'style="background: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 8px; font-family: monospace; font-size: 0.95em; overflow-x: auto;"'

    html = "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
    html = html + "<title>Análisis de Densidad Poblacional Mundial</title>\n</head>\n<body " + stBody + ">\n"
    html = html + "<h1 " + stH1 + ">Análisis de Densidad Poblacional Mundial</h1>\n"
    html = html + "<p " + stSub + ">Generado automáticamente el " + fechaCorta + "</p>\n"
    html = html + construirCardEstadisticasDensidad(promDens, maxDens, minDens, pMax, pMin, mega, grande, mediana, pequena, pctM, pctG, pctMed, pctP, stCard)
    html = html + construirTablaDensidad(top10Mayor, "10 Países con MAYOR Densidad Poblacional", stTable, stThL, stThC)
    html = html + construirTablaDensidad(top10Menor, "10 Países con MENOR Densidad Poblacional", stTable, stThL, stThC)
    html = html + "<h2>Gráfico de Distribución de Categorías Poblacionales</h2>\n<pre " + stPre + ">\n" + graficoAscii + "</pre>\n"
    html = html + "</body>\n</html>\n"

    archivo.write(html)
    archivo.close()
    return True
