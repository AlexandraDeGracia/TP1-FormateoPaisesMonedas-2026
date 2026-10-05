"""
Módulo de Formateo de Cadenas de Texto.
Estilo de código: Estudiante de primer año de programación.

RESTRICCIONES STRICTAS:
- Prohibido el uso de .replace().
- Procesamiento carácter por carácter con ciclos while e índices.
- Sin diccionarios, sin expresiones complejas.
"""


def es_caracter_blanco(caracter):
    """Verifica si un carácter es espacio, salto de línea o tabulación."""
    if caracter == " ":
        return True
    if caracter == "\n":
        return True
    if caracter == "\r":
        return True
    if caracter == "\t":
        return True
    return False


def limpiar_espacios_extremos(texto):
    """
    Remueve espacios en blanco y saltos de línea al inicio y final del texto
    recorriendo carácter por carácter con un ciclo while.
    """
    longitud = len(texto)
    if longitud == 0:
        return ""

    inicio = 0
    while inicio < longitud and es_caracter_blanco(texto[inicio]):
        inicio = inicio + 1

    fin = longitud - 1
    while fin >= inicio and es_caracter_blanco(texto[fin]):
        fin = fin - 1

    resultado = ""
    posicion = inicio
    while posicion <= fin:
        resultado = resultado + texto[posicion]
        posicion = posicion + 1

    return resultado


def separar_cadena(cadena, delimitador):
    """
    Separa una cadena de texto según un delimitador (ej: ';')
    recorriendo los caracteres uno por uno con un ciclo while.
    Retorna una lista con las partes obtenidas.
    """
    partes = []
    parte_actual = ""
    posicion = 0
    longitud = len(cadena)

    while posicion < longitud:
        caracter = cadena[posicion]
        if caracter == delimitador:
            partes.append(parte_actual)
            parte_actual = ""
        else:
            parte_actual = parte_actual + caracter
        posicion = posicion + 1

    # Agregar la última parte después del último delimitador
    partes.append(parte_actual)
    return partes


def convertir_a_entero(texto):
    """Limpia el texto y lo convierte a número entero."""
    texto_limpio = limpiar_espacios_extremos(texto)
    if len(texto_limpio) == 0:
        return 0
    return int(texto_limpio)


def convertir_a_flotante(texto):
    """Limpia el texto y lo convierte a número flotante (decimal)."""
    texto_limpio = limpiar_espacios_extremos(texto)
    if len(texto_limpio) == 0:
        return 0.0
    return float(texto_limpio)
