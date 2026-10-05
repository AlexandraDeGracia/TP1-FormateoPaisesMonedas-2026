#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-05
"""
Módulo de Formateo y Normalización de Cadenas de Texto.
Proporciona funciones para manipular y normalizar textos carácter por carácter
utilizando únicamente estructuras básicas como ciclos while e índices.
"""

MINUSCULAS = "abcdefghijklmnopqrstuvwxyzáàâãäåéèêëíìîïóòôõöúùûüñç"
MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÄÅÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÑÇ"


# Definición de función: esCaracterBlanco
def esCaracterBlanco(caracter):
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


# Definición de función: buscarIndiceCaracter
def buscarIndiceCaracter(caracter, cadenaBusqueda):
    """Busca la posición de un carácter dentro de una cadena. Retorna el índice o -1."""
    i = 0
    longitud = len(cadenaBusqueda)
    while i < longitud:
        if cadenaBusqueda[i] == caracter:
            return i
        i = i + 1
    return -1


# Definición de función: aMayusculaCaracter
def aMayusculaCaracter(caracter):
    """Convierte un único carácter a mayúscula."""
    idx = buscarIndiceCaracter(caracter, MINUSCULAS)
    if idx != -1:
        return MAYUSCULAS[idx]
    return caracter


# Definición de función: aMinusculaCaracter
def aMinusculaCaracter(caracter):
    """Convierte un único carácter a minúscula."""
    idx = buscarIndiceCaracter(caracter, MAYUSCULAS)
    if idx != -1:
        return MINUSCULAS[idx]
    return caracter


# Definición de función: aMayusculas
def aMayusculas(texto):
    """Convierte un texto completo a mayúsculas carácter por carácter."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + aMayusculaCaracter(texto[i])
        i = i + 1
    return resultado


# Definición de función: aMinusculas
def aMinusculas(texto):
    """Convierte un texto completo a minúsculas carácter por carácter."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + aMinusculaCaracter(texto[i])
        i = i + 1
    return resultado


# Definición de función: obtenerSubcadena
def obtenerSubcadena(texto, inicio, fin):
    """Extrae una subcadena desde la posición inicio hasta fin exclusiva."""
    resultado = ""
    i = inicio
    longitud = len(texto)
    while i < fin and i < longitud:
        resultado = resultado + texto[i]
        i = i + 1
    return resultado


# Definición de función: limpiarEspaciosExtremos
def limpiarEspaciosExtremos(texto):
    """Remueve espacios en blanco y saltos de línea al inicio y final del texto."""
    longitud = len(texto)
    if longitud == 0:
        return ""

    inicio = 0
    while inicio < longitud and esCaracterBlanco(texto[inicio]):
        inicio = inicio + 1

    fin = longitud - 1
    while fin >= inicio and esCaracterBlanco(texto[fin]):
        fin = fin - 1

    resultado = ""
    posicion = inicio
    while posicion <= fin:
        resultado = resultado + texto[posicion]
        posicion = posicion + 1

    return resultado


# Definición de función: quitarTildesCaracter
def quitarTildesCaracter(caracter):
    """Reemplaza vocales acentuadas, ñ y ç por su equivalente simple conservando mayúscula/minúscula."""
    if caracter == "Á" or caracter == "À" or caracter == "Â" or caracter == "Ã" or caracter == "Ä" or caracter == "Å":
        return "A"
    if caracter == "á" or caracter == "à" or caracter == "â" or caracter == "ã" or caracter == "ä" or caracter == "å":
        return "a"

    if caracter == "É" or caracter == "È" or caracter == "Ê" or caracter == "Ë":
        return "E"
    if caracter == "é" or caracter == "è" or caracter == "ê" or caracter == "ë":
        return "e"

    if caracter == "Í" or caracter == "Ì" or caracter == "Î" or caracter == "Ï":
        return "I"
    if caracter == "í" or caracter == "ì" or caracter == "î" or caracter == "ï":
        return "i"

    if caracter == "Ó" or caracter == "Ò" or caracter == "Ô" or caracter == "Õ" or caracter == "Ö":
        return "O"
    if caracter == "ó" or caracter == "ò" or caracter == "ô" or caracter == "õ" or caracter == "ö":
        return "o"

    if caracter == "Ú" or caracter == "Ù" or caracter == "Û" or caracter == "Ü":
        return "U"
    if caracter == "ú" or caracter == "ù" or caracter == "û" or caracter == "ü":
        return "u"

    if caracter == "Ñ":
        return "N"
    if caracter == "ñ":
        return "n"

    if caracter == "Ç":
        return "C"
    if caracter == "ç":
        return "c"

    return caracter


# Definición de función: quitarTildes
def quitarTildes(texto):
    """Reemplaza caracteres especiales y acentuados por sus equivalentes simples."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        resultado = resultado + quitarTildesCaracter(texto[i])
        i = i + 1
    return resultado


# Definición de función: quitarCaracteresEspeciales
def quitarCaracteresEspeciales(texto):
    """Elimina comillas simples, guiones y acentos graves."""
    resultado = ""
    i = 0
    longitud = len(texto)
    while i < longitud:
        caracter = texto[i]
        if caracter != "'" and caracter != "-" and caracter != "`":
            resultado = resultado + caracter
        i = i + 1
    return resultado


# Definición de función: quitarParentesis
def quitarParentesis(texto):
    """Elimina paréntesis y todo su contenido interno carácter por carácter."""
    resultado = ""
    i = 0
    longitud = len(texto)
    nivelParentesis = 0

    while i < longitud:
        caracter = texto[i]
        if caracter == "(":
            nivelParentesis = nivelParentesis + 1
        elif caracter == ")":
            if nivelParentesis > 0:
                nivelParentesis = nivelParentesis - 1
        else:
            if nivelParentesis == 0:
                resultado = resultado + caracter
        i = i + 1

    return resultado


# Definición de función: guionesBajosAEspacios
def guionesBajosAEspacios(texto):
    """Convierte cada guion bajo en un espacio en blanco."""
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


# Definición de función: capitalizarPalabras
def capitalizarPalabras(texto):
    """Capitaliza la primera letra de cada palabra y deja el resto en minúscula."""
    textoMin = aMinusculas(texto)
    resultado = ""
    i = 0
    longitud = len(textoMin)
    nuevaPalabra = True

    while i < longitud:
        caracter = textoMin[i]
        if esCaracterBlanco(caracter):
            resultado = resultado + caracter
            nuevaPalabra = True
        else:
            if nuevaPalabra:
                resultado = resultado + aMayusculaCaracter(caracter)
                nuevaPalabra = False
            else:
                resultado = resultado + caracter
        i = i + 1

    return resultado


# Definición de función: colapsarEspaciosMultiples
def colapsarEspaciosMultiples(texto):
    """Elimina espacios extremos y reduce múltiples espacios seguidos a uno solo."""
    textoLimpio = limpiarEspaciosExtremos(texto)
    resultado = ""
    i = 0
    longitud = len(textoLimpio)
    enEspacio = False

    while i < longitud:
        caracter = textoLimpio[i]
        if esCaracterBlanco(caracter):
            if not enEspacio:
                resultado = resultado + " "
                enEspacio = True
        else:
            resultado = resultado + caracter
            enEspacio = False
        i = i + 1

    return resultado


# Definición de función: normalizarNombre
def normalizarNombre(nombre):
    """Aplica las 8 reglas de normalización a un nombre de país."""
    p1 = aMayusculas(nombre)
    p2 = limpiarEspaciosExtremos(p1)
    p3 = quitarTildes(p2)
    p4 = quitarCaracteresEspeciales(p3)
    p5 = quitarParentesis(p4)
    p6 = guionesBajosAEspacios(p5)
    p7 = capitalizarPalabras(p6)
    p8 = colapsarEspaciosMultiples(p7)
    return p8


# Definición de función: esLetraValida
def esLetraValida(caracter):
    """Verifica si un único carácter es una letra alfabética."""
    if len(caracter) != 1:
        return False
    if buscarIndiceCaracter(caracter, MINUSCULAS) != -1:
        return True
    if buscarIndiceCaracter(caracter, MAYUSCULAS) != -1:
        return True
    return False


# Definición de función: contieneLetraNormalizada
def contieneLetraNormalizada(texto, letraBuscar):
    """Verifica si texto contiene letraBuscar en mayúsculas y sin tildes."""
    letraNorm = quitarTildes(aMayusculas(letraBuscar))
    textoNorm = quitarTildes(aMayusculas(texto))

    i = 0
    longitud = len(textoNorm)
    while i < longitud:
        if textoNorm[i] == letraNorm:
            return True
        i = i + 1
    return False


# Definición de función: contieneSubcadena
def contieneSubcadena(texto, subcadena):
    """Verifica si subcadena está contenida en texto ignorando mayúsculas y tildes."""
    textoNorm = quitarTildes(aMayusculas(texto))
    subNorm = quitarTildes(aMayusculas(subcadena))

    lenTexto = len(textoNorm)
    lenSub = len(subNorm)

    if lenSub == 0:
        return True
    if lenSub > lenTexto:
        return False

    i = 0
    while i <= lenTexto - lenSub:
        j = 0
        coincide = True
        while j < lenSub:
            if textoNorm[i + j] != subNorm[j]:
                coincide = False
                j = lenSub
            else:
                j = j + 1

        if coincide:
            return True
        i = i + 1

    return False


# Definición de función: separarCadena
def separarCadena(cadena, delimitador):
    """Separa una cadena según un delimitador carácter por carácter."""
    partes = []
    parteActual = ""
    posicion = 0
    longitud = len(cadena)

    while posicion < longitud:
        caracter = cadena[posicion]
        if caracter == delimitador:
            partes.append(parteActual)
            parteActual = ""
        else:
            parteActual = parteActual + caracter
        posicion = posicion + 1

    partes.append(parteActual)
    return partes


# Definición de función: convertirAEntero
def convertirAEntero(texto):
    """Limpia el texto y lo convierte a entero."""
    textoLimpio = limpiarEspaciosExtremos(texto)
    if len(textoLimpio) == 0:
        return 0
    return int(textoLimpio)


# Definición de función: convertirAFlotante
def convertirAFlotante(texto):
    """Limpia el texto y lo convierte a flotante."""
    textoLimpio = limpiarEspaciosExtremos(texto)
    if len(textoLimpio) == 0:
        return 0.0
    return float(textoLimpio)


# Definición de función: esNumeroEnteroPositivo
def esNumeroEnteroPositivo(cadena):
    """Verifica si una cadena representa un número entero positivo mayor a 0."""
    cadenaLimpia = limpiarEspaciosExtremos(cadena)
    longitud = len(cadenaLimpia)
    if longitud == 0:
        return False

    i = 0
    while i < longitud:
        caracter = cadenaLimpia[i]
        if buscarIndiceCaracter(caracter, "0123456789") == -1:
            return False
        i = i + 1

    valor = convertirAEntero(cadenaLimpia)
    if valor <= 0:
        return False

    return True


# Definición de función: contarLetrasSinEspacios
def contarLetrasSinEspacios(texto):
    """Cuenta la cantidad de caracteres excluyendo espacios en blanco."""
    contador = 0
    i = 0
    longitud = len(texto)
    while i < longitud:
        if not esCaracterBlanco(texto[i]):
            contador = contador + 1
        i = i + 1
    return contador


# Definición de función: formatearMonedaCodigoNombre
def formatearMonedaCodigoNombre(codigoMoneda, nombreMoneda):
    """Retorna la cadena en formato 'CODIGO - Nombre' eliminando solo tildes."""
    nombreNorm = quitarTildes(nombreMoneda)
    return str(codigoMoneda) + " - " + str(nombreNorm)


# Definición de función: esEnteroValido
def esEnteroValido(texto):
    """Verifica si una cadena representa un entero válido (opcionalmente con signo)."""
    cadena = limpiarEspaciosExtremos(texto)
    longitud = len(cadena)
    if longitud == 0:
        return False

    i = 0
    if cadena[0] == "+" or cadena[0] == "-":
        if longitud == 1:
            return False
        i = 1

    while i < longitud:
        if buscarIndiceCaracter(cadena[i], "0123456789") == -1:
            return False
        i = i + 1

    return True


# Definición de función: esFlotanteValido
def esFlotanteValido(texto):
    """Verifica si una cadena representa un flotante válido con máximo un punto."""
    cadena = limpiarEspaciosExtremos(texto)
    longitud = len(cadena)
    if longitud == 0:
        return False

    i = 0
    if cadena[0] == "+" or cadena[0] == "-":
        if longitud == 1:
            return False
        i = 1

    puntos = 0
    digitos = 0

    while i < longitud:
        caracter = cadena[i]
        if caracter == ".":
            puntos = puntos + 1
            if puntos > 1:
                return False
        elif buscarIndiceCaracter(caracter, "0123456789") != -1:
            digitos = digitos + 1
        else:
            return False
        i = i + 1

    if digitos == 0:
        return False

    return True
