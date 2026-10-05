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


def mostrar_menu():
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


def _solicitar_ruta_csv():
    """Solicita al usuario la ruta del archivo CSV y retorna la ruta limpia."""
    ruta_input = input("Ingrese el nombre/ruta del archivo CSV (Presione Enter para 'paises.csv'): ")
    ruta_limpia = fs.limpiar_espacios_extremos(ruta_input)
    if len(ruta_limpia) == 0:
        return "paises.csv"
    return ruta_limpia


def _imprimir_resultados_opcion_1(total_paises, top_5_poblacion, top_5_area, fecha_hoy, total_monedas, top_5_mayor_valor, top_5_menor_valor):
    """Imprime en consola los resultados procesados de la Opción 1."""
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 1")
    print("==================================================")

    print("\n--- PAÍSES ---")
    print("• Cantidad de países cargados: " + str(total_paises))

    print("\n• 5 Países con MAYOR población:")
    i = 0
    while i < len(top_5_poblacion):
        p = top_5_poblacion[i]
        print("  " + str(i + 1) + ". " + str(p[0]) + " (" + str(p[2]) + ") - Población: " + str(p[3]))
        i = i + 1

    print("\n• 5 Países con MENOR área (km²):")
    i = 0
    while i < len(top_5_area):
        p = top_5_area[i]
        print("  " + str(i + 1) + ". " + str(p[0]) + " (" + str(p[2]) + ") - Área: " + str(p[4]) + " km²")
        i = i + 1

    print("\n--- MONEDAS ---")
    print("• Fecha de la tasa de cambio: " + fecha_hoy)
    print("• Cantidad de monedas cargadas: " + str(total_monedas))

    print("\n• Top 5 monedas con MAYOR valor frente al USD (Tasa más baja):")
    i = 0
    while i < len(top_5_mayor_valor):
        m = top_5_mayor_valor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n• Top 5 monedas con MENOR valor frente al USD (Tasa más alta):")
    i = 0
    while i < len(top_5_menor_valor):
        m = top_5_menor_valor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n==================================================")


def ejecutar_opcion_1():
    """
    Opción 1: Carga los datos del archivo CSV, los guarda en un archivo .toon
    y muestra las estadísticas solicitadas en consola.
    """
    print("\n--- OPCIÓN 1: DESCARGAR DATOS DE PAÍSES (CSV) ---")
    ruta_csv = _solicitar_ruta_csv()

    print("Cargando datos desde: " + ruta_csv + " ...")
    lista_paises = datos.leer_csv_paises(ruta_csv)

    if lista_paises is None or len(lista_paises) == 0:
        print("No se pudieron cargar los datos. Regresando al menú principal.")
        return

    archivo_toon = "paises_datos.toon"
    exito_toon = datos.guardar_datos_toon(lista_paises, archivo_toon)
    if exito_toon:
        print("Datos crudos guardados exitosamente en '" + archivo_toon + "'.")

    total_paises = len(lista_paises)
    paises_por_pob = calc.ordenar_paises_por_poblacion_descendente(lista_paises)
    top_5_poblacion = calc.obtener_primeros_elementos(paises_por_pob, 5)

    paises_por_area = calc.ordenar_paises_por_area_ascendente(lista_paises)
    top_5_area = calc.obtener_primeros_elementos(paises_por_area, 5)

    fecha_hoy = str(datetime.date.today())

    monedas_unicas = calc.extraer_monedas_unicas(lista_paises)
    total_monedas = len(monedas_unicas)

    monedas_mayor_valor = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=False)
    top_5_mayor_valor = calc.obtener_primeros_elementos(monedas_mayor_valor, 5)

    monedas_menor_valor = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=True)
    top_5_menor_valor = calc.obtener_primeros_elementos(monedas_menor_valor, 5)

    _imprimir_resultados_opcion_1(total_paises, top_5_poblacion, top_5_area, fecha_hoy, total_monedas, top_5_mayor_valor, top_5_menor_valor)


def _solicitar_letra_busqueda():
    """Solicita y valida una única letra alfabética al usuario."""
    letra_valida = False
    letra_ingresada = ""

    while not letra_valida:
        letra_input = input("\nIngrese una letra para buscar en los nombres de países: ")
        letra_limpia = fs.limpiar_espacios_extremos(letra_input)

        if len(letra_limpia) == 1 and fs.es_letra_valida(letra_limpia):
            letra_valida = True
            letra_ingresada = letra_limpia
        else:
            print(" Error: Debe ingresar exactamente UNA letra alfabética válida.")

    return letra_ingresada


def ejecutar_opcion_2():
    """
    Opción 2: Lee los países desde paises_datos.toon, aplica las 8 reglas de normalización
    a los nombres de países, guarda los nombres normalizados de vuelta en paises_datos.toon
    y muestra las métricas requeridas por consola.
    """
    print("\n--- OPCIÓN 2: PROCESAR Y NORMALIZAR NOMBRES DE PAÍSES ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = []
    i = 0
    cantidad = len(lista_paises)

    while i < cantidad:
        p = lista_paises[i]
        nombre_normalizado = fs.normalizar_nombre(p[0])
        pais_norm = (nombre_normalizado, p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        lista_normalizados.append(pais_norm)
        i = i + 1

    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")
    print("Nombres normalizados guardados correctamente en 'paises_datos.toon'.")

    letra_ingresada = _solicitar_letra_busqueda()

    promedio_len = calc.calcular_longitud_promedio_nombres(lista_normalizados)
    nombre_largo, max_len = calc.obtener_pais_nombre_mas_largo(lista_normalizados)
    nombre_corto, min_len = calc.obtener_pais_nombre_mas_corto(lista_normalizados)
    cantidad_con_letra = calc.contar_paises_con_letra(lista_normalizados, letra_ingresada)

    letra_normalizada = fs.quitar_tildes(fs.a_mayusculas(letra_ingresada))

    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 2")
    print("==================================================")
    print("• Longitud promedio de los nombres (entero): " + str(promedio_len) + " caracteres")
    print("• País con nombre más largo: " + str(nombre_largo) + " (" + str(max_len) + " caracteres)")
    print("• País con nombre más corto: " + str(nombre_corto) + " (" + str(min_len) + " caracteres)")
    print("• Países que contienen la letra '" + letra_normalizada + "': " + str(cantidad_con_letra) + " países")
    print("==================================================")


def _imprimir_resultados_opcion_3(pob_total, pob_promedio, pob_mediana, mega, grande, mediana, pequena, suma_cat, area_total, top_10_mayor, top_10_menor):
    """Imprime en consola los resultados procesados de la Opción 3."""
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 3")
    print("==================================================")

    prom_pob_red = calc.redondear_manual(pob_promedio, 2)
    mediana_pob_red = calc.redondear_manual(pob_mediana, 2)

    print("\n--- DATOS POBLACIONALES ---")
    print("• Población total mundial: " + str(pob_total) + " habitantes")
    print("• Población promedio por país: " + str(prom_pob_red) + " habitantes")
    print("• Mediana de población: " + str(mediana_pob_red) + " habitantes")

    print("\n• Clasificación de países por tamaño poblacional:")
    print("  - Megaciudad (> 10,000,000): " + str(mega) + " países")
    print("  - Ciudad grande (1,000,000 - 10,000,000): " + str(grande) + " países")
    print("  - Ciudad mediana (100,000 - 999,999): " + str(mediana) + " países")
    print("  - Ciudad pequeña (< 100,000): " + str(pequena) + " países")
    print("  - Total países clasificados: " + str(suma_cat))

    print("\n--- DATOS GEOGRÁFICOS Y DENSIDAD ---")
    print("• Área total mundial: " + str(area_total) + " km²")

    print("\n• Top 10 países con MAYOR densidad poblacional:")
    i = 0
    while i < len(top_10_mayor):
        d = top_10_mayor[i]
        dens_red = calc.redondear_manual(d[4], 2)
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(dens_red) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("\n• Top 10 países con MENOR densidad poblacional:")
    i = 0
    while i < len(top_10_menor):
        d = top_10_menor[i]
        dens_red = calc.redondear_manual(d[4], 2)
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(dens_red) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("==================================================")


def ejecutar_opcion_3():
    """
    Opción 3: Procesar datos poblacionales y geográficos.
    Carga los países desde paises_datos.toon, normaliza datos, calcula y muestra resultados.
    """
    print("\n--- OPCIÓN 3: PROCESAR DATOS POBLACIONALES Y GEOGRÁFICOS ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    pob_total = calc.calcular_poblacion_total(lista_normalizados)
    pob_promedio = calc.calcular_poblacion_promedio(lista_normalizados)
    pob_mediana = calc.calcular_mediana_poblacion(lista_normalizados)
    mega, grande, mediana, pequena = calc.clasificar_paises_por_poblacion(lista_normalizados)
    suma_cat = mega + grande + mediana + pequena

    area_total = calc.calcular_area_total(lista_normalizados)
    lista_densidades = calc.calcular_densidades_poblacionales(lista_normalizados)

    densidades_mayor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=True)
    top_10_mayor = calc.obtener_primeros_elementos(densidades_mayor, 10)

    densidades_menor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=False)
    top_10_menor = calc.obtener_primeros_elementos(densidades_menor, 10)

    _imprimir_resultados_opcion_3(pob_total, pob_promedio, pob_mediana, mega, grande, mediana, pequena, suma_cat, area_total, top_10_mayor, top_10_menor)


def _solicitar_n_letras_moneda():
    """Solicita y valida un entero N positivo mayor a 0 para buscar en nombres de monedas."""
    valido = False
    n_letras = 0

    while not valido:
        n_input = input("\nIngrese la cantidad de letras N a buscar en los nombres de monedas: ")
        if fs.es_numero_entero_positivo(n_input):
            n_letras = fs.convertir_a_entero(n_input)
            valido = True
        else:
            print(" Error: Debe ingresar un número entero positivo mayor a 0.")

    return n_letras


def _imprimir_resultados_opcion_4(monedas_unicas, n_letras, monedas_con_n, promedio_tasa, moneda_fuerte, moneda_debil, mayores_1, iguales_1, menores_1, suma_conteos, monedas_asc, monedas_desc):
    """Imprime en consola los resultados procesados de la Opción 4."""
    total_monedas = len(monedas_unicas)
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 4")
    print("==================================================")

    print("\n--- LISTA DE MONEDAS ÚNICAS (" + str(total_monedas) + ") ---")
    i = 0
    while i < total_monedas:
        m = monedas_unicas[i]
        formato_moneda = fs.formatear_moneda_codigo_nombre(m[0], m[1])
        print("  " + str(i + 1) + ". " + formato_moneda + " (Tasa: " + str(m[2]) + ")")
        i = i + 1

    print("\n• Cantidad de monedas con exactamente " + str(n_letras) + " letras en su nombre: " + str(monedas_con_n) + " monedas")

    prom_tasa_red = calc.redondear_manual(promedio_tasa, 4)

    print("\n--- ESTADÍSTICAS Y OPERACIONES NUMÉRICAS ---")
    print("• Tasa de cambio promedio: " + str(prom_tasa_red))

    if moneda_fuerte is not None:
        print("• Moneda más fuerte (Mayor tasa): " + str(moneda_fuerte[1]) + " (" + str(moneda_fuerte[0]) + ") con tasa " + str(moneda_fuerte[2]))
    if moneda_debil is not None:
        print("• Moneda más débil (Menor tasa): " + str(moneda_debil[1]) + " (" + str(moneda_debil[0]) + ") con tasa " + str(moneda_debil[2]))

    print("\n• Clasificación según la tasa frente a 1 USD:")
    print("  - Monedas con tasa > 1 USD: " + str(mayores_1))
    print("  - Monedas con tasa = 1 USD: " + str(iguales_1))
    print("  - Monedas con tasa < 1 USD: " + str(menores_1))
    print("  - Total monedas clasificadas: " + str(suma_conteos))

    print("\n--- MONEDAS ORDENADAS POR TASA (ASCENDENTE - De menor a mayor) ---")
    i = 0
    while i < total_monedas:
        m = monedas_asc[i]
        print("  " + str(i + 1) + ". " + str(m[0]) + " - " + str(m[1]) + ": " + str(m[2]))
        i = i + 1

    print("\n--- MONEDAS ORDENADAS POR TASA (DESCENDENTE - De mayor a menor) ---")
    i = 0
    while i < total_monedas:
        m = monedas_desc[i]
        print("  " + str(i + 1) + ". " + str(m[0]) + " - " + str(m[1]) + ": " + str(m[2]))
        i = i + 1

    print("==================================================")


def ejecutar_opcion_4():
    """
    Opción 4: Procesar datos de monedas.
    Carga los datos desde paises_datos.toon, procesa monedas únicas,
    solicita N letras, calcula estadísticas y ordena monedas.
    """
    print("\n--- OPCIÓN 4: PROCESAR DATOS DE MONEDAS ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    monedas_unicas = calc.extraer_monedas_unicas(lista_normalizados)
    n_letras = _solicitar_n_letras_moneda()
    monedas_con_n = calc.contar_monedas_con_n_letras(monedas_unicas, n_letras)

    promedio_tasa = calc.calcular_tasa_promedio_monedas(monedas_unicas)
    moneda_fuerte = calc.obtener_moneda_mas_fuerte_opcion4(monedas_unicas)
    moneda_debil = calc.obtener_moneda_mas_debil_opcion4(monedas_unicas)
    mayores_1, iguales_1, menores_1 = calc.clasificar_monedas_por_tasa(monedas_unicas)
    suma_conteos = mayores_1 + iguales_1 + menores_1

    monedas_asc = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=False)
    monedas_desc = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=True)

    _imprimir_resultados_opcion_4(monedas_unicas, n_letras, monedas_con_n, promedio_tasa, moneda_fuerte, moneda_debil, mayores_1, iguales_1, menores_1, suma_conteos, monedas_asc, monedas_desc)


def ejecutar_opcion_5():
    """
    Opción 5: Generar reporte de países en TXT.
    Carga los países desde paises_datos.toon, normaliza datos y genera el archivo reporte_paises.txt.
    """
    print("\n--- OPCIÓN 5: GENERAR REPORTE DE PAÍSES EN TXT ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    exito = reportes.generar_reporte_paises_txt(lista_normalizados, "reporte_paises.txt")
    if exito:
        print(" Reporte TXT generado exitosamente en 'reporte_paises.txt'.")


def ejecutar_opcion_6():
    """
    Opción 6: Generar reporte de monedas en HTML.
    Carga los países desde paises_datos.toon, normaliza datos y genera el archivo reporte_monedas.html.
    """
    print("\n--- OPCIÓN 6: GENERAR REPORTE DE MONEDAS EN HTML ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    exito = reportes.generar_reporte_monedas_html(lista_normalizados, "reporte_monedas.html")
    if exito:
        print(" Reporte HTML de monedas generado exitosamente en 'reporte_monedas.html'.")


def ejecutar_opcion_7():
    """
    Opción 7: Generar reporte de densidad poblacional en HTML.
    Carga los países desde paises_datos.toon, normaliza datos y genera el archivo reporte_densidad.html.
    """
    print("\n--- OPCIÓN 7: GENERAR REPORTE DE DENSIDAD POBLACIONAL EN HTML ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    lista_normalizados = calc.normalizar_datos_paises(lista_paises)
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    exito = reportes.generar_reporte_densidad_html(lista_normalizados, "reporte_densidad.html")
    if exito:
        print(" Reporte HTML de densidad generado exitosamente en 'reporte_densidad.html'.")


def main():
    """Función principal para controlar el menú."""
    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ")
        opcion = fs.limpiar_espacios_extremos(opcion)

        if opcion == "1":
            ejecutar_opcion_1()
        elif opcion == "2":
            ejecutar_opcion_2()
        elif opcion == "3":
            ejecutar_opcion_3()
        elif opcion == "4":
            ejecutar_opcion_4()
        elif opcion == "5":
            ejecutar_opcion_5()
        elif opcion == "6":
            ejecutar_opcion_6()
        elif opcion == "7":
            ejecutar_opcion_7()
        elif opcion == "8":
            print("\n[Opción 8] - Submenú de bitácora (En desarrollo...)")
        elif opcion == "9":
            print("\n¡Gracias por utilizar el sistema!")
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 9.")


if __name__ == "__main__":
    main()
