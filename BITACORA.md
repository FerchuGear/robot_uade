# Bitácora técnica - TP02 Unitree Go2

## Integrante

Santino López

## Descripción

Se registra el procedimiento de preparación del entorno, obtención del laboratorio, puesta en marcha del simulador y ejecución del controlador. Los datos provienen de las salidas de terminal y las capturas realizadas durante el trabajo.

No se registraron problemas técnicos al obtener el repositorio ni al iniciar el simulador o ejecutar el programa.

## Lectura previa

### Herramientas necesarias

Para trabajar con el laboratorio se necesitan Python 3.10 o superior, pip, MuJoCo, el repositorio `UadeRobotLab` con los modelos del Go2 y un editor de código. Se utilizó Git para obtener el repositorio y Visual Studio Code para trabajar con el programa.

### Versión de Python

El laboratorio requiere Python 3.10 o superior. Se comprobó que estaba disponible la versión **3.11.3**.

### Componentes disponibles

Se verificaron Python 3.11.3, pip 22.3.1, Git 2.45.2.windows.1 y MuJoCo 4.0.0. No se cuenta con evidencia suficiente para afirmar si MuJoCo estaba instalado *antes* de iniciar la actividad; sí se verificó que estaba disponible durante las pruebas.

### Componentes que no se necesitan

No hace falta instalar CycloneDDS ni el SDK oficial de Unitree, porque el laboratorio actual se comunica con MuJoCo mediante el módulo `robot.py` y un socket local.

### Diferencias entre el PDF del TP y el laboratorio vigente

El PDF anterior utiliza `unitree_sdk_sim.py` y ejemplos de movimientos expresados mediante distancia/velocidad o ángulo/sentido. El repositorio vigente utiliza `robot.py` y movimientos basados en **velocidad y tiempo**, con `robot.avanzar(velocidad, tiempo)` y `robot.girar(velocidad, tiempo)`. Se respetó la API vigente.

## Caracterización del entorno

| Elemento | Información obtenida |
|---|---|
| Sistema operativo | Windows 11 Pro |
| Versión del sistema | 25H2 |
| Arquitectura | AMD64 (64 bits) |
| Python instalado | Sí |
| Versión de Python | 3.11.3 |
| pip disponible | Sí, 22.3.1 |
| Git disponible | Sí, 2.45.2.windows.1 |
| MuJoCo previamente instalado | No determinado |
| MuJoCo verificado | Sí, versión 4.0.0 |
| IDE utilizado | Visual Studio Code |
| Observaciones | Entorno verificado y ejecución sin incidencias técnicas |

## Comandos y verificaciones

| Comando o acción | Resultado obtenido |
|---|---|
| `python --version` | Python 3.11.3 |
| `py -3 --version` | Python 3.11.3 |
| `python -m pip --version` | pip 22.3.1 |
| `git --version` | Git 2.45.2.windows.1 |
| Consulta de arquitectura con `platform.machine()` | AMD64 |
| `python -c "import mujoco; print(mujoco.__version__)"` | 4.0.0 |
| `git clone https://github.com/tsamaan/UadeRobotLab.git` | Repositorio obtenido correctamente |
| `git remote -v` | `origin` vinculado a `tsamaan/UadeRobotLab.git` |
| `git log -1 --oneline` | Commit disponible `d30e282` |
| `INICIAR_SIMULADOR.bat` y selección `2 - Go2` | Verificación correcta, ventana 3D abierta y Go2 visible |
| `EJECUTAR_MI_CODIGO.bat` | Conexión informada y cuatro misiones procesadas |

La comprobación del repositorio se conservó mediante `git remote -v` y `git log -1 --oneline`. No se conservó la salida original del comando de clonación.

## Registro de actividades

| N.º | Acción | Resultado | Problema | Solución intentada | Estado |
|---|---|---|---|---|---|
| 1 | Revisar `INSTALACION.md` y `LEEME_ESTUDIANTE.md` | Se identificaron requisitos y arquitectura | Ninguno | No fue necesaria | RESUELTO |
| 2 | Verificar Python, pip y Git | Herramientas disponibles | Ninguno | No fue necesaria | RESUELTO |
| 3 | Obtener el repositorio UADE | Repositorio disponible | Ninguno | No fue necesaria | RESUELTO |
| 4 | Comprobar MuJoCo | Importación correcta; versión 4.0.0 | Ninguno | No fue necesaria | RESUELTO |
| 5 | Iniciar el simulador y seleccionar Go2 | Robot visible en la ventana 3D | Ninguno | No fue necesaria | RESUELTO |
| 6 | Ejecutar el controlador | Conexión y procesamiento de misiones | Ninguno | No fue necesaria | RESUELTO |
| 7 | Probar `MISION_CON_ERRORES` | Siete comandos inválidos omitidos y registrados | Errores intencionales de prueba | Validaciones del programa | RESUELTO |
| 8 | Probar la misión propia | Cinco ejecutados y uno omitido | Comando intencional fuera de rango | Validaciones del programa | RESUELTO |
| 9 | Generar los reportes | Cuatro reportes obtenidos | Ninguno | No fue necesaria | RESUELTO |

Los errores de comandos incluidos en las misiones eran deliberados y no representan problemas de instalación.

## Arquitectura del laboratorio

El controlador envía comandos a `robot.py`, que actúa como puente mediante un socket local `127.0.0.1` hacia el simulador MuJoCo con el modelo Unitree Go2. No se modificó el puente.

## Misiones ejecutadas

| Misión | Recibidos | Ejecutados | Omitidos | Distancia | Duración estimada |
|---|---:|---:|---:|---:|---:|
| `MISION_BASICA` | 4 | 4 | 0 | 0,8 m | 7,14 s |
| `MISION_CON_ERRORES` | 11 | 4 | 7 | 0,4 m | 5,14 s |
| `MISION_CUADRADO` | 9 | 9 | 0 | 1,6 m | 20,56 s |
| `MISION_PROPIA` | 6 | 5 | 1 | 0,7 m | 5,07 s |
| **Total** | **30** | **22** | **8** | **3,5 m** | **37,91 s** |

Las duraciones representan los tiempos programados para los movimientos válidos, no una medición cronológica del proceso completo.

## Nivel alcanzado

**Nivel 10: reporte final generado.** Se comprobó el simulador, la visualización del Go2, la conexión del controlador, las cuatro misiones y sus reportes.

## Evidencias

Las capturas del entorno, el repositorio, el simulador y las misiones se organizan en `evidencias/`. La descripción de cada una está en `evidencias/README.md`.
