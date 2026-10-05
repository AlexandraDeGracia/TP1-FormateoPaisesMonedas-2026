"""
Módulo de Cálculos y Ordenamientos Manuales.
Estilo de código: Estudiante de primer año de programación.

RESTRICCIONES STRICTAS:
- Prohibido utilizar sorted(), min(), max(), sum() o .sort().
- Todo ordenamiento y cálculo numérico se realiza manualmente con ciclos while.
- Sin diccionarios.
"""


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
                # Intercambio manual
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
                # Intercambio manual
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

    Si descendente es True: Ordena de mayor a menor tasa (monedas de menor valor a mayor tasa).
    Si descendente es False: Ordena de menor a mayor tasa (monedas de mayor valor a menor tasa).
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
