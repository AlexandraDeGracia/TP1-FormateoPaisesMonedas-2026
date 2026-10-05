# AVANCE 1 — Carga y procesamiento de países

La primera parte debe cubrir la carga de datos y la normalización de nombres.

La consigna establece que la opción 1 debe cargar países desde CSV y guardarlos en TOON, y la opción 2 debe normalizar los nombres aplicando las transformaciones carácter por carácter.

---

## COMMIT 1

**Nombre:**

```text
feat: crear estructura base del proyecto
```

### Qué debe hacer Antigravity

Copia esto:

```text
Quiero comenzar el proyecto de la TP1 "Sistema de formateo y análisis de datos de países y monedas".

Antes de modificar cualquier archivo, revisa TODO el repositorio y dime:
1. Qué archivos existen.
2. Qué código existe actualmente.
3. Qué funcionalidades ya están implementadas.
4. Qué falta implementar.
5. Si existe algún error.

NO hagas cambios todavía.

La estructura debe ser compatible con la consigna:
- Python 3.10+
- Aplicación únicamente por consola.
- No usar diccionarios.
- No usar .replace().
- Los procesamientos de strings deben realizarse carácter por carácter.
- Los cálculos numéricos deben hacerse manualmente.
- El código debe estar modularizado mediante funciones.
- Mantener el menú preparado para las opciones 1 a 9.

Después de la revisión, propón una estructura sencilla de archivos para el proyecto.

IMPORTANTE:
No modifiques ningún archivo hasta que yo te indique que puedes hacerlo.
No trabajes sobre main si existe otra rama de trabajo.
```

Después de que revise, haces los cambios necesarios.

---

## COMMIT 2

**Nombre:**

```text
feat: implementar carga de datos de paises
```

### Prompt para Antigravity

```text
Ahora implementa únicamente la funcionalidad correspondiente a la OPCIÓN 1 de la TP1.

Requisitos:
- Leer los datos de países desde el archivo CSV indicado por el proyecto.
- Procesar los datos sin utilizar diccionarios.
- Guardar los datos crudos en un archivo TOON.
- Definir una estructura clara y sencilla para el archivo TOON.
- Mostrar:
  - cantidad de países cargados
  - 5 países con mayor población
  - 5 países con menor área
  - fecha de la tasa de cambio
  - cantidad de monedas descargadas
  - 5 monedas con mayor valor frente al USD
  - 5 monedas con menor valor frente al USD

Los ordenamientos y cálculos deben realizarse manualmente según las restricciones de la tarea.

NO uses:
- diccionarios
- .replace()
- numpy
- statistics
- otras librerías para hacer automáticamente los cálculos

Antes de modificar:
1. Revisa el código existente.
2. No rompas funcionalidades anteriores.
3. Mantén el menú existente.
4. Trabaja solamente en mi rama actual, nunca en main.

Al terminar:
- revisa los archivos modificados
- ejecuta pruebas
- verifica que la opción 1 funcione
- dime exactamente qué archivos modificaste
- NO hagas commit todavía.
```

La opción 1 está especificada en las páginas 15–16 de la consigna.

---

## COMMIT 3

**Nombre:**

```text
feat: implementar normalizacion de nombres de paises
```

### Prompt

```text
Implementa ahora únicamente la OPCIÓN 2 de la TP1.

La función debe cargar los países desde el archivo TOON y normalizar sus nombres.

Debes cumplir exactamente estas reglas:
1. Convertir a mayúsculas.
2. Eliminar espacios al inicio y al final.
3. Convertir manualmente:
   á à â ã ä å -> A
   é è ê ë -> E
   í ì î ï -> I
   ó ò ô õ ö -> O
   ú ù û ü -> U
   ñ -> N
   ç -> C
4. Eliminar manualmente:
   ' - `
5. Eliminar paréntesis y todo su contenido.
6. Detectar guiones bajos para dividir palabras compuestas.
7. Capitalizar correctamente cada palabra.

IMPORTANTE:
- NO utilizar .replace().
- NO utilizar diccionarios.
- El procesamiento debe hacerse carácter por carácter.
- No usar librerías automáticas para normalización.
- Mantener el código sencillo y apropiado para una estudiante de Taller de Programación.

Además debe calcular:
- longitud promedio de los nombres
- país con nombre más largo
- país con nombre más corto
- cantidad de países que contienen una letra indicada por el usuario

Guardar los datos normalizados en el archivo TOON correspondiente.

Antes de terminar:
- probar la funcionalidad
- revisar que no se haya usado .replace()
- revisar que no existan diccionarios
- verificar que el menú siga funcionando
- NO crear el commit automáticamente.
```

Eso cubre específicamente la normalización que exige la tarea.
