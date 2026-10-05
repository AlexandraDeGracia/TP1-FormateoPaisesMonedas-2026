"""
Módulo de Generación de Reportes (TXT y HTML).
Genera reportes detallados en formato de texto plano (TXT) y páginas web (HTML)
utilizando listas, tuplas, concatenación de cadenas y funciones modulares.
"""

import datetime
import datos
import formateo_strings as fs
import calculos as calc


def formatear_4_decimales(numero):
    """Formatea un número flotante con exactamente 4 decimales manualmente."""
    val = calc.redondear_manual(numero, 4)
    texto = str(val)
    partes = fs.separar_cadena(texto, ".")
    if len(partes) == 1:
        return partes[0] + ".0000"
    entero = partes[0]
    dec = partes[1]
    while len(dec) < 4:
        dec = dec + "0"
    if len(dec) > 4:
        dec = fs.obtener_subcadena(dec, 0, 4)
    return entero + "." + dec


def formatear_2_decimales(numero):
    """Formatea un número flotante con exactamente 2 decimales manualmente."""
    val = calc.redondear_manual(numero, 2)
    texto = str(val)
    partes = fs.separar_cadena(texto, ".")
    if len(partes) == 1:
        return partes[0] + ".00"
    entero = partes[0]
    dec = partes[1]
    while len(dec) < 2:
        dec = dec + "0"
    if len(dec) > 2:
        dec = fs.obtener_subcadena(dec, 0, 2)
    return entero + "." + dec


def formatear_numero_limpio(numero):
    """
    Formatea un número removiendo el '.0' si es un valor entero exacto
    o redondeando a 2 decimales si tiene parte decimal.
    Ejemplo: 176469664.0 -> "176469664", 2483990.32 -> "2483990.32"
    """
    if numero == int(numero):
        return str(int(numero))
    return formatear_2_decimales(numero)


def generar_grafico_ascii_vertical(mega, grande, mediana, pequena):
    """
    Genera un gráfico de barras ASCII vertical para las 4 categorías poblacionales.
    Utiliza barras hechas con '|' y etiquetas debajo dentro de una etiqueta <pre>.
    """
    max_val = 25
    lineas = []
    lineas.append("DISTRIBUCIÓN DE CATEGORÍAS POBLACIONALES (GRÁFICO ASCII VERTICAL)")
    lineas.append("")

    nivel = max_val
    while nivel >= 1:
        if nivel % 5 == 0 or nivel == max_val or nivel == 1:
            if nivel < 10:
                eje = " " + str(nivel) + " |"
            else:
                eje = str(nivel) + " |"
        else:
            eje = "   |"

        col_mega = "  |  " if mega >= nivel else "     "
        col_gran = "  |  " if grande >= nivel else "     "
        col_med  = "  |  " if mediana >= nivel else "     "
        col_peq  = "  |  " if pequena >= nivel else "     "

        lineas.append(eje + col_mega + col_gran + col_med + col_peq)
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


def _construir_bloque_pais_txt(p):
    """Construye el bloque de texto de 4 líneas para un país individual."""
    nombre_norm = fs.normalizar_nombre(p[0])
    capital_norm = fs.normalizar_nombre(p[1])
    codigo = p[2]
    poblacion = p[3]
    area = p[4]
    moneda_sin_tildes = fs.quitar_tildes(p[5])
    codigo_moneda = p[6]
    tasa_usd_str = formatear_2_decimales(p[7])

    if area > 0:
        densidad = poblacion / area
    else:
        densidad = 0.0

    if poblacion > 10000000:
        categoria = "Megaciudad"
    elif poblacion >= 1000000:
        categoria = "Ciudad grande"
    elif poblacion >= 100000:
        categoria = "Ciudad mediana"
    else:
        categoria = "Ciudad pequeña"

    densidad_str = formatear_2_decimales(densidad)

    linea1 = "El país " + nombre_norm + " tiene como capital " + capital_norm + ", su código ISO es " + codigo + ",\n"
    linea2 = "tiene " + str(poblacion) + " habitantes, un área de " + str(area) + "km2, su moneda es " + moneda_sin_tildes + ",\n"
    linea3 = "código " + codigo_moneda + ", y hay " + tasa_usd_str + " por cada dólar.\n"
    linea4 = "Densidad poblacional: " + densidad_str + " hab/km2. Categoría: " + categoria + ".\n\n"

    return linea1 + linea2 + linea3 + linea4


def _construir_resumen_paises_txt(cantidad, pob_total, area_total, prom_pob, prom_area):
    """Construye la sección final de resumen general para el reporte TXT."""
    prom_pob_str = formatear_numero_limpio(prom_pob)
    prom_area_str = formatear_numero_limpio(prom_area)

    resumen = "==================================================\n"
    resumen = resumen + "RESUMEN GENERAL:\n"
    resumen = resumen + "Total de países: " + str(cantidad) + "\n"
    resumen = resumen + "Población total: " + str(pob_total) + "\n"
    resumen = resumen + "Área total: " + str(area_total) + " km2\n"
    resumen = resumen + "Promedio de población: " + prom_pob_str + " habitantes\n"
    resumen = resumen + "Promedio de área: " + prom_area_str + " km2\n"
    resumen = resumen + "==================================================\n"
    return resumen


def generar_reporte_paises_txt(lista_paises, ruta_salida="reporte_paises.txt"):
    """
    Opción 5: Genera un archivo de texto con el reporte detallado de cada país
    y una sección de resumen general al final.
    """
    try:
        archivo = open(ruta_salida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo '" + ruta_salida + "'.")
        return False

    cantidad = len(lista_paises)
    i = 0
    poblacion_total = 0
    area_total = 0

    while i < cantidad:
        p = lista_paises[i]
        poblacion_total = poblacion_total + p[3]
        area_total = area_total + p[4]
        bloque = _construir_bloque_pais_txt(p)
        archivo.write(bloque)
        i = i + 1

    if cantidad > 0:
        promedio_poblacion = poblacion_total / cantidad
        promedio_area = area_total / cantidad
    else:
        promedio_poblacion = 0.0
        promedio_area = 0.0

    resumen_final = _construir_resumen_paises_txt(cantidad, poblacion_total, area_total, promedio_poblacion, promedio_area)
    archivo.write(resumen_final)

    archivo.close()
    return True


def obtener_codigos_por_clasificacion(lista_monedas, condicion):
    """
    Retorna una cadena con los códigos de las monedas separados por coma
    que cumplen la condición ('fuerte', 'igual', 'debil').
    """
    codigos = ""
    i = 0
    cantidad = len(lista_monedas)
    primero = True

    while i < cantidad:
        m = lista_monedas[i]
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


def _construir_card_estadisticas_monedas(total_monedas, promedio_tasa, moneda_fuerte, moneda_debil, st_card, st_p):
    """Construye el HTML para la tarjeta de estadísticas generales de monedas."""
    html = "<div " + st_card + ">\n"
    html = html + "<h2>Estadísticas Generales</h2>\n"
    html = html + "<p " + st_p + "><strong>Cantidad total de monedas analizadas:</strong> " + str(total_monedas) + "</p>\n"
    html = html + "<p " + st_p + "><strong>Tasa de cambio promedio:</strong> " + formatear_4_decimales(promedio_tasa) + "</p>\n"

    if moneda_fuerte is not None:
        html = html + "<p " + st_p + "><strong>Moneda más fuerte (Mayor tasa según criterio PDF):</strong> " + str(moneda_fuerte[1]) + " (" + str(moneda_fuerte[0]) + ") con tasa " + formatear_4_decimales(moneda_fuerte[2]) + "</p>\n"
    if moneda_debil is not None:
        html = html + "<p " + st_p + "><strong>Moneda más débil (Menor tasa según criterio PDF):</strong> " + str(moneda_debil[1]) + " (" + str(moneda_debil[0]) + ") con tasa " + formatear_4_decimales(moneda_debil[2]) + "</p>\n"

    html = html + "</div>\n"
    return html


def _construir_tabla_detallada_monedas(monedas_unicas, st_table, st_th_l, st_th_c, st_fuerte, st_debil, st_igual):
    """Construye el HTML para la tabla detallada de 21 monedas."""
    total_monedas = len(monedas_unicas)
    html = "<h2>Tabla Detallada de Monedas</h2>\n"
    html = html + "<table " + st_table + ">\n<thead>\n<tr>\n"
    html = html + "<th " + st_th_c + ">Código</th>\n"
    html = html + "<th " + st_th_l + ">Nombre Normalizado</th>\n"
    html = html + "<th " + st_th_c + ">Tasa de Cambio (USD)</th>\n"
    html = html + "<th " + st_th_c + ">Relación con USD</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    i = 0
    while i < total_monedas:
        m = monedas_unicas[i]
        codigo_m = m[0]
        nombre_m = fs.quitar_tildes(m[1])
        tasa_m = m[2]
        tasa_str = formatear_4_decimales(tasa_m)

        bg = "background-color: #f9f9f9;" if (i % 2 == 1) else "background-color: #ffffff;"
        st_td_l = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; ' + bg + '"'
        st_td_c = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; ' + bg + '"'

        if tasa_m > 1.0:
            relacion = "<span " + st_fuerte + ">Fuerte</span>"
        elif tasa_m == 1.0:
            relacion = "<span " + st_igual + ">Igual</span>"
        else:
            relacion = "<span " + st_debil + ">Débil</span>"

        html = html + "<tr>\n"
        html = html + "<td " + st_td_c + ">" + str(codigo_m) + "</td>\n"
        html = html + "<td " + st_td_l + ">" + str(nombre_m) + "</td>\n"
        html = html + "<td " + st_td_c + ">" + tasa_str + "</td>\n"
        html = html + "<td " + st_td_c + ">" + relacion + "</td>\n"
        html = html + "</tr>\n"

        i = i + 1

    html = html + "</tbody>\n</table>\n"
    return html


def _construir_tabla_clasificacion_monedas(mayores_1, iguales_1, menores_1, c_fuertes, c_iguales, c_debiles, st_table, st_th_c, st_fuerte, st_debil, st_igual):
    """Construye el HTML para la tabla de clasificación de monedas."""
    html = "h2>Tabla de Clasificación</h2>\n"
    # Notice: '<h2>Tabla de Clasificación</h2>\n'
    html = "<h2>Tabla de Clasificación</h2>\n"
    html = html + "<table " + st_table + ">\n<thead>\n<tr>\n"
    html = html + "<th " + st_th_c + ">Clasificación</th>\n"
    html = html + "<th " + st_th_c + ">Cantidad de monedas</th>\n"
    html = html + "<th " + st_th_c + ">Códigos de las monedas</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    st_td_c1 = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; background-color: #ffffff;"'
    st_td_c2 = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; background-color: #f9f9f9;"'

    html = html + "<tr>\n"
    html = html + "<td " + st_td_c1 + "><span " + st_fuerte + ">Fuerte</span></td>\n"
    html = html + "<td " + st_td_c1 + ">" + str(mayores_1) + "</td>\n"
    html = html + "<td " + st_td_c1 + ">" + c_fuertes + "</td>\n"
    html = html + "</tr>\n"

    html = html + "<tr>\n"
    html = html + "<td " + st_td_c2 + "><span " + st_igual + ">Igual</span></td>\n"
    html = html + "<td " + st_td_c2 + ">" + str(iguales_1) + "</td>\n"
    html = html + "<td " + st_td_c2 + ">" + c_iguales + "</td>\n"
    html = html + "</tr>\n"

    html = html + "<tr>\n"
    html = html + "<td " + st_td_c1 + "><span " + st_debil + ">Débil</span></td>\n"
    html = html + "<td " + st_td_c1 + ">" + str(menores_1) + "</td>\n"
    html = html + "<td " + st_td_c1 + ">" + c_debiles + "</td>\n"
    html = html + "</tr>\n"

    html = html + "</tbody>\n</table>\n"
    return html


def generar_reporte_monedas_html(lista_paises, ruta_salida="reporte_monedas.html"):
    """
    Opción 6: Genera un reporte en formato HTML con las estadísticas,
    la tabla detallada de monedas únicas (21) y la tabla de clasificación.
    """
    try:
        archivo = open(ruta_salida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo HTML '" + ruta_salida + "'.")
        return False

    monedas_unicas = calc.extraer_monedas_unicas(lista_paises)
    total_monedas = len(monedas_unicas)

    promedio_tasa = calc.calcular_tasa_promedio_monedas(monedas_unicas)
    moneda_fuerte = calc.obtener_moneda_mas_fuerte_opcion4(monedas_unicas)
    moneda_debil = calc.obtener_moneda_mas_debil_opcion4(monedas_unicas)

    mayores_1, iguales_1, menores_1 = calc.clasificar_monedas_por_tasa(monedas_unicas)

    codigos_fuertes = obtener_codigos_por_clasificacion(monedas_unicas, "fuerte")
    codigos_iguales = obtener_codigos_por_clasificacion(monedas_unicas, "igual")
    codigos_debiles = obtener_codigos_por_clasificacion(monedas_unicas, "debil")

    fecha_hora = str(datetime.datetime.now())
    fecha_corta = fs.obtener_subcadena(fecha_hora, 0, 19)

    st_body = 'style="font-family: Arial, sans-serif; margin: 30px; background-color: #f4f7f6; color: #333;"'
    st_h1 = 'style="color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px;"'
    st_sub = 'style="text-align: center; color: #7f8c8d; font-size: 0.95em; margin-bottom: 25px;"'
    st_card = 'style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 25px;"'
    st_p = 'style="font-size: 1.05em; margin: 8px 0;"'
    st_table = 'style="width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 30px;"'
    st_th_l = 'style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #3498db; color: white; font-size: 0.85em;"'
    st_th_c = 'style="padding: 12px 15px; text-align: center; border-bottom: 1px solid #ddd; background-color: #3498db; color: white; font-size: 0.85em;"'

    st_fuerte = 'style="color: #27ae60; font-weight: bold;"'
    st_debil = 'style="color: #e74c3c; font-weight: bold;"'
    st_igual = 'style="color: #f39c12; font-weight: bold;"'

    html = "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n"
    html = html + "<meta charset=\"utf-8\">\n"
    html = html + "<title>Reporte de Análisis de Monedas</title>\n"
    html = html + "</head>\n<body " + st_body + ">\n"

    html = html + "<h1 " + st_h1 + ">Reporte de Análisis de Monedas</h1>\n"
    html = html + "<p " + st_sub + ">Generado automáticamente el " + fecha_corta + "</p>\n"

    html = html + _construir_card_estadisticas_monedas(total_monedas, promedio_tasa, moneda_fuerte, moneda_debil, st_card, st_p)
    html = html + _construir_tabla_detallada_monedas(monedas_unicas, st_table, st_th_l, st_th_c, st_fuerte, st_debil, st_igual)
    html = html + _construir_tabla_clasificacion_monedas(mayores_1, iguales_1, menores_1, codigos_fuertes, codigos_iguales, codigos_debiles, st_table, st_th_c, st_fuerte, st_debil, st_igual)

    html = html + "</body>\n</html>\n"

    archivo.write(html)
    archivo.close()
    return True


def _construir_card_estadisticas_densidad(prom_dens, max_dens, min_dens, p_max, p_min, mega, grande, mediana, pequena, pct_m, pct_g, pct_med, pct_p, st_card):
    """Construye el HTML para la tarjeta de estadísticas de densidad mundial."""
    html = "<div " + st_card + ">\n"
    html = html + "<h2>Estadísticas de Densidad Mundial</h2>\n"
    html = html + "<p><strong>Densidad Promedio Global:</strong> " + formatear_2_decimales(prom_dens) + " hab/km²</p>\n"
    html = html + "<p><strong>Densidad Máxima:</strong> " + p_max + " (" + formatear_2_decimales(max_dens) + " hab/km²)</p>\n"
    html = html + "<p><strong>Densidad Mínima:</strong> " + p_min + " (" + formatear_2_decimales(min_dens) + " hab/km²)</p>\n"
    html = html + "<hr>\n"
    html = html + "<h3>Distribución por Categorías Poblacionales:</h3>\n"
    html = html + "<p>• Megaciudades (> 10M): " + str(mega) + " países (" + formatear_2_decimales(pct_m) + "%)</p>\n"
    html = html + "<p>• Ciudades Grandes (1M - 10M): " + str(grande) + " países (" + formatear_2_decimales(pct_g) + "%)</p>\n"
    html = html + "<p>• Ciudades Medianas (100k - 999k): " + str(mediana) + " países (" + formatear_2_decimales(pct_med) + "%)</p>\n"
    html = html + "<p>• Ciudades Pequeñas (< 100k): " + str(pequena) + " países (" + formatear_2_decimales(pct_p) + "%)</p>\n"
    html = html + "</div>\n"
    return html


def _construir_tabla_densidad(top_10, titulo, st_table, st_th_l, st_th_c):
    """Construye el HTML para una tabla de top 10 densidad (mayor o menor)."""
    html = "<h2>" + titulo + "</h2>\n"
    html = html + "<table " + st_table + ">\n<thead>\n<tr>\n"
    html = html + "<th " + st_th_c + ">#</th>\n"
    html = html + "<th " + st_th_l + ">País</th>\n"
    html = html + "<th " + st_th_c + ">ISO</th>\n"
    html = html + "<th " + st_th_c + ">Población</th>\n"
    html = html + "<th " + st_th_c + ">Área (km²)</th>\n"
    html = html + "<th " + st_th_c + ">Densidad (hab/km²)</th>\n"
    html = html + "</tr>\n</thead>\n<tbody>\n"

    i = 0
    while i < len(top_10):
        d = top_10[i]
        bg = "background-color: #f9f9f9;" if (i % 2 == 1) else "background-color: #ffffff;"
        st_td_l = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; ' + bg + '"'
        st_td_c = 'style="padding: 12px 15px; border-bottom: 1px solid #ddd; text-align: center; ' + bg + '"'

        html = html + "<tr>\n"
        html = html + "<td " + st_td_c + ">" + str(i + 1) + "</td>\n"
        html = html + "<td " + st_td_l + ">" + str(d[0]) + "</td>\n"
        html = html + "<td " + st_td_c + ">" + str(d[1]) + "</td>\n"
        html = html + "<td " + st_td_c + ">" + str(d[2]) + "</td>\n"
        html = html + "<td " + st_td_c + ">" + str(d[3]) + "</td>\n"
        html = html + "<td " + st_td_c + ">" + formatear_2_decimales(d[4]) + "</td>\n"
        html = html + "</tr>\n"
        i = i + 1

    html = html + "</tbody>\n</table>\n"
    return html


def generar_reporte_densidad_html(lista_paises, ruta_salida="reporte_densidad.html"):
    """
    Opción 7: Genera un reporte HTML sobre el análisis de densidad poblacional mundial,
    incluyendo tablas de mayor/menor densidad y un gráfico de barras ASCII vertical en <pre>.
    """
    try:
        archivo = open(ruta_salida, "w", encoding="utf-8")
    except OSError:
        print("\n Error: No se pudo crear el archivo HTML '" + ruta_salida + "'.")
        return False

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    total_paises = len(lista_normalizados)

    lista_densidades = calc.calcular_densidades_poblacionales(lista_normalizados)
    densidades_mayor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=True)
    top_10_mayor = calc.obtener_primeros_elementos(densidades_mayor, 10)

    densidades_menor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=False)
    top_10_menor = calc.obtener_primeros_elementos(densidades_menor, 10)

    mega, grande, mediana, pequena = calc.clasificar_paises_por_poblacion(lista_normalizados)

    if total_paises > 0:
        pct_mega = (mega / total_paises) * 100.0
        pct_grande = (grande / total_paises) * 100.0
        pct_mediana = (mediana / total_paises) * 100.0
        pct_pequena = (pequena / total_paises) * 100.0
    else:
        pct_mega = pct_grande = pct_mediana = pct_pequena = 0.0

    suma_densidad = 0.0
    max_densidad = 0.0
    min_densidad = 999999999.0
    pais_max_dens = ""
    pais_min_dens = ""

    i = 0
    while i < len(lista_densidades):
        d = lista_densidades[i]
        val_dens = d[4]
        suma_densidad = suma_densidad + val_dens

        if val_dens > max_densidad:
            max_densidad = val_dens
            pais_max_dens = d[0]

        if val_dens < min_densidad:
            min_densidad = val_dens
            pais_min_dens = d[0]

        i = i + 1

    if total_paises > 0:
        densidad_promedio = suma_densidad / total_paises
    else:
        densidad_promedio = 0.0

    grafico_ascii = generar_grafico_ascii_vertical(mega, grande, mediana, pequena)

    fecha_hora = str(datetime.datetime.now())
    fecha_corta = fs.obtener_subcadena(fecha_hora, 0, 19)

    st_body = 'style="font-family: Arial, sans-serif; margin: 30px; background-color: #f4f7f6; color: #333;"'
    st_h1 = 'style="color: #2c3e50; text-align: center; border-bottom: 3px solid #27ae60; padding-bottom: 10px;"'
    st_sub = 'style="text-align: center; color: #7f8c8d; font-size: 0.95em; margin-bottom: 25px;"'
    st_card = 'style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 25px;"'
    st_table = 'style="width: 100%; border-collapse: collapse; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 30px;"'
    st_th_l = 'style="padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: #27ae60; color: white; font-size: 0.85em;"'
    st_th_c = 'style="padding: 12px 15px; text-align: center; border-bottom: 1px solid #ddd; background-color: #27ae60; color: white; font-size: 0.85em;"'
    st_pre = 'style="background: #2c3e50; color: #ecf0f1; padding: 20px; border-radius: 8px; font-family: monospace; font-size: 0.95em; overflow-x: auto;"'

    html = "<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n"
    html = html + "<meta charset=\"utf-8\">\n"
    html = html + "<title>Análisis de Densidad Poblacional Mundial</title>\n"
    html = html + "</head>\n<body " + st_body + ">\n"

    html = html + "<h1 " + st_h1 + ">Análisis de Densidad Poblacional Mundial</h1>\n"
    html = html + "<p " + st_sub + ">Generado automáticamente el " + fecha_corta + "</p>\n"

    html = html + _construir_card_estadisticas_densidad(densidad_promedio, max_densidad, min_densidad, pais_max_dens, pais_min_dens, mega, grande, mediana, pequena, pct_mega, pct_grande, pct_mediana, pct_pequena, st_card)
    html = html + _construir_tabla_densidad(top_10_mayor, "10 Países con MAYOR Densidad Poblacional", st_table, st_th_l, st_th_c)
    html = html + _construir_tabla_densidad(top_10_menor, "10 Países con MENOR Densidad Poblacional", st_table, st_th_l, st_th_c)

    html = html + "<h2>Gráfico de Distribución de Categorías Poblacionales</h2>\n"
    html = html + "<pre " + st_pre + ">\n" + grafico_ascii + "</pre>\n"

    html = html + "</body>\n</html>\n"

    archivo.write(html)
    archivo.close()
    return True
