# Registro de problemas - TP02 Unitree Go2

## Integrante

Santino López

## Descripción

Se documentan las dificultades encontradas durante la preparación, instalación y ejecución del laboratorio, distinguiéndolas de los comandos inválidos incorporados deliberadamente a las misiones de prueba.

## Problemas de instalación y ejecución

No se registraron incidencias técnicas durante la clonación del repositorio, la verificación de Python, pip y MuJoCo, la apertura del simulador ni la ejecución del controlador.

| Actividad | Resultado | Problema encontrado | Solución intentada | Estado |
|---|---|---|---|---|
| Obtener el repositorio UADE | Repositorio disponible | Ninguno | No fue necesaria | RESUELTO |
| Verificar Python, pip y Git | Herramientas reconocidas | Ninguno | No fue necesaria | RESUELTO |
| Verificar MuJoCo | Importación correcta, versión 4.0.0 | Ninguno | No fue necesaria | RESUELTO |
| Iniciar el simulador | Go2 visible en MuJoCo | Ninguno | No fue necesaria | RESUELTO |
| Ejecutar el controlador | Misiones y reportes completados | Ninguno | No fue necesaria | RESUELTO |

No hubo mensajes de error de instalación que interpretar, hipótesis de falla que investigar ni intentos de reparación que registrar. No se incorporaron dificultades ficticias.

## Comandos inválidos de las misiones

La misión `MISION_CON_ERRORES` incluye siete comandos inválidos para probar que el controlador pueda detectarlos, rechazarlos, registrarlos y continuar con los siguientes.

| Comando | Motivo de rechazo identificado |
|---|---|
| `('avanzar', 0.9, 2.0)` | Velocidad superior a 0,20 m/s |
| `('avanzar', 0.2, 50.0)` | Tiempo superior a 10 segundos |
| `('girar', 3.0, 2.0)` | Velocidad angular superior a 0,50 rad/s |
| `('volar', 0.2, 1.0)` | Comando desconocido |
| `('avanzar', 'rapido', 2.0)` | Velocidad no numérica |
| `('avanzar', 0.2)` | Falta el tiempo |
| `('avanzar', 0.2, -3.0)` | Tiempo negativo |

En la misión propia se agregó deliberadamente `('girar', 0.8, 1.0)`, que supera la velocidad angular máxima.

**Resultado:** se omitieron ocho comandos inválidos entre ambas misiones y la ejecución continuó con las órdenes posteriores. El programa mostró un mensaje general de validación; los motivos específicos de esta tabla se identificaron al analizar cada entrada.

## Evidencias

- `evidencias/06_misiones/mision_con_errores.png`: siete rechazos de prueba.
- `evidencias/06_misiones/mision_propia.png`: un rechazo deliberado.
- `evidencias/05_gemelo_digital/`: simulador en funcionamiento.

Las carpetas destinadas a errores y soluciones técnicas pueden quedar vacías porque no hubo incidencias reales que debieran resolverse.
