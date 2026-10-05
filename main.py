"""
Módulo Principal - TP1.
Sistema de Formateo y Análisis de Datos de Países y Monedas.

Estilo de código: Estudiante de primer año de programación.
Estructura de control mediante ciclos while y condicionales if/elif/else.
"""

import datetime
import datos
import formateo_strings as fs
import calculos as calc


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


def ejecutar_opcion_1():
    """
    Opción 1: Carga los datos del archivo CSV, los guarda en un archivo .toon
    y muestra las estadísticas solicitadas en consola.

    CRITERIO DE VALOR DE MONEDAS FRENTE AL USD:
    - La tasa de cambio indica cuántas unidades de la moneda equivalen a 1 USD.
    - Tasa BAJA (ejemplo: EUR 0.91): La moneda vale MÁS frente al dólar (mayor valor).
    - Tasa ALTA (ejemplo: COP 4150): La moneda vale MENOS frente al dólar (menor valor).
    """
    print("\n--- OPCIÓN 1: DESCARGAR DATOS DE PAÍSES (CSV) ---")
    ruta_input = input("Ingrese el nombre/ruta del archivo CSV (Presione Enter para 'paises.csv'): ")
    ruta_limpia = fs.limpiar_espacios_extremos(ruta_input)

    if len(ruta_limpia) == 0:
        ruta_csv = "paises.csv"
    else:
        ruta_csv = ruta_limpia

    print("Cargando datos desde: " + ruta_csv + " ...")
    lista_paises = datos.leer_csv_paises(ruta_csv)

    if lista_paises is None or len(lista_paises) == 0:
        print("No se pudieron cargar los datos. Regresando al menú principal.")
        return

    # Guardar datos crudos en formato TOON
    archivo_toon = "paises_datos.toon"
    exito_toon = datos.guardar_datos_toon(lista_paises, archivo_toon)
    if exito_toon:
        print("Datos crudos guardados exitosamente en '" + archivo_toon + "'.")

    # 1. Cantidad de países cargados
    total_paises = len(lista_paises)

    # 2. Top 5 países con mayor población
    paises_por_pob = calc.ordenar_paises_por_poblacion_descendente(lista_paises)
    top_5_poblacion = calc.obtener_primeros_elementos(paises_por_pob, 5)

    # 3. Top 5 países con menor área
    paises_por_area = calc.ordenar_paises_por_area_ascendente(lista_paises)
    top_5_area = calc.obtener_primeros_elementos(paises_por_area, 5)

    # 4. Fecha de la tasa de cambio (Fecha actual del sistema)
    fecha_hoy = str(datetime.date.today())

    # 5. Cantidad de monedas y procesamiento de tipos de cambio
    monedas_unicas = calc.extraer_monedas_unicas(lista_paises)
    total_monedas = len(monedas_unicas)

    # Monedas con mayor valor frente al USD (Tasa de cambio más baja)
    monedas_mayor_valor = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=False)
    top_5_monedas_mayor_valor = calc.obtener_primeros_elementos(monedas_mayor_valor, 5)

    # Monedas con menor valor frente al USD (Tasa de cambio más alta)
    monedas_menor_valor = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=True)
    top_5_monedas_menor_valor = calc.obtener_primeros_elementos(monedas_menor_valor, 5)

    # MOSTRAR RESULTADOS EN CONSOLA
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
    while i < len(top_5_monedas_mayor_valor):
        m = top_5_monedas_mayor_valor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n• Top 5 monedas con MENOR valor frente al USD (Tasa más alta):")
    i = 0
    while i < len(top_5_monedas_menor_valor):
        m = top_5_monedas_menor_valor[i]
        print("  " + str(i + 1) + ". " + str(m[1]) + " (" + str(m[0]) + ") - 1 USD = " + str(m[2]) + " " + str(m[0]))
        i = i + 1

    print("\n==================================================")


def ejecutar_opcion_2():
    """
    Opción 2: Lee los países desde paises_datos.toon, aplica las 8 reglas de normalización
    a los nombres de países, guarda los nombres normalizados de vuelta en paises_datos.toon
    y muestra las métricas requeridas por consola.
    """
    print("\n--- OPCIÓN 2: PROCESAR Y NORMALIZAR NOMBRES DE PAÍSES ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        print("No se encontraron datos. Primero ejecute la Opción 1.")
        return

    # Normalización de los nombres de los países
    lista_normalizados = []
    i = 0
    cantidad = len(lista_paises)

    while i < cantidad:
        p = lista_paises[i]
        nombre_original = p[0]
        nombre_normalizado = fs.normalizar_nombre(nombre_original)
        pais_norm = (nombre_normalizado, p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        lista_normalizados.append(pais_norm)
        i = i + 1

    # Guardar de vuelta en paises_datos.toon
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")
    print("Nombres normalizados guardados correctamente en 'paises_datos.toon'.")

    # Pedir letra al usuario y validar que sea exactamente 1 letra alfabética
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

    # Cálculos y estadísticas
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


def ejecutar_opcion_3():
    """
    Opción 3: Procesar datos poblacionales y geográficos.
    Carga los países desde paises_datos.toon (si no existe, indica "Primero ejecute la Opción 1").
    Normaliza nombre, capital y moneda de cada país si es necesario.
    Calcula e imprime por consola:
    - Población total, promedio y mediana.
    - Clasificación y conteos por categoría de población.
    - Área total y densidad poblacional por país.
    - Top 10 países con mayor densidad y Top 10 con menor densidad.
    Guarda los datos normalizados de vuelta en paises_datos.toon.
    """
    print("\n--- OPCIÓN 3: PROCESAR DATOS POBLACIONALES Y GEOGRÁFICOS ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    # Normalizar datos (nombre, capital y moneda)
    lista_normalizados = calc.normalizar_datos_paises(lista_paises)

    # Guardar de vuelta en paises_datos.toon
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    # 1. CÁLCULOS POBLACIONALES
    pob_total = calc.calcular_poblacion_total(lista_normalizados)
    pob_promedio = calc.calcular_poblacion_promedio(lista_normalizados)
    pob_mediana = calc.calcular_mediana_poblacion(lista_normalizados)
    mega, grande, mediana, pequena = calc.clasificar_paises_por_poblacion(lista_normalizados)
    suma_categorias = mega + grande + mediana + pequena

    # 2. CÁLCULOS GEOGRÁFICOS Y DENSIDAD
    area_total = calc.calcular_area_total(lista_normalizados)
    lista_densidades = calc.calcular_densidades_poblacionales(lista_normalizados)

    densidades_mayor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=True)
    top_10_mayor_densidad = calc.obtener_primeros_elementos(densidades_mayor, 10)

    densidades_menor = calc.ordenar_paises_por_densidad(lista_densidades, descendente=False)
    top_10_menor_densidad = calc.obtener_primeros_elementos(densidades_menor, 10)

    # 3. MOSTRAR RESULTADOS EN CONSOLA
    print("\n==================================================")
    print("          RESULTADOS DE LA OPCIÓN 3")
    print("==================================================")

    print("\n--- DATOS POBLACIONALES ---")
    print("• Población total mundial: " + str(pob_total) + " habitantes")
    print("• Población promedio por país: " + str(round(pob_promedio, 2)) + " habitantes")
    print("• Mediana de población: " + str(round(pob_mediana, 2)) + " habitantes")

    print("\n• Clasificación de países por tamaño poblacional:")
    print("  - Megaciudad (> 10,000,000): " + str(mega) + " países")
    print("  - Ciudad grande (1,000,000 - 10,000,000): " + str(grande) + " países")
    print("  - Ciudad mediana (100,000 - 999,999): " + str(mediana) + " países")
    print("  - Ciudad pequeña (< 100,000): " + str(pequena) + " países")
    print("  - Total países clasificados: " + str(suma_categorias))

    print("\n--- DATOS GEOGRÁFICOS Y DENSIDAD ---")
    print("• Área total mundial: " + str(area_total) + " km²")

    print("\n• Top 10 países con MAYOR densidad poblacional:")
    i = 0
    while i < len(top_10_mayor_densidad):
        d = top_10_mayor_densidad[i]
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(round(d[4], 2)) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("\n• Top 10 países con MENOR densidad poblacional:")
    i = 0
    while i < len(top_10_menor_densidad):
        d = top_10_menor_densidad[i]
        print("  " + str(i + 1) + ". " + str(d[0]) + " (" + str(d[1]) + ") - Densidad: " + str(round(d[4], 2)) + " hab/km² (Pob: " + str(d[2]) + ", Área: " + str(d[3]) + " km²)")
        i = i + 1

    print("==================================================")


def ejecutar_opcion_4():
    """
    Opción 4: Procesar datos de monedas.
    Carga los datos desde paises_datos.toon (si no existe, indica "Primero ejecute la Opción 1").
    Procesa las MONEDAS ÚNICAS (21 monedas).

    CRITERIO DE VALOR DE MONEDAS EN OPCIÓN 4 (Páginas 17-18 del PDF):
    - Moneda más fuerte = La de MAYOR tasa de cambio frente al USD.
    - Moneda más débil = La de MENOR tasa de cambio frente al USD.
    NOTA CRÍTICA: Este criterio es el especificado literalmente en el enunciado para la Opción 4
    y difiere de la Opción 1 (donde una tasa menor significa mayor valor frente al USD).
    No se modifica la Opción 1.

    Solicita al usuario N (entero positivo mayor a 0) y cuenta monedas cuyo nombre normalizado
    tenga exactamente N letras (sin contar espacios).

    Calcula e imprime por consola:
    - Formato "CODIGO - Nombre" de cada moneda única.
    - Conteo de monedas con N letras.
    - Tasa de cambio promedio.
    - Moneda más fuerte y más débil (con sus tasas).
    - Cantidad de monedas con tasa > 1 USD, = 1 USD y < 1 USD.
    - Lista de tasas ordenadas de forma ascendente y descendente.

    Guarda los datos normalizados de vuelta en paises_datos.toon.
    """
    print("\n--- OPCIÓN 4: PROCESAR DATOS DE MONEDAS ---")
    lista_paises = datos.leer_datos_toon("paises_datos.toon")

    if lista_paises is None or len(lista_paises) == 0:
        return

    # Normalizar datos (nombre, capital y moneda) de los países
    lista_normalizados = calc.normalizar_datos_paises(lista_paises)

    # Guardar de vuelta en paises_datos.toon
    datos.guardar_datos_toon(lista_normalizados, "paises_datos.toon")

    # Extraer monedas únicas (21 monedas)
    monedas_unicas = calc.extraer_monedas_unicas(lista_normalizados)
    total_monedas = len(monedas_unicas)

    # Solicitar N al usuario y validar que sea un entero positivo mayor a 0
    valido = False
    n_letras = 0

    while not valido:
        n_input = input("\nIngrese la cantidad de letras N a buscar en los nombres de monedas: ")
        if fs.es_numero_entero_positivo(n_input):
            n_letras = fs.convertir_a_entero(n_input)
            valido = True
        else:
            print(" Error: Debe ingresar un número entero positivo mayor a 0.")

    # 1. STRINGS Y FORMATO "CODIGO - Nombre"
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

    monedas_con_n = calc.contar_monedas_con_n_letras(monedas_unicas, n_letras)
    print("\n• Cantidad de monedas con exactamente " + str(n_letras) + " letras en su nombre: " + str(monedas_con_n) + " monedas")

    # 2. OPERACIONES NUMÉRICAS Y CRITERIOS EN OPCIÓN 4
    promedio_tasa = calc.calcular_tasa_promedio_monedas(monedas_unicas)
    moneda_fuerte = calc.obtener_moneda_mas_fuerte_opcion4(monedas_unicas)
    moneda_debil = calc.obtener_moneda_mas_debil_opcion4(monedas_unicas)
    mayores_1, iguales_1, menores_1 = calc.clasificar_monedas_por_tasa(monedas_unicas)
    suma_conteos = mayores_1 + iguales_1 + menores_1

    print("\n--- ESTADÍSTICAS Y OPERACIONES NUMÉRICAS ---")
    print("• Tasa de cambio promedio: " + str(round(promedio_tasa, 4)))

    if moneda_fuerte is not None:
        print("• Moneda más fuerte (Mayor tasa): " + str(moneda_fuerte[1]) + " (" + str(moneda_fuerte[0]) + ") con tasa " + str(moneda_fuerte[2]))
    if moneda_debil is not None:
        print("• Moneda más débil (Menor tasa): " + str(moneda_debil[1]) + " (" + str(moneda_debil[0]) + ") con tasa " + str(moneda_debil[2]))

    print("\n• Clasificación según la tasa frente a 1 USD:")
    print("  - Monedas con tasa > 1 USD: " + str(mayores_1))
    print("  - Monedas con tasa = 1 USD: " + str(iguales_1))
    print("  - Monedas con tasa < 1 USD: " + str(menores_1))
    print("  - Total monedas clasificadas: " + str(suma_conteos))

    # 3. LISTAS DE TASAS ORDENADAS
    monedas_asc = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=False)
    monedas_desc = calc.ordenar_monedas_por_tasa(monedas_unicas, descendente=True)

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
            print("\n[Opción 5] - Generar reporte de países en TXT (En desarrollo...)")

        elif opcion == "6":
            print("\n[Opción 6] - Generar reporte de monedas en HTML (En desarrollo...)")
        elif opcion == "7":
            print("\n[Opción 7] - Generar reporte de densidad poblacional en HTML (En desarrollo...)")
        elif opcion == "8":
            print("\n[Opción 8] - Submenú de bitácora (En desarrollo...)")
        elif opcion == "9":
            print("\n¡Gracias por utilizar el sistema!")
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 9.")


if __name__ == "__main__":
    main()
