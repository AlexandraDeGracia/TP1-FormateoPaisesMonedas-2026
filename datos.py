"""
Módulo de Datos (Estructura Base).
Almacenamiento de países y monedas mediante tuplas y listas (sin diccionarios).
"""

# Tupla de países: (código_iso, nombre_país, continente, población, superficie_km2, código_moneda)
PAISES = (
    ("ARG", "Argentina", "América del Sur", 45808747, 2780400, "ARS"),
    ("BRA", "Brasil", "América del Sur", 214326223, 8515767, "BRL"),
    ("CHL", "Chile", "América del Sur", 19493184, 756102, "CLP"),
    ("COL", "Colombia", "América del Sur", 51516562, 1141748, "COP"),
    ("ESP", "España", "Europa", 47415750, 505990, "EUR"),
    ("FRA", "Francia", "Europa", 67750000, 551695, "EUR"),
    ("JPN", "Japón", "Asia", 125507000, 377975, "JPY"),
    ("MEX", "México", "América del Norte", 126705138, 1964375, "MXN"),
    ("PAN", "Panamá", "América Central", 4351267, 75417, "PAB"),
    ("PER", "Perú", "América del Sur", 33715471, 1285216, "PEN"),
    ("USA", "Estados Unidos", "América del Norte", 331893745, 9833517, "USD"),
    ("URY", "Uruguay", "América del Sur", 3426260, 176215, "UYU"),
)

# Tupla de monedas: (código_moneda, nombre_moneda, símbolo, tasa_cambio_usd)
MONEDAS = (
    ("ARS", "Peso Argentino", "$", 975.50),
    ("BRL", "Real Brasileño", "R$", 5.45),
    ("CLP", "Peso Chileno", "$", 920.00),
    ("COP", "Peso Colombiano", "$", 4150.00),
    ("EUR", "Euro", "€", 0.91),
    ("JPY", "Yen Japonés", "¥", 148.20),
    ("MXN", "Peso Mexicano", "$", 19.30),
    ("PAB", "Balboa Panameño", "B/.", 1.00),
    ("PEN", "Sol Peruano", "S/.", 3.76),
    ("USD", "Dólar Estadounidense", "$", 1.00),
    ("UYU", "Peso Uruguayo", "$", 41.20),
)


def obtener_paises():
    """Retorna la tupla de países."""
    return PAISES


def obtener_monedas():
    """Retorna la tupla de monedas."""
    return MONEDAS


def buscar_moneda(codigo_moneda):
    """Firma base para buscar una moneda por su código."""
    pass


def buscar_pais(codigo_iso):
    """Firma base para buscar un país por su código ISO."""
    pass
