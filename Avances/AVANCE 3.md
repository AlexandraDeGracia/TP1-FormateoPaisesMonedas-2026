# AVANCE 3 — Persistencia en dos TOON, bitácora binaria real, robustez y cierre

Cubre la fase final de la TP1 "Sistema de formateo y análisis de datos de países y monedas"
(Taller de Programación, II Semestre 2026): mejoras de persistencia, bitácora, robustez de
entrada, ampliación de los datos de prueba, limpieza del repositorio y pruebas de cierre.

---

## Estado del avance

| Commit | Nombre | Estado |
|---|---|---|
| 17 | `feat: separar TOON en paises y tasas, bitacora con pickle, formatos.py y cierre del avance 3` | Se registra al hacer el commit y el push |

**Rama de trabajo:** `main`.
Confirmar con `git log --oneline` y `git status` que el commit quedó en `origin/main`.

---

## Cambios respecto al Avance 2

### 1. Persistencia TOON separada (`datos.py`)
- `paises.toon`: nombre, capital, código ISO, población, área y código de moneda de cada país.
- `tasas_cambio.toon`: `fecha_tasa` y la lista de monedas **únicas** (código, nombre, tasa_usd).
- Antes, los datos de la moneda se repetían por país (p. ej. el EUR cinco veces) y la fecha de
  la tasa era la fecha del día. Ahora la fecha se guarda en el archivo al cargar los datos y la
  Opción 1 la lee de ahí.
- Opciones 2 y 3 leen `paises.toon`; 4 y 6 leen `tasas_cambio.toon`; 5 y 7 leen ambos.
- Lectura y escritura siguen siendo manuales (línea por línea, sin diccionarios).

### 2. Bitácora binaria real (`bitacora.py`)
- `bitacora.bin` guarda una tupla `("AAAA-MM-DD HH:MM:SS", "descripción")` por registro con
  `pickle`, en modo `ab`. La lectura recorre el archivo hasta `EOFError`.
- Se conserva el submenú A–E (buscar por fecha, por palabra clave, mostrar todo, exportar a CSV).
- También se registra cada lectura de TOON (ruta, cantidad de registros y tiempo de respuesta).

### 3. Formato numérico centralizado (`formatos.py`)
- Nuevo módulo con el formateo manual a 2 y 4 decimales y el formato limpio de números.
- La consola y los reportes usan las mismas funciones (p. ej. `122.80` en lugar de `122.8`).

### 4. Robustez de entrada (`main.py`)
- `EOFError` y `KeyboardInterrupt` se capturan: mensaje claro, registro en bitácora y salida limpia.
- Se eliminó la duplicación de las opciones 3–7 con una función de carga común.

### 5. Etiquetas del criterio de moneda
- Opción 4 y reporte HTML de monedas usan "Moneda más fuerte (mayor tasa)" y
  "Moneda más débil (menor tasa)", según el enunciado. La nota económica queda como aclaración.

### 6. Datos de prueba ampliados (`paises.csv`)
- De 25 a 35 países y 26 monedas.
- Ahora aparecen las cuatro categorías de población y nombres con `_`, `-`, paréntesis y tildes
  (p. ej. Corea del Sur, Guinea-Bissau, Congo, Côte d'Ivoire, São Tomé y Príncipe), de modo que
  la normalización y el gráfico ASCII se ejercitan completos.

### 7. Limpieza del repositorio
- `.gitignore` ahora ignora archivos generados: `bitacora.bin`, `bitacora.csv`, `*.toon`,
  `reporte_*.txt`, `reporte_*.html` y `__pycache__/`.
- Se retiraron del control de versiones los archivos generados y el material de apoyo que no
  forma parte de la entrega.

---

## Estado del sistema

| Elemento | Valor |
|---|---|
| Módulos | 7 (`main`, `datos`, `formateo_strings`, `calculos`, `reportes`, `bitacora`, `formatos`) |
| Funciones | 115 |
| Países en `paises.csv` | 35 |
| Monedas únicas | 26 |
| Tasa de cambio promedio | 456.7619 |
| Restricciones | Sin `.replace()`, sin diccionarios, sin `statistics`/`numpy`, sin `sorted`/`sum`/`round`; solo `datetime`, `time` y `pickle` |

---

## Pruebas realizadas

Se ejecutó el programa completo con entradas válidas e inválidas y no se produjo ninguna traza de error.

| Prueba | Resultado |
|---|---|
| Opciones 1 a 9 en secuencia normal | Correcto: 35 países, 26 monedas, reportes TXT/HTML generados |
| Opción 1 con archivo inexistente (`noexiste.csv`) | Mensaje de error, registro en bitácora, regreso al menú |
| Opción 2 antes de la Opción 1 | Aviso "Primero ejecute la Opción 1" y regreso al menú |
| Letra inválida en Opción 2 | Rechazada; se vuelve a pedir |
| N = 0 o texto en Opción 4 | Rechazado; se vuelve a pedir |
| Opción de menú inválida (`99`, `A`) | Aviso y registro del error en bitácora |
| Submenú de bitácora: búsqueda por fecha y palabra clave | Coincidencias mostradas y registradas |
| Exportar bitácora a CSV | `bitacora.csv` generado con encabezado y registros |
| Fin de entrada (Ctrl+D) | Salida limpia sin traza |

---

## Pendientes antes de la entrega

- Documentación final en PDF (`documentaciónCódigos.PDF`).
- Verificar que el repositorio de GitHub sea público.
- Armar el comprimido de entrega (Parte 1: documentación; Parte 2: código fuente).