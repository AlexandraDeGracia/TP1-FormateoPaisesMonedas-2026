#Elaborado por: Alexandra De Gracia
#Fecha de Creación: 2026-10-05
#Fecha de última Modificación: 2026-10-14
"""
Módulo de Formateo Numérico y Representación Textual.
Proporciona funciones para formatear números flotantes y enteros con cantidad fija
de decimales evitando notación científica y utilizando operaciones aritméticas manuales.
"""


# Definición de función: formatearNDecimales
def formatearNDecimales(numero, decimales):
    """Formatea un número con N decimales exactos evitando notación científica."""
    if decimales < 0:
        decimales = 0

    signo = ""
    if numero < 0.0:
        signo = "-"
        numeroPositivo = -numero
    else:
        numeroPositivo = numero

    factor = 1.0
    i = 0
    while i < decimales:
        factor = factor * 10.0
        i = i + 1

    escalado = int(numeroPositivo * factor + 0.5)
    enteroFactor = int(factor)

    if enteroFactor > 0:
        parteEntera = escalado // enteroFactor
        parteDecimal = escalado % enteroFactor
    else:
        parteEntera = escalado
        parteDecimal = 0

    if decimales == 0:
        return signo + str(parteEntera)

    decStr = str(parteDecimal)
    while len(decStr) < decimales:
        decStr = "0" + decStr

    return signo + str(parteEntera) + "." + decStr


# Definición de función: formatear2Decimales
def formatear2Decimales(numero):
    """Formatea un número flotante con exactamente 2 decimales sin notación científica."""
    return formatearNDecimales(numero, 2)


# Definición de función: formatear4Decimales
def formatear4Decimales(numero):
    """Formatea un número flotante con exactamente 4 decimales sin notación científica."""
    return formatearNDecimales(numero, 4)


# Definición de función: formatearNumeroLimpio
def formatearNumeroLimpio(numero):
    """Formatea un número removiendo el '.0' si es entero o mostrando 2 decimales."""
    if numero == int(numero):
        return str(int(numero))
    return formatear2Decimales(numero)
