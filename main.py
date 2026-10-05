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
            print("\n[Opción 3] - Procesar datos poblacionales y geográficos (En desarrollo...)")
        elif opcion == "4":
            print("\n[Opción 4] - Procesar datos de monedas (En desarrollo...)")
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
