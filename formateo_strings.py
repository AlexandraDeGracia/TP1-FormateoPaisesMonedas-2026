"""
Módulo de Formateo y Normalización de Cadenas de Texto.
Estilo de código: Estudiante de primer año de programación.

RESTRICCIONES STRICTAS:
- Prohibido el uso de .replace(), .upper(), .lower(), .strip(), .title(), .capitalize(), .split(), etc.
- Procesamiento carácter por carácter con ciclos while e índices.
- Sin diccionarios, sin expresiones complejas.
"""

MINUSCULAS = "abcdefghijklmnopqrstuvwxyzáàâãäåéèêëíìîïóòôõöúùûüñç"
MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÄÅÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÑÇ"


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


def buscar_indice_caracter(caracter, cadena_busqueda):
    """
    Busca la posición de un carácter dentro de una cadena de búsqueda
    recorriendo los caracteres con un ciclo while. Retorna el índice o -1.
    """
    i = 0
    longitud = len(cadena_busqueda)
    while i < longitud:
        if cadena_busqueda[i] == caracter:
            return i
        i = i + 1
    return -1


def a_mayuscula_caracter(caracter):
    """Convierte un único carácter a mayúscula usando la cadena MINUSCULAS."""
    idx = buscar_indice_caracter(caracter, MINUSCULAS)
    if idx != -1:
        return MAYUSCULAS[idx]
    return caracter


def a_minuscula_caracter(caracter):
    """Convierte un único carácter a minúscula usando la cadena MAYUSCULAS."""
    idx = buscar_indice_caracter(caracter, MAYUSCULAS)
    if idx != -1:
        return MINUSCULAS[idx]
    return caracter


def a_mayusculas(texto):
    """Convierte un texto completo a mayúsculas carácter por carácter con un ciclo while."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + a_mayuscula_caracter(texto[i])
        i = i + 1
    return resultado


def a_minusculas(texto):
    """Convierte un texto completo a minúsculas carácter por carácter con un ciclo while."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + a_minuscula_caracter(texto[i])
        i = i + 1
    return resultado


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


def quitar_tildes_caracter(caracter):
    """
    Reemplaza vocales acentuadas, ñ y ç por su equivalente simple (A, E, I, O, U, N, C).
    Funciona tanto con minúsculas como con mayúsculas.
    """
    if caracter == "Á" or caracter == "À" or caracter == "Â" or caracter == "Ã" or caracter == "Ä" or caracter == "Å" or caracter == "á" or caracter == "à" or caracter == "â" or caracter == "ã" or caracter == "ä" or caracter == "å":
        return "A"
    if caracter == "É" or caracter == "È" or caracter == "Ê" or caracter == "Ë" or caracter == "é" or caracter == "è" or caracter == "ê" or caracter == "ë":
        return "E"
    if caracter == "Í" or caracter == "Ì" or caracter == "Î" or caracter == "Ï" or caracter == "í" or caracter == "ì" or caracter == "î" or caracter == "ï":
        return "I"
    if caracter == "Ó" or caracter == "Ò" or caracter == "Ô" or caracter == "Õ" or caracter == "Ö" or caracter == "ó" or caracter == "ò" or caracter == "ô" or caracter == "õ" or caracter == "ö":
        return "O"
    if caracter == "Ú" or caracter == "Ù" or caracter == "Û" or caracter == "Ü" or caracter == "ú" or caracter == "ù" or caracter == "û" or caracter == "ü":
        return "U"
    if caracter == "Ñ" or caracter == "ñ":
        return "N"
    if caracter == "Ç" or caracter == "ç":
        return "C"
    return caracter


def quitar_tildes(texto):
    """Reemplaza caracteres especiales y acentuados por sus equivalentes simples."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + quitar_tildes_caracter(texto[i])
        i = i + 1
    return resultado


def quitar_caracteres_especiales(texto):
    """Elimina por completo comillas simples ('), guiones (-) y acentos graves (`)."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        caracter = texto[i]
        if caracter != "'" and caracter != "-" and caracter != "`":
            resultado = resultado + caracter
        i = i + 1
    return resultado


def quitar_parentesis(texto):
    """Elimina paréntesis '(' ')' y todo su contenido interno carácter por carácter."""
    resultado = ""
    i = 0
    longitud = len(texto)
    nivel_parentesis = 0

    while i < longitud:
        caracter = texto[i]
        if caracter == "(":
            nivel_parentesis = nivel_parentesis + 1
        elif caracter == ")":
            if nivel_parentesis > 0:
                nivel_parentesis = nivel_parentesis - 1
        else:
            if nivel_parentesis == 0:
                resultado = resultado + caracter
        i = i + 1

    return resultado


def guiones_bajos_a_espacios(texto):
    """Convierte cada guion bajo '_' en un espacio en blanco."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        caracter = texto[i]
        if caracter == "_":
            resultado = resultado + " "
        else:
            resultado = resultado + caracter
        i = i + 1
    return resultado


def capitalizar_palabras(texto):
    """
    Capitaliza la primera letra de cada palabra en mayúscula
    y deja las demás en minúscula carácter por carácter.
    """
    resultado = ""
    i = 0
    longitud = len(texto)
    nueva_palabra = True

    while i < longitud:
        caracter = texto[i]
        if es_caracter_blanco(caracter):
            resultado = resultado + caracter
            nueva_palabra = True
        else:
            if nueva_palabra:
                resultado = resultado + a_mayuscula_caracter(caracter)
                nueva_palabra = False
            else:
                resultado = resultado + a_minuscula_caracter(caracter)
        i = i + 1

    return resultado


def colapsar_espacios_multiples(texto):
    """Elimina espacios extremos y reduce múltiples espacios seguidos a un único espacio."""
    texto_limpio = limpiar_espacios_extremos(texto)
    resultado = ""
    i = 0
    longitud = len(texto_limpio)
    en_espacio = False

    while i < longitud:
        caracter = texto_limpio[i]
        if es_caracter_blanco(caracter):
            if not en_espacio:
                resultado = resultado + " "
                en_espacio = True
        else:
            resultado = resultado + caracter
            en_espacio = False
        i = i + 1

    return resultado


def normalizar_nombre(nombre):
    """
    Aplica las 8 reglas de normalización a un nombre de país en orden:
    1. Convertir a mayúsculas.
    2. Eliminar espacios al inicio y al final.
    3. Reemplazar caracteres especiales (tildes/acentos/ñ/ç).
    4. Eliminar por completo: ' - `
    5. Eliminar paréntesis y todo su contenido.
    6. Convertir '_' a espacio.
    7. Capitalizar palabras (Primera mayúscula, resto minúscula).
    8. Limpiar espacios sobrantes (extremos y dobles).
    """
    p1 = a_mayusculas(nombre)
    p2 = limpiar_espacios_extremos(p1)
    p3 = quitar_tildes(p2)
    p4 = quitar_caracteres_especiales(p3)
    p5 = quitar_parentesis(p4)
    p6 = guiones_bajos_a_espacios(p5)
    p7 = capitalizar_palabras(p6)
    p8 = colapsar_espacios_multiples(p7)
    return p8


def es_letra_valida(caracter):
    """Verifica si un único carácter es una letra alfabética (incluyendo tildes)."""
    if len(caracter) != 1:
        return False
    if buscar_indice_caracter(caracter, MINUSCULAS) != -1:
        return True
    if buscar_indice_caracter(caracter, MAYUSCULAS) != -1:
        return True
    return False


def contiene_letra_normalizada(texto, letra_buscar):
    """
    Verifica si 'texto' contiene 'letra_buscar' (ambas normalizadas en mayúscula y sin tildes).
    Retorna True o False.
    """
    letra_norm = quitar_tildes(a_mayusculas(letra_buscar))
    texto_norm = quitar_tildes(a_mayusculas(texto))

    i = 0
    longitud = len(texto_norm)
    while i < longitud:
        if texto_norm[i] == letra_norm:
            return True
        i = i + 1
    return False


def separar_cadena(cadena, delimitador):
    """Separa una cadena según un delimitador carácter por carácter."""
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

    partes.append(parte_actual)
    return partes


def convertir_a_entero(texto):
    """Limpia el texto y lo convierte a entero."""
    texto_limpio = limpiar_espacios_extremos(texto)
    if len(texto_limpio) == 0:
        return 0
    return int(texto_limpio)


def convertir_a_flotante(texto):
    """Limpia el texto y lo convierte a flotante."""
    texto_limpio = limpiar_espacios_extremos(texto)
    if len(texto_limpio) == 0:
        return 0.0
    return float(texto_limpio)


def es_numero_entero_positivo(cadena):
    """
    Verifica si una cadena representa un número entero positivo (> 0)
    recorriendo carácter por carácter con un ciclo while.
    """
    cadena_limpia = limpiar_espacios_extremos(cadena)
    longitud = len(cadena_limpia)
    if longitud == 0:
        return False

    i = 0
    while i < longitud:
        caracter = cadena_limpia[i]
        if buscar_indice_caracter(caracter, "0123456789") == -1:
            return False
        i = i + 1

    valor = convertir_a_entero(cadena_limpia)
    if valor <= 0:
        return False

    return True


def contar_letras_sin_espacios(texto):
    """Cuenta la cantidad de caracteres en un texto excluyendo los espacios en blanco."""
    contador = 0
    i = 0
    longitud = len(texto)
    while i < longitud:
        if not es_caracter_blanco(texto[i]):
            contador = contador + 1
        i = i + 1
    return contador


def formatear_moneda_codigo_nombre(codigo_moneda, nombre_moneda):
    """Retorna la cadena en formato 'CODIGO - Nombre'."""
    nombre_norm = normalizar_nombre(nombre_moneda)
    return str(codigo_moneda) + " - " + str(nombre_norm)

