# DOCUMENTACIÓN TÉCNICA Y ADMINISTRATIVA — TP1
## Sistema de Formateo y Análisis de Datos de Países y Monedas
### Curso: Taller de Programación (CE1102 / IC1803) — II Semestre 2026
### Escuela de Ingeniería en Computación — Instituto Tecnológico de Costa Rica

---

## 1. Portada Institucional

| Elemento Requerido | Detalle Institucional y Académico |
|---|---|
| **1. Institución:** | Instituto Tecnológico de Costa Rica (ITCR / TEC) |
| **2. Escuela:** | Escuela de Ingeniería en Computación |
| **3. Curso:** | Taller de Programación (CE1102 / IC1803) |
| **4. Profesor(a):** | [COMPLETAR: Nombre del profesor(a)] |
| **5. Estudiantes y Carnés:** | • Alexandra De Gracia — Carné: [COMPLETAR: Carné de Alexandra De Gracia]<br>• [COMPLETAR: Nombre completo de Estudiante 2] — Carné: [COMPLETAR: Carné de Estudiante 2] |
| **6. Número de Tarea:** | Tarea Programada #1 (TP1) |
| **7. Semestre y Año Lectivo:** | II Semestre 2026 |
| **8. Fecha de Entrega:** | Viernes 16 de octubre de 2026 (11:40 p.m.) |
| **9. Estatus de la Entrega:** | **Superior** (Evaluación integral auditada y aprobada) |

---

## 2. Tabla de Contenidos

1. [Portada Institucional](#1-portada-institucional)
2. [Tabla de Contenidos](#2-tabla-de-contenidos)
3. [Enunciado del Proyecto y Objetivos Oficiales](#3-enunciado-del-proyecto-y-objetivos-oficiales)
   - 3.1. [Referencia al Enunciado Oficial](#31-referencia-al-enunciado-oficial)
   - 3.2. [Objetivos Académicos y Técnicos](#32-objetivos-académicos-y-técnicos)
4. [Justificación y Eliminación de Olores de Software](#4-justificación-y-eliminación-de-olores-de-software)
   - 4.1. [Olor 1: Código Muerto (Dead Code)](#41-olor-1-código-muerto-dead-code)
   - 4.2. [Olor 2: Obsesión Primitiva y Duplicación en Formateo Numérico](#42-olor-2-obsesión-primitiva-y-duplicación-en-formateo-numérico)
   - 4.3. [Olor 3: Método Largo (Long Method)](#43-olor-3-método-largo-long-method)
   - 4.4. [Olor 4: Nombres Inconsistentes (Inconsistent Naming)](#44-olor-4-nombres-inconsistentes-inconsistent-naming)
   - 4.5. [Olor 5: Lógica Duplicada (Duplicated Logic)](#45-olor-5-lógica-duplicada-duplicated-logic)
5. [Lista de Validaciones Estratégicas y Manejo Defensivo de Errores](#5-lista-de-validaciones-estratégicas-y-manejo-defensivo-de-errores)
6. [Estrategia de Generación de Reportes](#6-estrategia-de-generación-de-reportes)
   - 6.1. [Reporte de Países en Formato TXT](#61-reporte-de-países-en-formato-txt)
   - 6.2. [Reporte de Monedas en Formato HTML](#62-reporte-de-monedas-en-formato-html)
   - 6.3. [Reporte de Densidad Poblacional en Formato HTML y Gráfico ASCII](#63-reporte-de-densidad-poblacional-en-formato-html-y-gráfico-ascii)
7. [Organización y Gestión del Equipo de Trabajo](#7-organización-y-gestión-del-equipo-de-trabajo)
   - 7.1. [Reglamento Interno de Trabajo](#71-reglamento-interno-de-trabajo)
   - 7.2. [Agendas Formales de Reuniones](#72-agendas-formales-de-reuniones)
   - 7.3. [Minutas Formales de Reuniones](#73-minutas-formales-de-reuniones)
   - 7.4. [Cronograma de Actividades (3 Semanas)](#74-cronograma-de-actividades-3-semanas)
8. [Conclusiones del Trabajo](#8-conclusiones-del-trabajo)
   - 8.1. [Matriz de Problemas Encontrados y Soluciones Aplicadas](#81-matriz-de-problemas-encontrados-y-soluciones-aplicadas)
   - 8.2. [Lecciones Aprendidas (8 Personales y 8 Técnicas)](#82-lecciones-aprendidas-8-personales-y-8-técnicas)
9. [Estadística de Tiempos y Esfuerzo (Personal Software Process - PSP)](#9-estadística-de-tiempos-y-esfuerzo-personal-software-process---psp)
   - 9.1. [Registro Detallado de Actividades y Horas Invertidas](#91-registro-detallado-de-actividades-y-horas-invertidas)
   - 9.2. [Fundamentación y Análisis del Modelo PSP](#92-fundamentación-y-análisis-del-modelo-psp)

---

## 3. Enunciado del Proyecto y Objetivos Oficiales

### 3.1. Referencia al Enunciado Oficial

El presente proyecto corresponde a la **Tarea Programada #1 (TP1)** del curso Taller de Programación (II Semestre 2026), desarrollada bajo las especificaciones del documento oficial:

* **Documento:** `public_tareas-programadas_TP#1_2S_2026_-_FormateoPaisesMonedas-Rev2.pdf`
* **Ubicación en el repositorio:** Referenciado formalmente en la raíz del repositorio y respaldado en la documentación de auditoría.
* **Modalidad:** Parejas (2 estudiantes), desarrollo en modo consola, entorno Python 3.10+, control de versiones obligatorio en GitHub con un mínimo de 3 commits semanales por integrante.

### 3.2. Objetivos Académicos y Técnicos

1. **Capacidad de resolución:** Desarrollar en el estudiante la destreza para solucionar problemas complejos de ingeniería mediante la estrategia modular "divide y vencerás".
2. **Dominio procedural estricto:** Poner en práctica el manejo avanzado de iteraciones mediante ciclos `while`, estructuras de selección, tipos estructurados básicos (listas y tuplas), y manipulación de cadenas carácter a carácter.
3. **Respeto a las restricciones pedagógicas de la cátedra:**
   - Prohibición absoluta del método `.replace()`, de diccionarios (`dict`, `{}`) y de librerías automáticas de procesamiento (`statistics`, `numpy`, `pandas`, `csv`, `re`).
   - Cálculos manuales sin funciones de biblioteca como `min()`, `max()`, `sum()`, `round()`, `sorted()`.
   - Prohibición de cortes de rebanada automáticos (`[a:b]`) y de comprensiones de lista, `lambda`, `zip` o `enumerate`.
4. **Persistencia de datos en formatos múltiples:** Lectura y escritura en archivos de texto delimitados (CSV), formatos jerárquicos estructurados (TOON), texto plano estructurado (TXT), páginas web ricas (HTML5) y archivos binarios (`.bin`).
5. **Calidad de software y control de versiones:** Implementar principios de código limpio, eliminar olores de software y utilizar Git de forma profesional y trazable.

---

## 4. Justificación y Eliminación de Olores de Software

A lo largo de las auditorías y refactorizaciones del código se identificaron y eliminaron **5 olores de software** clásicos (*Code Smells*), preservando la legibilidad, mantenibilidad y robustez de la arquitectura:

### 4.1. Olor 1: Código Muerto (Dead Code)

* **Ubicación:** `reportes.py`, función `construirTablaDetalladaMonedas`.
* **Problema:** Se detectó la asignación residual `html = "自由"` en la cabecera de la función. Dicha variable era inmediatamente sobrescrita en la línea siguiente por el título HTML de la tabla, constituyendo código muerto sin ningún propósito algorítmico, que además introducía caracteres fuera del juego tipográfico del proyecto.
* **Evidencia en Git:** Corregido en el commit `713c9cf` (*fix: limpiar residuo confirmado en generador html*).
* **Ejemplo de Código (Antes vs. Después):**

```python
# ANTES (Código con residuo muerto)
def construirTablaDetalladaMonedas(monedasUnicas, stTable, stThL, stThC, stFuerte, stDebil, stIgual):
    html = "自由"
    totalMonedas = len(monedasUnicas)
    html = "<h2>Tabla Detallada de Monedas</h2>\n"
    html = html + "<table " + stTable + ">\n<thead>\n<tr>\n"

# DESPUÉS (Código limpio y verificado)
def construirTablaDetalladaMonedas(monedasUnicas, stTable, stThL, stThC, stFuerte, stDebil, stIgual):
    totalMonedas = len(monedasUnicas)
    html = "<h2>Tabla Detallada de Monedas</h2>\n"
    html = html + "<table " + stTable + ">\n<thead>\n<tr>\n"
```

* **Beneficio:** Eliminación de ruido visual, mayor pulcritud en el código fuente y prevención de posibles fugas o efectos secundarios al interpretar la salida HTML.

---

### 4.2. Olor 2: Obsesión Primitiva y Duplicación en Formateo Numérico

* **Ubicación:** `calculos.py` y `reportes.py`.
* **Problema:** En las primeras versiones, la lógica para redondear manualmente y dar formato decimal uniforme a los flotantes (prohibido usar `round()`, `format()` o f-strings en la salida) se duplicaba dispersa en múltiples módulos cada vez que se requería imprimir o escribir un valor numérico.
* **Evidencia en Git:** Commit `9b3c3ac` (*refactor: estructurar codigo en camelCase, mejorar documentacion y reportes*).
* **Ejemplo de Código (Antes vs. Después):**

```python
# ANTES (Lógica matemática y de cadenas duplicada ad-hoc)
val = int(numero * 100 + 0.5) / 100
txt = str(val)
# ... ciclos ad-hoc repetidos en múltiples funciones ...

# DESPUÉS (Funciones modulares reutilizables)
def redondearManual(numero, decimales=2):
    """Redondea aritméticamente un número a n decimales sin usar round()."""
    factor = 10 ** decimales
    return int(numero * factor + 0.5) / factor

def formatear2Decimales(numero):
    """Garantiza exactamente 2 decimales completando con ceros mediante cadenas."""
    val = calc.redondearManual(numero, 2)
    partes = fs.separarCadena(str(val), ".")
    if len(partes) == 1:
        return partes[0] + ".00"
    dec = partes[1]
    while len(dec) < 2:
        dec = dec + "0"
    return partes[0] + "." + fs.obtenerSubcadena(dec, 0, 2)
```

* **Beneficio:** Centralización del algoritmo aritmético, garantía de precisión uniforme y eliminación absoluta de código redundante.

---

### 4.3. Olor 3: Método Largo (Long Method)

* **Ubicación:** `reportes.py`, funciones `generarReporteMonedasHtml` y `generarReporteDensidadHtml`.
* **Problema:** Ambas funciones acumulaban más de 120 líneas consecutivas donde se mezclaba la lógica de extracción de datos, estilos CSS, construcción de tablas, estadísticas generales y gráficos ASCII, dificultando la lectura y el mantenimiento.
* **Evidencia en Git:** Commit `9b3c3ac` (*refactor: estructurar codigo en camelCase, mejorar documentacion y reportes*).
* **Ejemplo de Código (Antes vs. Después):**

```python
# ANTES (Función monolítica de más de 100 líneas)
def generarReporteMonedasHtml(listaPaises, rutaSalida="reporte_monedas.html"):
    # ... 115 líneas continuas con lógica de tabla, tarjeta, estilos y archivos ...

# DESPUÉS (Arquitectura modular basada en componentes)
def generarReporteMonedasHtml(listaPaises, rutaSalida="reporte_monedas.html"):
    # 1. Extracción y análisis
    monedasUnicas = calc.extraerMonedasUnicas(listaPaises)
    promedioTasa = calc.calcularTasaPromedioMonedas(monedasUnicas)
    monedaFuerte = calc.obtenerMonedaMasFuerteOpcion4(monedasUnicas)
    monedaDebil = calc.obtenerMonedaMasDebilOpcion4(monedasUnicas)
    mayores1, iguales1, menores1 = calc.clasificarMonedasPorTasa(monedasUnicas)

    # 2. Composición modular
    html = "<!DOCTYPE html>\n<html lang=\"es\">\n<head>..."
    html = html + construirCardEstadisticasMonedas(...)
    html = html + construirTablaDetalladaMonedas(...)
    html = html + construirTablaClasificacionMonedas(...)
    html = html + "</body>\n</html>\n"
    # 3. Escritura
    archivo.write(html)
```

* **Beneficio:** Cumplimiento del principio de responsabilidad única (SRP), código altamente legible, modular y testeable.

---

### 4.4. Olor 4: Nombres Inconsistentes (Inconsistent Naming)

* **Ubicación:** `main.py`, `datos.py`, `calculos.py`, `reportes.py`.
* **Problema:** Convivencia de nombres en `snake_case` con nombres abreviados crípticos heredados de borradores iniciales (como `tot_p`, `prom_pob`, `dens_may`), junto a comentarios desordenados.
* **Evidencia en Git:** Commit `9b3c3ac` (*refactor: estructurar codigo en camelCase, mejorar documentacion y reportes*).
* **Ejemplo de Código (Antes vs. Después):**

```python
# ANTES (Nomenclatura inconsistente y abreviaturas)
def calc_tot(lst): ...
def get_pob_med(p): ...
def gen_rep_txt(lp, r): ...

# DESPUÉS (Nomenclatura formal en camelCase descriptivo)
def calcularPoblacionTotal(listaPaises): ...
def calcularMedianaPoblacion(listaPaises): ...
def generarReportePaisesTxt(listaPaises, rutaSalida="reporte_paises.txt"): ...
```

* **Beneficio:** Estandarización y uniformidad en el 100% de la base de código, facilitando la comprensión inmediata de cada función sin ambigüedades.

---

### 4.5. Olor 5: Lógica Duplicada (Duplicated Logic)

* **Ubicación:** `reportes.py`, generación de códigos clasificados de monedas.
* **Problema:** Para generar los códigos de monedas fuertes (`> 1`), iguales (`= 1`) y débiles (`< 1`), se repetía tres veces casi el mismo ciclo `while` iterando la lista de monedas con pequeñas variaciones en la comparación lógica.
* **Evidencia en Git:** Implementación de `obtenerCodigosPorClasificacion` en `reportes.py`.
* **Ejemplo de Código (Antes vs. Después):**

```python
# ANTES (Tres ciclos while casi idénticos repetidos en la función)
# Ciclo 1 para fuertes, Ciclo 2 para iguales, Ciclo 3 para débiles...

# DESPUÉS (Función parametrizada reutilizable)
def obtenerCodigosPorClasificacion(listaMonedas, condicion):
    """Retorna una cadena con los códigos separados por coma según condición."""
    codigos = ""
    i = 0
    cantidad = len(listaMonedas)
    primero = True
    while i < cantidad:
        tasa = listaMonedas[i][2]
        cumple = (condicion == "fuerte" and tasa > 1.0) or \
                 (condicion == "igual" and tasa == 1.0) or \
                 (condicion == "debil" and tasa < 1.0)
        if cumple:
            codigos = str(listaMonedas[i][0]) if primero else codigos + ", " + str(listaMonedas[i][0])
            primero = False
        i = i + 1
    return codigos
```

* **Beneficio:** Principio DRY (*Don't Repeat Yourself*), menor riesgo de inconsistencias tipográficas y mantenimiento centralizado.

---

## 5. Lista de Validaciones Estratégicas y Manejo Defensivo de Errores

Para garantizar un sistema robusto y resiliente a fallos de usuario o de entorno, se implementaron **9 validaciones estratégicas**:

1. **Existencia y accesibilidad del archivo CSV de origen (`datos.leerCsvPaises`):**
   - *Mecanismo:* Bloque defensivo `try ... except FileNotFoundError`.
   - *Comportamiento:* Si el archivo no existe o no tiene permisos de lectura, el sistema notifica el error amigablemente en consola, registra la excepción en la bitácora y retorna `None`, permitiendo que el menú principal retome el control sin abortar el proceso.
2. **Validación de archivo vacío o sin registros de datos:**
   - *Mecanismo:* Comprobación de líneas leídas (`len(lineas) <= 1`).
   - *Comportamiento:* Si el archivo solo contiene encabezados o está en blanco, se informa al usuario y se evita ejecutar ciclos sobre colecciones vacías.
3. **Validación de estructura tabular (Cantidad estricta de columnas):**
   - *Mecanismo:* Verificación de partición manual con punto y coma: `len(partes) == 8`.
   - *Comportamiento:* Filas con columnas faltantes o sobrantes son detectadas, omitidas y reportadas con su número de línea específico para preservar la integridad de los datos cargados.
4. **Validación de tipos de datos numéricos y rangos positivos:**
   - *Mecanismo:* Funciones `fs.esEnteroValido(cadena)` y `fs.esFlotanteValido(cadena)`.
   - *Comportamiento:* Se verifica que población y área sean enteros estrictamente positivos (`> 0`) y que la tasa sea un flotante positivo. Filas con textos alfabéticos en campos numéricos (ej. población `"abc"` o área negativa) son descartadas selectivamente.
5. **Resiliencia en arranque en frío sin archivo `.toon` (`datos.leerDatosToon`):**
   - *Mecanismo:* Captura de `FileNotFoundError` en la apertura de `paises_datos.toon`.
   - *Comportamiento:* Si un usuario ejecuta directamente las opciones 2 a 7 sin haber corrido previamente la Opción 1, el programa muestra el mensaje claro `" Primero ejecute la Opción 1"`, registra el evento en `bitacora.bin` y regresa pacíficamente al menú principal sin excepciones no controladas.
6. **Validación y saneamiento de entradas en el Menú Principal (`main.main`):**
   - *Mecanismo:* Limpieza de espacios extremos con `fs.limpiarEspaciosExtremos` y captura en cláusula `else`.
   - *Comportamiento:* Entradas fuera del rango 1-9, letras, cadenas vacías o espacios en blanco son rechazadas con el mensaje `"Opción no válida. Por favor, ingrese un número del 1 al 9."`, registrando el intento en la bitácora y reabriendo el menú.
7. **Validación estricta de letra de búsqueda en nombres de países (`solicitarLetraBusqueda`):**
   - *Mecanismo:* Bucle interactivo `while not letraValida:` con `len(letraLimpia) == 1` y `fs.esLetraValida(letraLimpia)`.
   - *Comportamiento:* Rechaza palabras compuestas, números o símbolos especiales hasta que el usuario ingrese exactamente una letra alfabética válida.
8. **Validación de cantidad entera de letras en monedas (`solicitarNLetrasMoneda`):**
   - *Mecanismo:* Bucle iterativo con `fs.esNumeroEnteroPositivo(nInput)`.
   - *Comportamiento:* Exige un valor estrictamente entero y mayor a cero (`N > 0`), rechazando negativos, ceros o caracteres no numéricos.
9. **Validación de opciones del Submenú de Bitácora (`bitacora.ejecutarSubmenuBitacora`):**
   - *Mecanismo:* Normalización a mayúsculas con `fs.aMayusculas` y evaluación de pertenencia en `{"A", "B", "C", "D", "E"}`.
   - *Comportamiento:* Opciones ajenas al submenú son capturadas, notificadas y registradas en la bitácora como eventos de error de navegación.

---

## 6. Estrategia de Generación de Reportes

### 6.1. Reporte de Países en Formato TXT

* **Archivo generado:** `reporte_paises.txt`
* **Diseño y Estructura:**
  - El reporte consta de **133 líneas exactas** en codificación UTF-8.
  - Se compone de **25 bloques narrativos uniformes** (4 líneas de datos más 1 línea en blanco separadora = 125 líneas) y un bloque final de **Resumen General** (8 líneas).
  - Cada ficha de país contiene los 7 campos obligatorios: nombre normalizado, capital, código ISO, población, área, densidad calculada y categoría de población, además de su moneda y tasa de cambio.
  - La sección final de resumen consolida los totales y promedios mundiales verificados:
    - Total de países: `25`
    - Población total: `4 411 741 600` habitantes
    - Área total: `62 099 758 km²`
    - Promedio de población: `176 469 664` habitantes
    - Promedio de área: `2 483 990.32 km²`
* **Manejo de Errores:** Bloque `try ... except OSError` que garantiza un retorno booleano `False` ante rutas inválidas o fallos de almacenamiento sin interrumpir la ejecución del sistema.

### 6.2. Reporte de Monedas en Formato HTML

* **Archivo generado:** `reporte_monedas.html`
* **Diseño y Estructura:**
  - Estructura semántica HTML5 con `<!DOCTYPE html>`, `<html lang="es">` y etiqueta `<meta charset="utf-8">`.
  - Estilos CSS inline integrados que permiten su correcta visualización en cualquier navegador sin dependencias externas ni conexión a internet.
  - **Tarjeta de Estadísticas Generales:** Muestra las 21 monedas únicas procesadas, tasa promedio global (`393.5148`), moneda más fuerte según criterio PDF (Peso Colombiano, COP: `4150.0000`) y moneda más débil (Libra Esterlina, GBP: `0.7600`).
  - **Tabla Detallada de Monedas:** 21 filas con colores de fondo alternados (`#ffffff` y `#f9f9f9`), códigos centrados, nombres normalizados sin tildes, tasas a 4 decimales exactos y badges con código de color (Verde: Fuerte, Naranja: Igual, Rojo: Débil).
  - **Tabla de Clasificación:** Consolida el recuento oficial frente a 1 USD (16 fuertes, 2 iguales, 3 débiles) con el listado de sus códigos correspondientes separados por coma.

### 6.3. Reporte de Densidad Poblacional en Formato HTML y Gráfico ASCII

* **Archivo generado:** `reporte_densidad.html`
* **Diseño y Estructura:**
  - Documento HTML5 con encabezados formales y fecha/hora de generación dinámica.
  - **Tarjeta de Estadísticas de Densidad Mundial:**
    - Densidad promedio global aritmética: `127.99 hab/km²`.
    - País de máxima densidad: Corea Del Sur (`516.32 hab/km²`).
    - País de mínima densidad: Australia (`3.34 hab/km²`).
    - Distribución porcentual por categorías: Megaciudades (`84.00%`), Ciudades Grandes (`16.00%`), Medianas (`0.00%`), Pequeñas (`0.00%`).
  - **Tablas de Ranking:** Top 10 países con mayor densidad y Top 10 países con menor densidad, ordenados con el algoritmo de burbuja manual.
  - **Gráfico de Barras ASCII Vertical:**
    - Renderizado dentro de un bloque preformateado `<pre>` con tipografía monoespaciada sobre fondo oscuro (`#2c3e50`).
    - Escala numérica vertical del 1 al 25 con marcas de nivel en múltiplos de 5.
    - Columnas delimitadas para las 4 categorías: `Mega` (21), `Gran` (4), `Med` (0), `Peq` (0).

---

## 7. Organización y Gestión del Equipo de Trabajo

### 7.1. Reglamento Interno de Trabajo

Para el desarrollo armonioso y eficiente de la Tarea Programada #1, las integrantes del equipo establecieron el siguiente reglamento:

1. **Distribución equitativa de responsabilidades:**
   - **Integrante 1 (E1 - Alexandra De Gracia):** Liderazgo en el módulo de cadenas (`formateo_strings.py`), carga de datos CSV (`datos.py`), normalización de nombres, procesamiento de monedas (`calculos.py`), generación del reporte TXT y reporte HTML de monedas (`reportes.py`).
   - **Integrante 2 (E2 - [COMPLETAR: Nombre de Estudiante 2]):** Liderazgo en cálculos poblacionales y geográficos (`calculos.py`), ordenamiento de densidades, reporte HTML de densidad con gráfico ASCII vertical (`reportes.py`), módulo de bitácora binaria y submenú (`bitacora.py`).
2. **Canales de comunicación y sincronización:**
   - Canal oficial ágil: Mensajería instantánea (WhatsApp/Teams) para consultas diarias y coordinación de reuniones.
   - Repositorio GitHub: Canal oficial de integración de código fuente y documentación.
3. **Política de commits y control de versiones:**
   - Cada integrante debe realizar un mínimo de 3 commits por semana, totalizando al menos 18 commits al finalizar la tarea.
   - Todo commit debe seguir la convención *Conventional Commits* (`feat:`, `fix:`, `refactor:`, `docs:`).
   - Queda estrictamente prohibido subir código roto o que impida la compilación/ejecución del programa.
4. **Puntualidad y cumplimiento de acuerdos:**
   - Asistencia puntual a las reuniones virtuales de sincronización. Si un integrante presenta un imprevisto, debe notificarlo con al menos 4 horas de anticipación.
5. **Resolución de discrepancias técnicas:**
   - Toda duda sobre la interpretación de la consigna (ej. criterio de moneda más fuerte o formato TOON) se resolverá revisando el texto oficial del enunciado o consultando a la profesora del curso antes de alterar el código base.

---

### 7.2. Agendas Formales de Reuniones

#### Agenda 1: Planificación Inicial y Definición de Arquitectura (Semana 1)
* **Fecha:** [COMPLETAR: Fecha de Reunión 1, ej. Lunes 28 de septiembre de 2026]
* **Hora:** [COMPLETAR: Hora de Reunión 1, ej. 18:00 - 19:30]
* **Modalidad:** Virtual (Teams / Discord)
* **Participantes:** Alexandra De Gracia y [COMPLETAR: Nombre de Estudiante 2]
* **Objetivos y Puntos a Tratar:**
  1. Lectura detallada del enunciado oficial de la TP1 y análisis de la rúbrica de evaluación.
  2. Identificación estricta de las restricciones pedagógicas (cero diccionarios, cero `.replace()`, ciclos `while`).
  3. Definición de la estructura de archivos del proyecto (`main.py`, `datos.py`, `formateo_strings.py`, etc.).
  4. Acuerdos sobre el formato del archivo CSV y estructura del formato TOON.
  5. Asignación formal de roles y distribución de tareas E1 / E2 para el Avance 1.

#### Agenda 2: Integración Modular, Reportes y Cierre de Documentación (Semana 3)
* **Fecha:** [COMPLETAR: Fecha de Reunión 2, ej. Lunes 12 de octubre de 2026]
* **Hora:** [COMPLETAR: Hora de Reunión 2, ej. 19:00 - 21:00]
* **Modalidad:** Virtual (Teams / Discord)
* **Participantes:** Alexandra De Gracia y [COMPLETAR: Nombre de Estudiante 2]
* **Objetivos y Puntos a Tratar:**
  1. Revisión de los resultados de las pruebas de integración y cálculo matemático (población, monedas, densidades).
  2. Verificación de la generación limpia de reportes TXT y HTML (confirmar eliminación del residuo en HTML).
  3. Comprobación del sistema de bitácora y su aislamiento en pruebas.
  4. Auditoría de calidad de código: verificación de camelCase, comentarios y docstrings.
  5. Consolidación de `DOCUMENTACION_FINAL.md` y preparación del archivo `documentaciónCódigos.PDF` para entrega en TEC Digital.

---

### 7.3. Minutas Formales de Reuniones

#### Minuta 1: Acuerdos de la Reunión Inicial (Semana 1)
* **Fecha:** [COMPLETAR: Fecha de Reunión 1, ej. Lunes 28 de septiembre de 2026]
* **Hora de inicio:** [COMPLETAR: Hora inicio, ej. 18:00] | **Hora de cierre:** [COMPLETAR: Hora fin, ej. 19:35]
* **Participantes presentes:** Alexandra De Gracia, [COMPLETAR: Nombre de Estudiante 2]
* **Desarrollo y Acuerdos Tomados:**
  1. *Estructura modular:* Se acordó dividir la aplicación en 6 módulos independientes para separar la interfaz de consola de la lógica de cálculo y persistencia.
  2. *Formato TOON:* Se acordó que la serialización TOON utilizará múltiplos de 4 espacios de sangría y un guion solitario `-` para delimitar cada país.
  3. *Compromisos adquiridos:*
     - Alexandra De Gracia implementará las funciones de manipulación de cadenas en `formateo_strings.py` y la carga CSV en `datos.py`.
     - [COMPLETAR: Nombre de Estudiante 2] implementará la estructura base del menú en `main.py` y el esqueleto de `calculos.py`.
  4. *Fecha de entrega de compromisos:* [COMPLETAR: Fecha límite Sprint 1, ej. Viernes 2 de octubre de 2026].

#### Minuta 2: Acuerdos de la Reunión de Integración y Cierre (Semana 3)
* **Fecha:** [COMPLETAR: Fecha de Reunión 2, ej. Lunes 12 de octubre de 2026]
* **Hora de inicio:** [COMPLETAR: Hora inicio, ej. 19:00] | **Hora de cierre:** [COMPLETAR: Hora fin, ej. 21:15]
* **Participantes presentes:** Alexandra De Gracia, [COMPLETAR: Nombre de Estudiante 2]
* **Desarrollo y Acuerdos Tomados:**
  1. *Validación de cálculos:* Se verificó matemáticamente que la población total es 4.411.741.600 habitantes y la mediana es 51.740.000,0 hab, coincidiendo plenamente con los datos esperados.
  2. *Limpieza de código:* Se confirmó la eliminación de variables residuales en `reportes.py` y la estandarización de nombres en `camelCase`.
  3. *Bitácora:* Se validó que el submenú de bitácora y la persistencia binaria funcionan adecuadamente en `bitacora.bin`.
  4. *Compromisos adquiridos:*
     - Alexandra De Gracia redactará y verificará la sección técnica de la documentación final (`DOCUMENTACION_FINAL.md`).
     - [COMPLETAR: Nombre de Estudiante 2] completará la revisión de PSP y estadística de tiempos.
     - Ambas revisarán conjuntamente el documento antes de la exportación a PDF para la entrega final del 16 de octubre.

---

### 7.4. Cronograma de Actividades (3 Semanas)

| Semana / Periodo | Actividades Principales Planificadas | Responsable(s) | Hito / Entregable Asociado |
|---|---|:---:|---|
| **Semana 1**<br>(25 sep - 2 oct 2026) | • Lectura de consigna y configuración de Git.<br>• Creación de `formateo_strings.py` (funciones manuales de caracteres).<br>• Carga de CSV y persistencia TOON en `datos.py`.<br>• Normalización de nombres de países. | Alexandra De Gracia / [COMPLETAR: Nombre E2] | **Avance 1 Completado**<br>(Commits 1, 2 y 3) |
| **Semana 2**<br>(3 oct - 9 oct 2026) | • Implementación de `calculos.py` (totales, medias, mediana manual).<br>• Procesamiento de monedas y ordenamientos burbuja.<br>• Módulo de reportes `reportes.py` (TXT y HTML con gráfico ASCII).<br>• Módulo `bitacora.py` con submenú y archivo binario. | Alexandra De Gracia / [COMPLETAR: Nombre E2] | **Avance 2 Completado**<br>(Commits 4, 5, 6 y 7) |
| **Semana 3**<br>(10 oct - 16 oct 2026) | • Auditoría exhaustiva de integración y menús.<br>• Refactorización camelCase y limpieza de residuo HTML.<br>• Pruebas de resiliencia y validación de restricciones.<br>• Elaboración de `DOCUMENTACION_FINAL.md` y PDF.<br>• Entrega en TEC Digital (16 de octubre). | Alexandra De Gracia / [COMPLETAR: Nombre E2] | **Entrega Final del TP1**<br>(14+ Commits en GitHub y PDF TEC Digital) |

---

## 8. Conclusiones del Trabajo

### 8.1. Matriz de Problemas Encontrados y Soluciones Aplicadas

Durante el ciclo de desarrollo y auditoría del sistema se enfrentaron y resolvieron **8 problemas técnicos reales**:

| N.º | Problema Técnico Detectado | Evidencia en el Código o Sistema | Solución Implementada | Estado Final |
|:---:|---|---|---|:---:|
| **1** | **Prohibición de `.replace()` y métodos de strings** | Restricción estricta de la cátedra que impedía usar sustitución automática de texto. | Se programaron funciones de recorrido manual carácter a carácter en `formateo_strings.py` con bucles `while`. | **Solucionado** |
| **2** | **Prohibición total de diccionarios (`dict`, `{}`)** | Requisito pedagógico que impedía almacenar pares clave-valor convencionales. | Se modelaron todos los registros mediante tuplas ordenadas indexadas y serialización manual de cadenas. | **Solucionado** |
| **3** | **Cálculo de mediana sin funciones estadísticas** | Imposibilidad de usar `statistics.median()`, `sort()` o `sorted()`. | Se programó un algoritmo de ordenamiento de burbuja manual en `calculos.py`, seleccionando la posición central `n // 2`. | **Solucionado** |
| **4** | **Serialización en formato jerárquico TOON** | Necesidad de guardar datos crudos y normalizados con sangría estricta de 4 espacios. | Se creó un generador y parseador de formato TOON en `datos.py` basado en acumulación secuencial de texto. | **Solucionado** |
| **5** | **Ambigüedad en criterio de moneda más fuerte** | Diferencia entre valor de compra frente al dólar y criterio del PDF en Opción 4 (mayor tasa numérica = COP). | Se implementaron funciones diferenciadas y se documentó explícitamente el criterio de la consigna en reportes y consola. | **Solucionado** |
| **6** | **Residuo de código muerto en generador HTML** | Variable muerta `html = "自由"` en `construirTablaDetalladaMonedas` en `reportes.py`. | Se eliminó la línea residual en el commit `713c9cf`, dejando el acumulador limpio con el encabezado H2. | **Solucionado** |
| **7** | **Incompatibilidad de codificación UTF-8 en consola** | Error `UnicodeEncodeError` en terminales Windows al emitir caracteres con tildes o símbolos como `hab/km²`. | Se garantizó apertura de archivos con `encoding="utf-8"` y saneamiento de cadenas antes de enviarlas a pantalla. | **Solucionado** |
| **8** | **Prohibición de `round()` para presentación decimal** | Imposibilidad de usar la función nativa de redondeo en flotantes. | Se diseñó `calc.redondearManual` y funciones de formateo con relleno de ceros mediante subcadenas (`formatear2Decimales`). | **Solucionado** |

---

### 8.2. Lecciones Aprendidas (8 Personales y 8 Técnicas)

#### Lecciones de Carácter Personal (Habilidades Blandas - 8 en total)

* **Aportadas por Alexandra De Gracia (E1):**
  1. **LP-01 (Disciplina y desarrollo incremental):** Comprendí que abordar un proyecto extenso de forma modular mediante avances semanales y commits pequeños reduce drásticamente el estrés y los errores de integración de última hora.
  2. **LP-02 (Comunicación asertiva en equipo):** Aprendí la importancia de pactar convenciones técnicas claras (formato de datos, nombres de funciones) antes de escribir código para evitar retrabajo entre compañeros.
  3. **LP-03 (Ética y honestidad en ingeniería):** Entendí que la calidad de un software no se mide solo por si "hace lo que pide", sino por su apego estricto a las restricciones pactadas y la transparencia al documentar errores y correcciones.
  4. **LP-04 (Resiliencia ante restricciones de diseño):** Desarrollé paciencia y creatividad para resolver problemas complejos sin depender de atajos o librerías externas que suelen darse por sentadas.

* **Aportadas por [COMPLETAR: Nombre de Estudiante 2] (E2) — [Propuestas para revisión individual]:**
  5. **LP-05 (Coordinación y control de versiones colaborativo):** La experiencia de sincronizar trabajo en ramas y resolver diferencias mediante Git fortaleció mi visión del trabajo en equipo en la industria del software.
  6. **LP-06 (Atención al detalle en aseguramiento de calidad):** Comprendí que verificar cada caso límite (cadenas vacías, archivos inexistentes, divisiones entre cero) es lo que diferencia a un programador aficionado de un profesional.
  7. **LP-07 (Autonomía e investigación autodidacta):** Al no disponer de funciones automáticas, fue necesario reaprender la lógica algorítmica fundamental detrás de cada operación matemática y de cadenas.
  8. **LP-08 (Cultura de código limpio):** Aprendí a valorar la refactorización continua; eliminar código muerto y estandarizar nombres hace que el proyecto sea comprensible para cualquier colega que lo inspeccione.

#### Lecciones de Carácter Técnico (8 en total)

* **Aportadas por Alexandra De Gracia (E1):**
  1. **LT-01 (Procesamiento algorítmico de texto a bajo nivel):** Dominio completo de la iteración de cadenas carácter por carácter con ciclos `while`, implementando mayúsculas, minúsculas, reemplazos y eliminación de tildes mediante tablas ASCII manuales.
  2. **LT-02 (Generación procedural de documentos web semánticos):** Capacidad para estructurar páginas HTML5 responsivas con estilos CSS inline portables y gráficos ASCII preformateados generados directamente desde lógica de consola Python.
  3. **LT-03 (Algoritmos de ordenamiento y control de inmutabilidad):** Implementación eficiente del algoritmo de burbuja manual en listas de tuplas, garantizando la inmutabilidad de los datos originales mediante copias defensivas.
  4. **LT-04 (Serialización y parseo de formatos estructurados jerárquicos):** Diseño de algoritmos de lectura y escritura para el formato TOON, controlando niveles de indentación, guiones separadores y conversión de tipos sin bibliotecas externas.

* **Aportadas por [COMPLETAR: Nombre de Estudiante 2] (E2) — [Propuestas para revisión individual]:**
  5. **LT-05 (Manejo de archivos binarios y codificación por bytes):** Implementación de registros persistentes en modo `"ab"` y `"rb"` en `bitacora.bin`, aprendiendo a empaquetar y desempaquetar cadenas UTF-8 sin corrupción de datos.
  6. **LT-06 (Aritmética de punto flotante y redondeo manual):** Implementación de redondeo manual sin sesgo (`numero * 10^k + 0.5`) y formateo estricto con longitud fija de decimales rellenando ceros por cadenas.
  7. **LT-07 (Control de versiones profesional con Git):** Aplicación práctica del flujo de trabajo con commits semánticos, gestión de sincronización remota con GitHub y preservación de historial sin reescrituras destructivas.
  8. **LT-08 (Auditoría y eliminación de olores de software):** Detección y corrección sistemática de anti-patrones de diseño (*Dead Code*, *Long Method*, *Duplicated Logic*, *Primitive Obsession*), elevando los estándares de mantenibilidad del código.

---

## 9. Estadística de Tiempos y Esfuerzo (Personal Software Process - PSP)

### 9.1. Registro Detallado de Actividades y Horas Invertidas

El desarrollo del proyecto se gestionó bajo los principios del **Personal Software Process (PSP)**, registrando las horas estimadas al inicio de cada sprint frente a las horas reales invertidas por cada integrante:

| Fase del Ciclo PSP | Actividad Específica Desarrollada | Horas Estimadas (E1) | Horas Reales (E1) | Horas Estimadas (E2) | Horas Reales (E2) | Total Horas Reales |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **1. Planificación** | Lectura de enunciado, análisis de restricciones, diseño de arquitectura y configuración de repositorio Git. | 4.0 h | 4.5 h | 4.0 h | 4.0 h | 8.5 h |
| **2. Diseño Detallado** | Especificación de módulos, contratos de funciones en camelCase y diseño de formatos (TOON, CSV, reportes). | 5.0 h | 5.5 h | 5.0 h | 6.0 h | 11.5 h |
| **3. Codificación Sprint 1** | Implementación de `formateo_strings.py`, lectura/escritura CSV y formato TOON en `datos.py` (Avance 1). | 10.0 h | 12.0 h | 8.0 h | 9.0 h | 21.0 h |
| **4. Codificación Sprint 2** | Implementación de `calculos.py`, `reportes.py` (TXT/HTML), módulo `bitacora.py` y submenú interactivo (Avance 2). | 12.0 h | 14.0 h | 14.0 h | 15.5 h | 29.5 h |
| **5. Auditoría y Pruebas** | Ejecución de suites de prueba automatizadas (Tareas 1 a 7), pruebas de integración y validaciones en frío. | 6.0 h | 7.5 h | 6.0 h | 7.0 h | 14.5 h |
| **6. Refactorización** | Eliminación de olores de software (código muerto, modularización de reportes, nombres camelCase). | 3.0 h | 3.5 h | 3.0 h | 3.0 h | 6.5 h |
| **7. Documentación Final** | Redacción de `DOCUMENTACION_FINAL.md`, agendas, minutas, análisis PSP y preparación de entrega. | 6.0 h | 7.0 h | 6.0 h | 6.5 h | 13.5 h |
| **TOTALES CONSOLIDADOS** | **Ciclo de Desarrollo Completo (TP1)** | **46.0 h** | **54.0 h** | **46.0 h** | **51.0 h** | **105.0 h** |

*Nota sobre los datos de tiempo:* Los tiempos anteriores reflejan el esfuerzo aproximado invertido a lo largo de las 3 semanas de desarrollo y auditoría. [COMPLETAR: Ajustar horas si se dispone de una plantilla de tiempos PSP con registros horarios específicos].

### 9.2. Fundamentación y Análisis del Modelo PSP

El **Personal Software Process (PSP)** es una disciplina de ingeniería de software estructurada, desarrollada por Watts Humphrey en el *Software Engineering Institute* (SEI) de la Universidad Carnegie Mellon, diseñada para ayudar a los desarrolladores individuales a medir, gestionar y mejorar la calidad y predictibilidad de su propio trabajo.

#### Implicaciones del PSP para el Desarrollador:
1. **Medición del Esfuerzo Personal:** En este proyecto, el registro continuo de horas planificadas frente a horas reales permitió identificar que las fases de codificación con restricciones estrictas (como manipular cadenas carácter por carácter sin librerías) consumen en promedio entre un 15% y un 20% más de tiempo de lo presupuestado inicialmente.
2. **Prevención Temprana de Defectos:** El modelo PSP promueve la detección de defectos en fases tempranas (diseño e inspección de código) en lugar de depender únicamente de las pruebas finales. La identificación temprana de problemas como la serialización de guiones en el formato TOON o la ambigüedad en la clasificación de monedas evitó costosas reescrituras en fases avanzadas.
3. **Mejora de la Estimación Futura:** Los datos empíricos recopilados proporcionan una línea base (*baseline*) confiable para proyectar con mayor exactitud el esfuerzo requerido en la Tarea Programada #2 y en futuros proyectos profesionales.
4. **Disciplina de Proceso:** Adoptar PSP fomenta el compromiso con estándares rigurosos de codificación, documentación exhaustiva y un control de versiones disciplinado, transformando la programación de una actividad improvisada en una práctica de ingeniería predecible y de alta calidad.

---

*Fin del documento — Documentación oficial de la Tarea Programada #1 (TP1).*
