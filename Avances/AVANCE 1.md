# AVANCE 1 — Carga y procesamiento de países

Cubre la carga de datos (Opción 1) y la normalización de nombres (Opción 2) de la TP1
"Sistema de formateo y análisis de datos de países y monedas" (Taller de Programación, II Semestre 2026).

La Opción 1 carga países desde un CSV y guarda los datos crudos en TOON. La Opción 2 normaliza los
nombres aplicando las transformaciones carácter por carácter (consigna, páginas 16 y 17).

---

## Estado del avance

| Commit | Nombre | Estado |
|---|---|---|
| 1 | `feat: crear estructura base del proyecto` | Hecho (corregido dentro del commit 2) |
| 2 | `feat: implementar carga de datos de paises` | Hecho y verificado |
| 3 | `feat: implementar normalizacion de nombres de paises` | Hecho y verificado |

Confirmar con `git log --oneline -5` y `git status` que los tres commits están en `origin/main`.

**Rama de trabajo:** `main` (el repositorio se creó como `master` y se renombró con `git branch -M main`).

---

## Decisiones de diseño

- **Formato del CSV:** separador `;`, encabezado
  `Nombre;Capital;Codigo;Poblacion;Area;Moneda;CodigoMoneda;TasaCambioUSD`, código ISO de **2 letras**
  (como el ejemplo del PDF). El archivo `paises.csv` tiene 25 países.
- **Formato TOON:** indentación en múltiplos de 4 espacios; el `-` va solo en su línea (4 espacios) y los
  campos de cada país van debajo (8 espacios); textos entre comillas dobles y números sin comillas.

  ```text
  paises:
      -
          nombre: "Argentina"
          capital: "Buenos Aires"
          codigo: "AR"
          poblacion: 45808747
          area: 2780400
          moneda: "Peso Argentino"
          codigo_moneda: "ARS"
          tasa_usd: 975.5
  ```
- **Criterio "mayor / menor valor frente al USD":** la tasa indica cuántas unidades de la moneda equivalen
  a 1 USD. Tasa baja = la moneda vale más (EUR 0.91). Tasa alta = vale menos (COP 4150). Está documentado en
  `main.py` y `calculos.py`. La consigna usa "mayor tasa = más fuerte" en la Opción 4, por lo que hay que
  confirmar el criterio con la profesora.
- **Fecha de la tasa:** el CSV no trae fecha, se usa la fecha del sistema.
- **Guiones bajos (regla 6):** cada `_` se convierte en un espacio.
- **Opción 2 sobrescribe el `.toon`** con los nombres normalizados (como pide la consigna). Para recuperar
  los datos crudos se ejecuta la Opción 1 de nuevo.
- **Estructura de módulos:** `main.py` (menú), `datos.py` (archivos CSV y TOON), `formateo_strings.py`
  (strings), `calculos.py` (cálculos numéricos).

---

## COMMIT 1

**Nombre:**

```text
feat: crear estructura base del proyecto
```

### Prompt usado

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
```

### Lo que pasó realmente

El commit 1 dejó un menú que **no seguía la consigna** (listar países, convertir monto, buscar país...,
con salida en `0`) y datos hardcodeados en tuplas con códigos de 3 letras. El menú de la sección 5 del PDF es:

1. Descargar datos de países (CSV)
2. Procesar y normalizar nombres de países
3. Procesar datos poblacionales y geográficos
4. Procesar datos de monedas
5. Generar reporte de países en TXT
6. Generar reporte de monedas en HTML
7. Generar reporte de densidad poblacional en HTML
8. Submenú de bitácora del sistema
9. Salir

Esto se corrigió dentro del commit 2.

---

## COMMIT 2

**Nombre:**

```text
feat: implementar carga de datos de paises
```

### Prompt usado (versión final)

```text
Trabaja en la rama main. No crees ni cambies de rama. NO hagas commit ni push.

Implementa únicamente la OPCIÓN 1 de la TP1 (consigna, página 16).

- Alinear el menú con la sección 5 de la consigna (opciones 2 a 8 muestran "en desarrollo", 9 sale).
- Leer paises.csv (separador ";", encabezado Nombre;Capital;Codigo;Poblacion;Area;Moneda;CodigoMoneda;TasaCambioUSD),
  separando cada línea carácter por carácter.
- Guardar los datos crudos en paises_datos.toon (indentación en múltiplos de 4 espacios, listas con guiones).
- Mostrar: cantidad de países cargados, 5 países con mayor población, 5 países con menor área, fecha de la
  tasa de cambio, cantidad de monedas, top 5 monedas con mayor y con menor valor frente al USD.
- Si el archivo no existe, mostrar un mensaje claro y volver al menú sin cerrarse.
- Códigos ISO de 2 letras, UTF-8 en todos los open(), criterio de tasa documentado en comentarios.

ESTILO: estudiante de primer año (ciclos while, listas, tuplas, funciones cortas, nombres en español,
comentarios simples).
PROHIBIDO: diccionarios, .replace(), sorted(), min(), max(), sum(), .sort(), import csv, numpy, statistics,
lambda, enumerate, zip, list comprehensions, clases.

Al terminar: py_compile, probar la Opción 1, confirmar que no hay usos prohibidos y decir qué archivos
se modificaron. NO hagas commit.
```

### Resultado verificado

- 25 países cargados; 21 monedas únicas.
- Mayor población: China, India, Estados Unidos, Brasil, México.
- Menor área: Suiza, Costa Rica, Panamá, Corea del Sur, Uruguay.
- Archivo inexistente: mensaje de error, el programa no se cierra.

---

## COMMIT 3

**Nombre:**

```text
feat: implementar normalizacion de nombres de paises
```

### Prompt usado (versión final)

```text
Trabaja en la rama main. NO hagas commit ni push.

Implementa únicamente la OPCIÓN 2 de la TP1 (consigna, página 17).

CARGA: leer paises_datos.toon con un parser propio carácter por carácter (función reutilizable
leer_datos_toon). Si no existe, mostrar "Primero ejecute la Opción 1" y volver al menú.

REGLAS (sin .replace(), carácter por carácter), en este orden:
1. Convertir a mayúsculas.
2. Eliminar espacios al inicio y al final.
3. á à â ã ä å -> A | é è ê ë -> E | í ì î ï -> I | ó ò ô õ ö -> O | ú ù û ü -> U | ñ -> N | ç -> C
   (debe funcionar con minúsculas y mayúsculas acentuadas: Á É Í Ó Ú Ñ Ç).
4. Eliminar ' - `
5. Eliminar paréntesis y su contenido.
6. Cada guion bajo se convierte en un espacio.
7. Capitalizar cada palabra (primera en mayúscula, resto en minúscula).
8. Limpiar espacios sobrantes (al inicio, al final y dobles).

CÁLCULOS EN CONSOLA: longitud promedio como valor entero; país con el nombre más largo y más corto (nombre y
longitud); cantidad de países que contienen una letra dada por el usuario (validar que sea una sola letra,
sin distinguir mayúsculas y normalizando tildes; un país cuenta una sola vez).

GUARDADO: sobrescribir paises_datos.toon con los nombres normalizados, en el mismo formato. Ejecutar la
Opción 2 dos veces no debe cambiar el resultado.

PROHIBIDO: .replace(), .upper(), .lower(), .strip(), .title(), .capitalize(), .split(), .translate(),
.isalpha(), unicodedata, re, diccionarios, sorted(), min(), max(), sum(), .sort(), import csv, numpy,
statistics, lambda, enumerate, zip, list comprehensions, clases.

PRUEBAS (script temporal fuera del repo): México, "  Perú  ", PERÚ, España, Corea del Sur, costa_rica,
Guinea-Bissau, Côte d'Ivoire, Congo (Rep.), Curaçao, Åland, "Nueva   Zelanda".
Al terminar: py_compile, búsqueda de usos prohibidos, probar la Opción 1 y las opciones 3 a 9.
NO hagas commit.
```

### Resultado verificado

| Entrada | Salida |
|---|---|
| `México` | `Mexico` |
| `  Perú  ` / `PERÚ` | `Peru` |
| `España` | `Espana` |
| `Corea del Sur` | `Corea Del Sur` |
| `costa_rica` | `Costa Rica` |
| `Guinea-Bissau` | `Guineabissau` |
| `Côte d'Ivoire` | `Cote Divoire` |
| `Congo (Rep.)` | `Congo` |
| `Curaçao` / `Åland` | `Curacao` / `Aland` |
| `Nueva   Zelanda` | `Nueva Zelanda` |

Con los 25 países: longitud promedio **7**, más largo **Estados Unidos (14)**, más corto **Peru (4)**,
**20** países contienen la letra "A" y **11** contienen la "E" (también al escribir "é").

---

## Verificación antes de cada commit

```powershell
# Usos prohibidos (no debe aparecer nada, salvo textos dentro de docstrings)
Select-String -Path *.py -Pattern "\.replace\(|\.upper\(|\.lower\(|\.strip\(|\.title\(|\.capitalize\(|\.split\(|\.isalpha\(|\.translate\(|sorted\(|min\(|max\(|sum\(|\.sort\(|dict\(|import csv|import re|unicodedata|lambda|enumerate|zip\("

# Diccionarios literales (solo se permiten llaves dentro de f-strings)
Select-String -Path *.py -Pattern "\{"

# Tildes (PowerShell necesita el encoding para mostrarlas bien)
Get-Content paises.csv -Encoding UTF8 | Select-Object -First 5

# Idempotencia de la Opción 2: el hash no debe cambiar al ejecutarla dos veces
Get-FileHash paises_datos.toon

git status
```

---

## Problemas encontrados y soluciones

(Para registrar en `Plantilla_Bitacora_ResoluciónProb.xls`; la consigna pide al menos 7.)

| N.º | Problema | Solución |
|---|---|---|
| 1 | El menú del commit 1 no seguía la sección 5 de la consigna | Se rehízo con las 9 opciones del PDF |
| 2 | No había CSV de datos en el repositorio | Se creó `paises.csv` con el formato del PDF y 25 países |
| 3 | Los códigos ISO estaban en 3 letras y la consigna pide 2 | Se cambiaron a 2 letras (AR, BR, CL...) |
| 4 | La estructura del `.toon` era ambigua (campos con indentación incoherente) | Se rediseñó con `-` en su línea y niveles de 4 espacios |
| 5 | "Mayor valor" (Opción 1) y "mayor tasa = más fuerte" (Opción 4) se contradicen | Se eligió un criterio, se documentó en el código y se consultará a la profesora |
| 6 | PowerShell mostraba `BrasileÃ±o` por leer UTF-8 como ANSI | `encoding="utf-8"` en los `open()` y `-Encoding UTF8` al revisar |
| 7 | `PERÚ` en mayúscula no se normalizaba | La tabla de reemplazo cubre mayúsculas y minúsculas acentuadas |
| 8 | La rama se llamaba `master` y se quería `main` | `git branch -M main` y `git push -u origin main` |

---

## Pendiente para los siguientes avances

- **Opción 3** (cálculos poblacionales y densidad) y **Opción 4** (monedas): E2.
- **Opción 5** (reporte TXT), **6** (HTML monedas) y **7** (HTML densidad). La Opción 5 reutiliza
  `normalizar_nombre` para las capitales.
- **Opción 8** (bitácora en `bitacora.bin` con submenú A–E) y registro de eventos en las Opciones 1 y 2.
  Aún no existe.
- Documentación en PDF (`documentaciónCódigos.PDF`) y estadística de tiempos.
- Mínimo de 3 commits por persona por semana (18 en total); el compañero debe hacer los suyos desde su cuenta.
- Entrega: viernes 16 de octubre, 11:40 pm, por TEC Digital.