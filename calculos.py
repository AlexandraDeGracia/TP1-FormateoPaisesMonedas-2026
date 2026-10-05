"""
Módulo de Cálculos y Ordenamientos Manuales.
Estilo de código: Estudiante de primer año de programación.

RESTRICCIONES STRICTAS:
- Prohibido utilizar sorted(), min(), max(), sum() o .sort().
- Todo ordenamiento y cálculo numérico se realiza manualmente con ciclos while.
- Sin diccionarios.
"""

import formateo_strings as fs


def copiar_lista(lista_original):
    """Crea y retorna una copia de una lista usando un ciclo while."""
    copia = []
    i = 0
    cantidad = len(lista_original)
    while i < cantidad:
        copia.append(lista_original[i])
        i = i + 1
    return copia


def obtener_primeros_elementos(lista, cantidad):
    """
    Retorna los primeros 'cantidad' elementos de una lista
    recorriendo con un ciclo while.
    """
    resultado = []
    i = 0
    total = len(lista)
    while i < total and i < cantidad:
        resultado.append(lista[i])
        i = i + 1
    return resultado


def ordenar_paises_por_poblacion_descendente(lista_paises):
    """
    Ordena una lista de países por población (índice 3) de mayor a menor
    utilizando el algoritmo de ordenamiento por burbuja con ciclos while.
    """
    paises = copiar_lista(lista_paises)
    n = len(paises)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            poblacion_actual = paises[j][3]
            poblacion_siguiente = paises[j + 1][3]

            if poblacion_actual < poblacion_siguiente:
                aux = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = aux

            j = j + 1
        i = i + 1

    return paises


def ordenar_paises_por_area_ascendente(lista_paises):
    """
    Ordena una lista de países por área (índice 4) de menor a mayor
    utilizando el algoritmo de ordenamiento por burbuja con ciclos while.
    """
    paises = copiar_lista(lista_paises)
    n = len(paises)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            area_actual = paises[j][4]
            area_siguiente = paises[j + 1][4]

            if area_actual > area_siguiente:
                aux = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = aux

            j = j + 1
        i = i + 1

    return paises


def existe_moneda_en_lista(codigo_moneda, lista_monedas):
    """Verifica si un código de moneda ya existe en la lista de monedas procesadas."""
    i = 0
    total = len(lista_monedas)
    while i < total:
        if lista_monedas[i][0] == codigo_moneda:
            return True
        i = i + 1
    return False


def extraer_monedas_unicas(lista_paises):
    """
    Extrae las monedas únicas de la lista de países.
    Retorna una lista de tuplas: (codigo_moneda, nombre_moneda, tasa_usd)
    """
    monedas_unicas = []
    i = 0
    total_paises = len(lista_paises)

    while i < total_paises:
        p = lista_paises[i]
        moneda_nombre = p[5]
        codigo_moneda = p[6]
        tasa_usd = p[7]

        if not existe_moneda_en_lista(codigo_moneda, monedas_unicas):
            monedas_unicas.append((codigo_moneda, moneda_nombre, tasa_usd))

        i = i + 1

    return monedas_unicas


def ordenar_monedas_por_tasa(lista_monedas, descendente=True):
    """
    Ordena la lista de monedas según su tasa de cambio frente al USD (índice 2).

    CRITERIO DE TASA DE CAMBIO FRENTE AL USD:
    - La tasa indica cuántas unidades de esa moneda equivalen a 1 USD.
    - Tasa BAJA (ejemplo: CHF 0.85, EUR 0.91): La moneda vale MÁS frente al dólar (mayor valor).
    - Tasa ALTA (ejemplo: COP 4150, KRW 1335): La moneda vale MENOS frente al dólar (menor valor).
    """
    monedas = copiar_lista(lista_monedas)
    n = len(monedas)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            tasa_actual = monedas[j][2]
            tasa_siguiente = monedas[j + 1][2]

            intercambiar = False
            if descendente:
                if tasa_actual < tasa_siguiente:
                    intercambiar = True
            else:
                if tasa_actual > tasa_siguiente:
                    intercambiar = True

            if intercambiar:
                aux = monedas[j]
                monedas[j] = monedas[j + 1]
                monedas[j + 1] = aux

            j = j + 1
        i = i + 1

    return monedas


def calcular_longitud_promedio_nombres(lista_paises):
    """
    Calcula la longitud promedio de los nombres de los países como VALOR ENTERO
    utilizando una suma acumulada con un ciclo while y división entera (//).
    """
    cantidad = len(lista_paises)
    if cantidad == 0:
        return 0

    suma_longitudes = 0
    i = 0
    while i < cantidad:
        nombre = lista_paises[i][0]
        suma_longitudes = suma_longitudes + len(nombre)
        i = i + 1

    return suma_longitudes // cantidad


def obtener_pais_nombre_mas_largo(lista_paises):
    """
    Encuentra el país con el nombre más largo.
    Retorna la tupla (nombre, longitud). Si hay empate, retorna el primero encontrado.
    """
    cantidad = len(lista_paises)
    if cantidad == 0:
        return "", 0

    nombre_largo = lista_paises[0][0]
    max_len = len(nombre_largo)

    i = 1
    while i < cantidad:
        nombre_actual = lista_paises[i][0]
        len_actual = len(nombre_actual)
        if len_actual > max_len:
            nombre_largo = nombre_actual
            max_len = len_actual
        i = i + 1

    return nombre_largo, max_len


def obtener_pais_nombre_mas_corto(lista_paises):
    """
    Encuentra el país con el nombre más corto.
    Retorna la tupla (nombre, longitud). Si hay empate, retorna el primero encontrado.
    """
    cantidad = len(lista_paises)
    if cantidad == 0:
        return "", 0

    nombre_corto = lista_paises[0][0]
    min_len = len(nombre_corto)

    i = 1
    while i < cantidad:
        nombre_actual = lista_paises[i][0]
        len_actual = len(nombre_actual)
        if len_actual < min_len:
            nombre_corto = nombre_actual
            min_len = len_actual
        i = i + 1

    return nombre_corto, min_len


def contar_paises_con_letra(lista_paises, letra):
    """
    Cuenta cuántos países contienen la letra especificada (normalizada e insensible a mayúsculas/tildes).
    Cada país se cuenta a lo sumo UNA vez.
    """
    contador = 0
    i = 0
    cantidad = len(lista_paises)

    while i < cantidad:
        nombre = lista_paises[i][0]
        if fs.contiene_letra_normalizada(nombre, letra):
            contador = contador + 1
        i = i + 1

    return contador


def normalizar_datos_paises(lista_paises):
    """
    Normaliza el nombre, capital y moneda de cada país en la lista
    utilizando fs.normalizar_nombre y un ciclo while.
    """
    lista_normalizada = []
    i = 0
    cantidad = len(lista_paises)
    while i < cantidad:
        p = lista_paises[i]
        nombre_norm = fs.normalizar_nombre(p[0])
        capital_norm = fs.normalizar_nombre(p[1])
        moneda_norm = fs.normalizar_nombre(p[5])
        pais_norm = (nombre_norm, capital_norm, p[2], p[3], p[4], moneda_norm, p[6], p[7])
        lista_normalizada.append(pais_norm)
        i = i + 1
    return lista_normalizada


def calcular_poblacion_total(lista_paises):
    """Calcula la población total mundial sumando la población de cada país con un ciclo while."""
    total = 0
    i = 0
    cantidad = len(lista_paises)
    while i < cantidad:
        total = total + lista_paises[i][3]
        i = i + 1
    return total


def calcular_poblacion_promedio(lista_paises):
    """Calcula la población promedio por país utilizando un ciclo while."""
    cantidad = len(lista_paises)
    if cantidad == 0:
        return 0.0
    total = calcular_poblacion_total(lista_paises)
    return total / cantidad


def calcular_mediana_poblacion(lista_paises):
    """
    Calcula la mediana de población mediante ordenamiento manual (burbuja).
    Si la cantidad de países es impar, retorna el valor central.
    Si es par, retorna el promedio de los dos valores centrales.
    """
    cantidad = len(lista_paises)
    if cantidad == 0:
        return 0.0

    paises_ordenados = ordenar_paises_por_poblacion_descendente(lista_paises)

    if cantidad % 2 == 1:
        indice_central = cantidad // 2
        return float(paises_ordenados[indice_central][3])
    else:
        idx1 = (cantidad // 2) - 1
        idx2 = cantidad // 2
        val1 = paises_ordenados[idx1][3]
        val2 = paises_ordenados[idx2][3]
        return (val1 + val2) / 2.0


def clasificar_paises_por_poblacion(lista_paises):
    """
    Clasifica los países según su población en 4 categorías:
    - Megaciudad: > 10,000,000
    - Ciudad grande: 1,000,000 - 10,000,000
    - Ciudad mediana: 100,000 - 999,999
    - Ciudad pequeña: < 100,000
    Retorna una tupla: (megaciudades, grandes, medianas, pequenas)
    """
    megaciudades = 0
    grandes = 0
    medianas = 0
    pequenas = 0

    i = 0
    cantidad = len(lista_paises)
    while i < cantidad:
        pob = lista_paises[i][3]
        if pob > 10000000:
            megaciudades = megaciudades + 1
        elif pob >= 1000000:
            grandes = grandes + 1
        elif pob >= 100000:
            medianas = medianas + 1
        else:
            pequenas = pequenas + 1
        i = i + 1

    return megaciudades, grandes, medianas, pequenas


def calcular_area_total(lista_paises):
    """Calcula el área total acumulada de todos los países con un ciclo while."""
    total = 0
    i = 0
    cantidad = len(lista_paises)
    while i < cantidad:
        total = total + lista_paises[i][4]
        i = i + 1
    return total


def calcular_densidades_poblacionales(lista_paises):
    """
    Calcula la densidad poblacional (población / área) de cada país.
    Protege contra división por cero (área = 0).
    Retorna una lista de tuplas: (nombre, codigo, poblacion, area, densidad)
    """
    resultado = []
    i = 0
    cantidad = len(lista_paises)
    while i < cantidad:
        p = lista_paises[i]
        pob = p[3]
        area = p[4]
        if area > 0:
            densidad = pob / area
        else:
            densidad = 0.0
        resultado.append((p[0], p[2], pob, area, densidad))
        i = i + 1
    return resultado


def ordenar_paises_por_densidad(lista_densidades, descendente=True):
    """
    Ordena una lista de tuplas de densidad por el valor de densidad (índice 4)
    utilizando el algoritmo de ordenamiento por burbuja con ciclos while.
    """
    densidades = copiar_lista(lista_densidades)
    n = len(densidades)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            d_actual = densidades[j][4]
            d_siguiente = densidades[j + 1][4]

            intercambiar = False
            if descendente:
                if d_actual < d_siguiente:
                    intercambiar = True
            else:
                if d_actual > d_siguiente:
                    intercambiar = True

            if intercambiar:
                aux = densidades[j]
                densidades[j] = densidades[j + 1]
                densidades[j + 1] = aux

            j = j + 1
        i = i + 1

    return densidades


def calcular_tasa_promedio_monedas(lista_monedas):
    """Calcula la tasa de cambio promedio de una lista de monedas únicas."""
    cantidad = len(lista_monedas)
    if cantidad == 0:
        return 0.0

    suma_tasas = 0.0
    i = 0
    while i < cantidad:
        suma_tasas = suma_tasas + lista_monedas[i][2]
        i = i + 1

    return suma_tasas / cantidad


def obtener_moneda_mas_fuerte_opcion4(lista_monedas):
    """
    Obtiene la moneda con MAYOR tasa de cambio (moneda más fuerte según el criterio explícito de la Opción 4).
    NOTA CRÍTICA: La consigna de la Opción 4 define 'moneda más fuerte = mayor tasa'.
    Esto difiere del criterio de la Opción 1 donde una tasa menor significa mayor valor frente al USD.
    Retorna la tupla (codigo_moneda, nombre_moneda, tasa_usd).
    """
    cantidad = len(lista_monedas)
    if cantidad == 0:
        return None

    moneda_max = lista_monedas[0]
    max_tasa = moneda_max[2]

    i = 1
    while i < cantidad:
        m = lista_monedas[i]
        if m[2] > max_tasa:
            moneda_max = m
            max_tasa = m[2]
        i = i + 1

    return moneda_max


def obtener_moneda_mas_debil_opcion4(lista_monedas):
    """
    Obtiene la moneda con MENOR tasa de cambio (moneda más débil según el criterio explícito de la Opción 4).
    NOTA CRÍTICA: La consigna de la Opción 4 define 'moneda más débil = menor tasa'.
    Esto difiere del criterio de la Opción 1 donde una tasa mayor significa menor valor frente al USD.
    Retorna la tupla (codigo_moneda, nombre_moneda, tasa_usd).
    """
    cantidad = len(lista_monedas)
    if cantidad == 0:
        return None

    moneda_min = lista_monedas[0]
    min_tasa = moneda_min[2]

    i = 1
    while i < cantidad:
        m = lista_monedas[i]
        if m[2] < min_tasa:
            moneda_min = m
            min_tasa = m[2]
        i = i + 1

    return moneda_min


def clasificar_monedas_por_tasa(lista_monedas):
    """
    Clasifica las monedas según su tasa respecto a 1 USD:
    - Mayores a 1 USD (> 1)
    - Iguales a 1 USD (= 1)
    - Menores a 1 USD (< 1)
    Retorna una tupla: (mayores, iguales, menores)
    """
    mayores = 0
    iguales = 0
    menores = 0

    i = 0
    cantidad = len(lista_monedas)
    while i < cantidad:
        tasa = lista_monedas[i][2]
        if tasa > 1.0:
            mayores = mayores + 1
        elif tasa == 1.0:
            iguales = iguales + 1
        else:
            menores = menores + 1
        i = i + 1

    return mayores, iguales, menores


def contar_monedas_con_n_letras(lista_monedas, n_letras):
    """
    Cuenta cuántas monedas tienen exactamente n_letras en su nombre normalizado
    (sin contar espacios en blanco).
    """
    contador = 0
    i = 0
    cantidad = len(lista_monedas)

    while i < cantidad:
        nombre = lista_monedas[i][1]
        nombre_norm = fs.normalizar_nombre(nombre)
        letras = fs.contar_letras_sin_espacios(nombre_norm)
        if letras == n_letras:
            contador = contador + 1
        i = i + 1

    return contador


