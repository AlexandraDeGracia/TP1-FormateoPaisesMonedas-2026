"""
Módulo de Cálculos y Ordenamientos Manuales.
Contiene funciones numéricas, de ordenamiento y agregación desarrolladas
manualmente utilizando únicamente listas, tuplas y ciclos while.
"""

import formateo_strings as fs


# Definición de función: redondearManual
def redondearManual(numero, decimales):
    """Redondea un número a una cantidad especificada de decimales mediante operaciones aritméticas simples."""
    if decimales < 0:
        return numero

    factor = 1.0
    i = 0
    while i < decimales:
        factor = factor * 10.0
        i = i + 1

    scaled = numero * factor
    if scaled >= 0.0:
        entero = int(scaled + 0.5)
    else:
        entero = int(scaled - 0.5)

    return entero / factor


# Definición de función: copiarLista
def copiarLista(listaOriginal):
    """Crea y retorna una copia de una lista usando un ciclo while."""
    copia = []
    i = 0
    cantidad = len(listaOriginal)
    while i < cantidad:
        copia.append(listaOriginal[i])
        i = i + 1
    return copia


# Definición de función: obtenerPrimerosElementos
def obtenerPrimerosElementos(lista, cantidad):
    """Retorna los primeros N elementos de una lista usando un ciclo while."""
    resultado = []
    i = 0
    total = len(lista)
    while i < cantidad and i < total:
        resultado.append(lista[i])
        i = i + 1
    return resultado


# Definición de función: normalizarDatosPaises
def normalizarDatosPaises(listaPaises):
    """Normaliza los nombres, capitales y monedas de una lista de países."""
    listaNormalizada = []
    i = 0
    cantidad = len(listaPaises)

    while i < cantidad:
        p = listaPaises[i]
        nombreNorm = fs.normalizarNombre(p[0])
        capitalNorm = fs.normalizarNombre(p[1])
        monedaSinTildes = fs.quitarTildes(p[5])

        paisTuple = (nombreNorm, capitalNorm, p[2], p[3], p[4], monedaSinTildes, p[6], p[7])
        listaNormalizada.append(paisTuple)
        i = i + 1

    return listaNormalizada


# Definición de función: calcularPoblacionTotal
def calcularPoblacionTotal(listaPaises):
    """Suma manualmente la población de todos los países."""
    total = 0
    i = 0
    cantidad = len(listaPaises)
    while i < cantidad:
        p = listaPaises[i]
        total = total + p[3]
        i = i + 1
    return total


# Definición de función: calcularPoblacionPromedio
def calcularPoblacionPromedio(listaPaises):
    """Calcula la población promedio por país."""
    cantidad = len(listaPaises)
    if cantidad == 0:
        return 0.0
    total = calcularPoblacionTotal(listaPaises)
    return total / cantidad


# Definición de función: calcularMedianaPoblacion
def calcularMedianaPoblacion(listaPaises):
    """Calcula la mediana de población utilizando ordenamiento manual de burbuja."""
    copiaPaises = copiarLista(listaPaises)
    n = len(copiaPaises)
    if n == 0:
        return 0.0

    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copiaPaises[j][3] > copiaPaises[j + 1][3]:
                temp = copiaPaises[j]
                copiaPaises[j] = copiaPaises[j + 1]
                copiaPaises[j + 1] = temp
            j = j + 1
        i = i + 1

    if n % 2 == 1:
        mediana = float(copiaPaises[n // 2][3])
    else:
        m1 = copiaPaises[(n // 2) - 1][3]
        m2 = copiaPaises[n // 2][3]
        mediana = (m1 + m2) / 2.0

    return mediana


# Definición de función: clasificarPaisesPorPoblacion
def clasificarPaisesPorPoblacion(listaPaises):
    """Clasifica los países en 4 categorías según su tamaño poblacional."""
    mega = 0
    grande = 0
    mediana = 0
    pequena = 0

    i = 0
    cantidad = len(listaPaises)
    while i < cantidad:
        pob = listaPaises[i][3]
        if pob > 10000000:
            mega = mega + 1
        elif pob >= 1000000:
            grande = grande + 1
        elif pob >= 100000:
            mediana = mediana + 1
        else:
            pequena = pequena + 1
        i = i + 1

    return mega, grande, mediana, pequena


# Definición de función: calcularAreaTotal
def calcularAreaTotal(listaPaises):
    """Suma manualmente el área geográfica total."""
    total = 0
    i = 0
    cantidad = len(listaPaises)
    while i < cantidad:
        p = listaPaises[i]
        total = total + p[4]
        i = i + 1
    return total


# Definición de función: calcularDensidadesPoblacionales
def calcularDensidadesPoblacionales(listaPaises):
    """Calcula la densidad poblacional de cada país y retorna lista de tuplas."""
    listaDensidades = []
    i = 0
    cantidad = len(listaPaises)
    while i < cantidad:
        p = listaPaises[i]
        nombre = p[0]
        codigo = p[2]
        poblacion = p[3]
        area = p[4]

        if area > 0:
            densidad = poblacion / area
        else:
            densidad = 0.0

        item = (nombre, codigo, poblacion, area, densidad)
        listaDensidades.append(item)
        i = i + 1
    return listaDensidades


# Definición de función: ordenarPaisesPorDensidad
def ordenarPaisesPorDensidad(listaDensidades, descendente=True):
    """Ordena la lista de densidades usando ordenamiento manual de burbuja."""
    copia = copiarLista(listaDensidades)
    n = len(copia)
    if n <= 1:
        return copia

    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            d1 = copia[j][4]
            d2 = copia[j + 1][4]

            intercambiar = False
            if descendente:
                if d1 < d2:
                    intercambiar = True
            else:
                if d1 > d2:
                    intercambiar = True

            if intercambiar:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

            j = j + 1
        i = i + 1

    return copia


# Definición de función: ordenarPaisesPorPoblacionDescendente
def ordenarPaisesPorPoblacionDescendente(listaPaises):
    """Ordena países por población de mayor a menor manualmente."""
    copia = copiarLista(listaPaises)
    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j][3] < copia[j + 1][3]:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        i = i + 1
    return copia


# Definición de función: ordenarPaisesPorAreaAscendente
def ordenarPaisesPorAreaAscendente(listaPaises):
    """Ordena países por área de menor a mayor manualmente."""
    copia = copiarLista(listaPaises)
    n = len(copia)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if copia[j][4] > copia[j + 1][4]:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp
            j = j + 1
        i = i + 1
    return copia


# Definición de función: extraerMonedasUnicas
def extraerMonedasUnicas(listaPaises):
    """Extrae las monedas únicas retornando una lista de tuplas (codigo, nombre, tasaUsd)."""
    monedasUnicas = []
    i = 0
    cantidadPaises = len(listaPaises)

    while i < cantidadPaises:
        p = listaPaises[i]
        nombreMoneda = p[5]
        codigoMoneda = p[6]
        tasaUsd = p[7]

        existe = False
        j = 0
        cantMonedas = len(monedasUnicas)

        while j < cantMonedas:
            m = monedasUnicas[j]
            if m[0] == codigoMoneda:
                existe = True
            j = j + 1

        if not existe:
            tuplaMoneda = (codigoMoneda, nombreMoneda, tasaUsd)
            monedasUnicas.append(tuplaMoneda)

        i = i + 1

    return monedasUnicas


# Definición de función: contarMonedasConNLetras
def contarMonedasConNLetras(listaMonedas, nLetras):
    """Cuenta monedas cuyo nombre normalizado tenga exactamente N letras sin contar espacios."""
    contador = 0
    i = 0
    cantidad = len(listaMonedas)

    while i < cantidad:
        m = listaMonedas[i]
        nombreMoneda = m[1]
        nombreNorm = fs.quitarTildes(nombreMoneda)
        numLetras = fs.contarLetrasSinEspacios(nombreNorm)

        if numLetras == nLetras:
            contador = contador + 1
        i = i + 1

    return contador


# Definición de función: calcularTasaPromedioMonedas
def calcularTasaPromedioMonedas(listaMonedas):
    """Calcula la tasa de cambio promedio de las monedas."""
    cantidad = len(listaMonedas)
    if cantidad == 0:
        return 0.0

    sumaTasas = 0.0
    i = 0
    while i < cantidad:
        m = listaMonedas[i]
        sumaTasas = sumaTasas + m[2]
        i = i + 1

    return sumaTasas / cantidad


# Definición de función: obtenerMonedaMasFuerteOpcion4
def obtenerMonedaMasFuerteOpcion4(listaMonedas):
    """Retorna la moneda con MAYOR tasa de cambio frente al USD (Criterio Opción 4 PDF)."""
    cantidad = len(listaMonedas)
    if cantidad == 0:
        return None

    monedaFuerte = listaMonedas[0]
    maxTasa = monedaFuerte[2]

    i = 1
    while i < cantidad:
        m = listaMonedas[i]
        tasa = m[2]
        if tasa > maxTasa:
            maxTasa = tasa
            monedaFuerte = m
        i = i + 1

    return monedaFuerte


# Definición de función: obtenerMonedaMasDebilOpcion4
def obtenerMonedaMasDebilOpcion4(listaMonedas):
    """Retorna la moneda con MENOR tasa de cambio frente al USD (Criterio Opción 4 PDF)."""
    cantidad = len(listaMonedas)
    if cantidad == 0:
        return None

    monedaDebil = listaMonedas[0]
    minTasa = monedaDebil[2]

    i = 1
    while i < cantidad:
        m = listaMonedas[i]
        tasa = m[2]
        if tasa < minTasa:
            minTasa = tasa
            monedaDebil = m
        i = i + 1

    return monedaDebil


# Definición de función: clasificarMonedasPorTasa
def clasificarMonedasPorTasa(listaMonedas):
    """Clasifica las monedas según su tasa frente a 1 USD (> 1, = 1, < 1)."""
    mayores1 = 0
    iguales1 = 0
    menores1 = 0

    i = 0
    cantidad = len(listaMonedas)
    while i < cantidad:
        m = listaMonedas[i]
        tasa = m[2]

        if tasa > 1.0:
            mayores1 = mayores1 + 1
        elif tasa == 1.0:
            iguales1 = iguales1 + 1
        else:
            menores1 = menores1 + 1

        i = i + 1

    return mayores1, iguales1, menores1


# Definición de función: ordenarMonedasPorTasa
def ordenarMonedasPorTasa(listaMonedas, descendente=False):
    """Ordena las monedas por su tasa de cambio utilizando ordenamiento manual de burbuja."""
    copia = copiarLista(listaMonedas)
    n = len(copia)
    if n <= 1:
        return copia

    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            t1 = copia[j][2]
            t2 = copia[j + 1][2]

            intercambiar = False
            if descendente:
                if t1 < t2:
                    intercambiar = True
            else:
                if t1 > t2:
                    intercambiar = True

            if intercambiar:
                temp = copia[j]
                copia[j] = copia[j + 1]
                copia[j + 1] = temp

            j = j + 1
        i = i + 1

    return copia


# Definición de función: calcularLongitudPromedioNombres
def calcularLongitudPromedioNombres(listaPaises):
    """Calcula la longitud promedio de los nombres de países (retorna entero)."""
    cantidad = len(listaPaises)
    if cantidad == 0:
        return 0

    sumaLongitudes = 0
    i = 0
    while i < cantidad:
        nombre = listaPaises[i][0]
        sumaLongitudes = sumaLongitudes + len(nombre)
        i = i + 1

    return sumaLongitudes // cantidad


# Definición de función: obtenerPaisNombreMasLargo
def obtenerPaisNombreMasLargo(listaPaises):
    """Retorna (nombre, longitud) del país con el nombre más largo."""
    cantidad = len(listaPaises)
    if cantidad == 0:
        return "", 0

    paisMax = listaPaises[0]
    nombreMax = paisMax[0]
    maxLen = len(nombreMax)

    i = 1
    while i < cantidad:
        p = listaPaises[i]
        nombreActual = p[0]
        longitudActual = len(nombreActual)

        if longitudActual > maxLen:
            maxLen = longitudActual
            nombreMax = nombreActual

        i = i + 1

    return nombreMax, maxLen


# Definición de función: obtenerPaisNombreMasCorto
def obtenerPaisNombreMasCorto(listaPaises):
    """Retorna (nombre, longitud) del país con el nombre más corto."""
    cantidad = len(listaPaises)
    if cantidad == 0:
        return "", 0

    paisMin = listaPaises[0]
    nombreMin = paisMin[0]
    minLen = len(nombreMin)

    i = 1
    while i < cantidad:
        p = listaPaises[i]
        nombreActual = p[0]
        longitudActual = len(nombreActual)

        if longitudActual < minLen:
            minLen = longitudActual
            nombreMin = nombreActual

        i = i + 1

    return nombreMin, minLen


# Definición de función: contarPaisesConLetra
def contarPaisesConLetra(listaPaises, letraBuscar):
    """Cuenta cuántos países contienen la letraBuscar en su nombre normalizado."""
    contador = 0
    i = 0
    cantidad = len(listaPaises)

    while i < cantidad:
        nombre = listaPaises[i][0]
        if fs.contieneLetraNormalizada(nombre, letraBuscar):
            contador = contador + 1
        i = i + 1

    return contador
