# AVANCE 2 — Población, monedas y reportes

Cubre las opciones 3, 4, 5, 6 y 7 de la TP1 del "Sistema de formateo y análisis de datos de países y monedas".

La Opción 3 procesa población, área y densidad. La Opción 4 procesa las monedas y sus tasas. Las Opciones 5, 6 y 7 generan los reportes solicitados por la consigna.

---

## Estado del avance

| Commit | Nombre | Estado |
|---|---|---|
| 4 | `feat: implementar analisis poblacional y geografico` | Hecho y verificado |
| 5 | `feat: implementar procesamiento de monedas` | Hecho y verificado |
| 6 | `feat: generar reportes txt y html` | Hecho y verificado |


Confirmar con `git log --oneline` y `git status` que los commits estén registrados correctamente.

**Rama de trabajo:** `main`.

---

## Decisiones de diseño

- **Población:** los cálculos de total, promedio y mediana se realizan manualmente, respetando las restricciones de la consigna.
- **Clasificación de población:** se mantienen las categorías indicadas por el PDF: Megaciudad, Ciudad grande, Ciudad mediana y Ciudad pequeña.
- **Densidad:** se calcula a partir de población y área, y se permite obtener los 10 países con mayor y menor densidad.
- **Monedas:** se procesan los códigos, nombres y tasas de cambio sin diccionarios ni funciones automáticas prohibidas.
- **Reportes:** se mantienen como archivos TXT y HTML generados desde el programa de consola.
- **Restricciones:** no se utilizan diccionarios, `.replace()`, `.split()`, `sorted`, `min`, `max`, `sum`, `round`, cortes `[a:b]`, `for`, `lambda` ni comprensiones.
- **Modularización:** se reutilizan las funciones existentes de lectura, normalización y cálculo siempre que corresponde.
- **Validaciones:** los archivos con datos inválidos muestran advertencias y el programa continúa sin cerrarse.

---

## COMMIT 4

**Nombre:**

```text
feat: implementar analisis poblacional y geografico
```

### Prompt usado

```text
Implementa ahora la OPCIÓN 3 de la TP1.

Debe cargar los datos normalizados desde el archivo TOON y realizar manualmente:

POBLACIÓN:
- población total mundial
- población promedio
- mediana de población mediante ordenamiento manual
- clasificación:
  - Megaciudad: > 10,000,000
  - Ciudad grande: 1,000,000 - 10,000,000
  - Ciudad mediana: 100,000 - 999,999
  - Ciudad pequeña: < 100,000
- cantidad de países por categoría

ÁREA:
- área total
- densidad poblacional de cada país
- 10 países con mayor densidad
- 10 países con menor densidad

Restricciones:
- no usar diccionarios
- no usar .replace()
- no usar statistics
- no usar numpy
- no utilizar funciones automáticas para obtener mediana, promedio u ordenamientos
- realizar los procesos manualmente
- mantener la modularización mediante funciones

Revisa primero el código existente y reutiliza las funciones que ya existan.

No modifiques funcionalidades que no estén relacionadas con esta opción.

Prueba la opción completa antes de terminar y NO hagas commit automáticamente.
```

### Resultado verificado

- 25 países procesados.
- Población total: **4 411 741 600**.
- Mediana de población: **51 740 000**.
- 21 países clasificados como Megaciudad.
- 4 países clasificados como Ciudad grande.
- Cálculo de área y densidad funcionando.
- Cálculo de los países con mayor y menor densidad funcionando.

---

## COMMIT 5

**Nombre:**

```text
feat: implementar procesamiento de monedas
```

### Prompt usado

```text
Implementa ahora la OPCIÓN 4 de la TP1.

Debe procesar el archivo TOON de tasas de cambio.

Implementar:

STRINGS:
- extraer código de moneda de 3 letras
- extraer nombre completo
- normalizar nombres de monedas
- crear formato "CODIGO - Nombre"
- contar monedas que tengan exactamente N letras

OPERACIONES NUMÉRICAS:
- tasa de cambio promedio
- moneda más fuerte
- moneda más débil
- cantidad de monedas con tasa > 1 USD
- cantidad con tasa = 1 USD
- cantidad con tasa < 1 USD
- ordenar tasas ascendente
- ordenar tasas descendente

Restricciones obligatorias:
- no diccionarios
- no .replace()
- no statistics
- no numpy
- cálculos manuales
- procesamiento de strings carácter por carácter cuando corresponda

Reutiliza funciones existentes si son compatibles.

Antes de terminar:
1. Ejecuta pruebas.
2. Comprueba los resultados.
3. Revisa que no existan diccionarios.
4. Busca cualquier uso de .replace().
5. No rompas las opciones anteriores.
6. No hagas commit automáticamente.
```

### Resultado verificado

- 21 monedas procesadas.
- Tasa promedio: **393.5148**.
- 16 monedas con tasa mayor que 1.
- 2 monedas con tasa igual a 1.
- 3 monedas con tasa menor que 1.
- Procesamiento de códigos y nombres de monedas funcionando.
- Ordenamiento de tasas funcionando.

También se verificó la consulta de países por letra:

- Letra `"a"`: promedio **7**.
- Estados Unidos: **14**.
- Perú: **4**.
- Total: **20 países**.

---

## COMMIT 6

**Nombre:**

```text
feat: generar reportes txt y html
```

### Prompt usado

```text
Implementa las opciones 5, 6 y 7 de la TP1.

OPCIÓN 5:
Generar un reporte TXT de países con:
- nombre normalizado
- capital normalizada
- código ISO
- población
- área
- densidad
- categoría de población

Agregar al final:
- total de países
- población total
- área total
- promedio de población
- promedio de área

OPCIÓN 6:
Generar HTML "Reporte de Análisis de Monedas" con:
- título
- fecha y hora
- cantidad de monedas
- tasa promedio
- moneda más fuerte
- moneda más débil
- tabla con código
- nombre normalizado
- tasa con 4 decimales
- relación con USD
- tabla de clasificación con colores alternados y celdas centradas

OPCIÓN 7:
Generar HTML "Análisis de Densidad Poblacional Mundial" con:
- 10 países más densamente poblados
- 10 países menos densamente poblados
- gráfico de barras ASCII
- densidad promedio
- densidad máxima
- densidad mínima
- porcentaje de países por categoría

Restricciones:
- mantener el programa de consola
- no usar diccionarios
- no usar .replace()
- no usar numpy
- no usar statistics
- reutilizar las funciones existentes
- mantener el código modular
- no modificar main innecesariamente

Antes de terminar:
1. Probar las opciones 5, 6 y 7.
2. Comprobar que los archivos TXT y HTML se creen correctamente.
3. Revisar errores.
4. Revisar restricciones de la tarea.
5. NO hacer commit automáticamente.
```

### Resultado verificado

- El reporte TXT se genera correctamente.
- El reporte HTML de monedas se genera correctamente.
- El reporte HTML de densidad se genera correctamente.
- Los contenidos de los reportes coinciden con los resultados comprobados anteriormente.
- La Opción 7 genera los 10 países con mayor densidad, los 10 con menor densidad y el gráfico ASCII.

---

## Verificación antes del siguiente commit

```powershell
# Revisar usos prohibidos
Select-String -Path *.py -Pattern "\.replace\(|\.split\(|sorted\(|min\(|max\(|sum\(|round\(|for |lambda|enumerate|zip\("

# Revisar diccionarios
Select-String -Path *.py -Pattern "dict\("

# Revisar estado
git status

# Revisar commits
git log --oneline
```

---

## Verificación general

Se probó el programa completo y las **Opciones 1 a 7** mantienen los resultados esperados.

### Resultados principales

- 25 países.
- 21 monedas.
- Población total: **4 411 741 600**.
- Mediana: **51 740 000**.
- 21 Megaciudades.
- 4 Ciudades grandes.
- Tasa promedio: **393.5148**.
- 16 monedas con tasa > 1.
- 2 monedas con tasa = 1.
- 3 monedas con tasa < 1.

### Validaciones

Se probaron datos inválidos en CSV:

- población `"abc"`;
- área `-5`;
- columna adicional.

El programa muestra una advertencia con el número de línea, omite los datos inválidos y continúa con los registros válidos.

También se verificaron:

- CSV inexistente;
- CSV vacío;
- TOON corrupto;
- entrada inválida del menú;
- letra inválida;
- N inválido.

El TOON corrupto muestra `"No se encontraron datos válidos"` sin provocar que el programa se caiga.


### Estilo

Las funciones tienen docstrings y los encabezados del código ya no contienen residuos de prompts.

---

## Problemas encontrados y soluciones

| N.º | Problema | Solución |
|---|---|---|
| 1 | Los cálculos poblacionales debían hacerse manualmente | Se implementaron cálculos mediante las funciones del programa |
| 2 | La mediana no podía obtenerse mediante una función automática | Se realizó el ordenamiento manual |
| 3 | El criterio de moneda más fuerte generaba una diferencia con la interpretación inicial | Se documentó y verificó el criterio utilizado |
| 4 | El CSV con población `"abc"` provocaba un dato inválido | Se agregó validación y se omite la línea incorrecta |
| 5 | Un área negativa debía rechazarse | Se agregó validación del área |
| 6 | El uso de `round()` estaba prohibido | Se reemplazó por el procesamiento permitido |
| 7 | Los cortes de texto estaban prohibidos | Se reemplazaron por procesamiento carácter por carácter |
| 8 | Algunas funciones quedaron demasiado largas | Se identificaron para una posible refactorización posterior |

---

## Pendiente para los siguientes avances

- **Commit 7:** regenerar `reporte_densidad.html`, eliminar el comentario en inglés de `reportes.py`, revisar cambios y realizar el commit.
- **Modularización:** dividir, si hay tiempo, las funciones que superan las 40 líneas.
- **Opción 8:** implementar `bitacora.bin` con registros de fecha, hora y descripción.
- **Submenú de bitácora:** A) buscar por fecha, B) buscar por palabra clave, C) mostrar todas, D) exportar a CSV y E) salir.
- Registrar las acciones de las opciones 1 a 7 y los errores.
- Registrar en la Opción 1 el archivo consultado, cantidad de datos y tiempo de respuesta.
- **Opción 9:** registrar la salida antes de finalizar el programa.
- Documentación en `documentaciónCódigos.PDF`.
- Incluir en la documentación portada, índice, enunciado, olores de software, validaciones, estrategia de reportes, agendas, minutas, cronograma, problemas y soluciones, lecciones aprendidas y estadísticas de tiempos.
- Completar la carpeta final de documentación y programa fuente.

---

## Estado del AVANCE 2

| Parte | Estado |
|---|---|
| Opción 1 | Hecha |
| Opción 2 | Hecha |
| Opción 3 | Hecha y verificada |
| Opción 4 | Hecha y verificada |
| Opción 5 | Hecha y verificada |
| Opción 6 | Hecha y verificada |
| Opción 7 | Hecha y verificada |
| Opción 8 | Pendiente |
| Opción 9 | Pendiente de registrar salida |
|

**Estado general:** En progreso.


