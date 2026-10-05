"""
Módulo Principal - TP1 (Estructura Base del Menú).
Sistema de Formateo y Análisis de Datos de Países y Monedas.

Estructura de control básica mediante bucle while y condicionales if/elif/else.
"""

import datos
import formateo_strings as fs
import calculos as calc


def mostrar_menu():
    """Muestra el menú de opciones en la consola."""
    print("\n==================================================")
    print("  SISTEMA DE PAISES Y MONEDAS (TP1)")
    print("==================================================")
    print("  1. Listar todos los países")
    print("  2. Listar monedas y tipos de cambio")
    print("  3. Convertir monto entre dos monedas")
    print("  4. Buscar país por código o nombre")
    print("  5. Calcular densidad poblacional")
    print("  6. Ver países extremos (Mayor/Menor)")
    print("  7. Demostración de formateador de cadenas")
    print("  8. Mostrar estadísticas globales")
    print("  9. Ordenar y clasificar países")
    print("  0. Salir")
    print("--------------------------------------------------")


def main():
    """Función principal para controlar el menú."""
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción (0-9): ")

        if opcion == "1":
            print("\n[Opción 1] - Lista de Países (En desarrollo...)")
        elif opcion == "2":
            print("\n[Opción 2] - Monedas y Tipos de Cambio (En desarrollo...)")
        elif opcion == "3":
            print("\n[Opción 3] - Conversión de Monedas (En desarrollo...)")
        elif opcion == "4":
            print("\n[Opción 4] - Búsqueda de País (En desarrollo...)")
        elif opcion == "5":
            print("\n[Opción 5] - Densidad Poblacional (En desarrollo...)")
        elif opcion == "6":
            print("\n[Opción 6] - Países Extremos (En desarrollo...)")
        elif opcion == "7":
            print("\n[Opción 7] - Formateador de Cadenas (En desarrollo...)")
        elif opcion == "8":
            print("\n[Opción 8] - Estadísticas Globales (En desarrollo...)")
        elif opcion == "9":
            print("\n[Opción 9] - Ordenar Países (En desarrollo...)")
        elif opcion == "0":
            print("\n¡Gracias por utilizar el sistema!")
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 0 al 9.")


if __name__ == "__main__":
    main()
