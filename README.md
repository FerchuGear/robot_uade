# Controlador de Misiones - Unitree Go2

Trabajo Práctico N.º 2 de Programación I.

## Integrante

Santino López

## Descripción

El proyecto consiste en un controlador de misiones desarrollado en Python para el robot Unitree Go2, utilizando el simulador MuJoCo del laboratorio UADE.

El sistema recibe misiones representadas como listas de comandos, valida cada orden, la ejecuta cuando corresponde y genera un informe con los resultados. Los comandos incorrectos se registran y se omiten sin interrumpir la misión.

**Repositorio de entrega:** https://github.com/FerchuGear/robot_uade.git

**Repositorio base del laboratorio:** https://github.com/tsamaan/UadeRobotLab.git

## Objetivo

Aplicar diseño Top-Down, funciones con parámetros, listas, tuplas, diccionarios, decisiones, iteraciones y validaciones para desarrollar un controlador capaz de ejecutar distintas misiones sin reescribir su lógica.

## Funcionalidades

El programa permite:

1. Conectarse con el simulador del robot Unitree Go2.
2. Ejecutar comandos de avance, giro, detención y saludo.
3. Validar el tipo de comando y los parámetros recibidos.
4. Detectar y omitir comandos inválidos sin finalizar la misión.
5. Registrar los resultados de cada comando en un historial.
6. Calcular la distancia y la duración estimada de los movimientos válidos.
7. Generar un reporte independiente para cada misión.
8. Desconectarse del simulador al finalizar.

## Comandos utilizados

- `avanzar(velocidad, tiempo)`: movimiento hacia adelante.
- `girar(velocidad, tiempo)`: giro; velocidad positiva hacia la izquierda y negativa hacia la derecha.
- `detenerse()`: detención del robot.
- `saludar()`: acción de saludo.

Los límites utilizados por el controlador son **0,20 m/s** de avance, **0,50 rad/s** de velocidad angular en valor absoluto y **10 segundos** por orden de movimiento.

## Estructuras utilizadas

### Listas y tuplas

Cada misión se representa mediante una lista de tuplas. Las tuplas indican el comando y sus parámetros, por ejemplo `("avanzar", 0.2, 2.0)`.

### Diccionarios

El historial se almacena en una lista de diccionarios que registra el comando recibido, si fue ejecutado, el motivo de rechazo y los valores necesarios para el reporte.

### Funciones y control de flujo

El programa utiliza funciones con responsabilidades diferenciadas, un ciclo `for`, condiciones `if/elif` y `continue` para omitir comandos inválidos. El historial se modifica dentro de la función que ejecuta la misión.

## Modularización

El controlador se organiza en cuatro funciones principales:

- `comando_es_valido(comando)`: comprueba tipo, cantidad de parámetros y límites.
- `ejecutar_comando(robot, comando)`: envía al robot una orden previamente validada.
- `ejecutar_mision(robot, mision, historial)`: procesa la misión y registra los resultados.
- `generar_reporte(historial)`: calcula e imprime las estadísticas finales.

La función `main()` coordina la conexión, ejecuta las cuatro misiones y desconecta el robot. El esquema está documentado en `ESQUEMA_TOP_DOWN.md`.

## Entorno utilizado

- Sistema operativo: Windows 11 Pro, versión 25H2.
- Arquitectura: AMD64.
- Python: 3.11.3.
- MuJoCo: 4.0.0.
- Editor: Visual Studio Code.

La instalación y ejecución se realizaron sin incidencias técnicas. No fue necesario instalar CycloneDDS ni el SDK oficial de Unitree.

## Instalación y ejecución

El archivo `codigo/tp02_lopez.py` contiene **únicamente el controlador desarrollado**. Para ejecutarlo se necesita el entorno del laboratorio UADE, incluidos sus módulos `robot.py` y `misiones.py`.

1. Clonar el repositorio original:

   ```bash
   git clone https://github.com/tsamaan/UadeRobotLab.git
   ```

2. Ingresar a `UadeRobotLab/05LaboratoriosTPs/TP02_Programacion_I/`.
3. Leer `INSTALACION.md` y `LEEME_ESTUDIANTE.md`, e instalar MuJoCo si no está disponible.
4. Copiar el contenido de `codigo/tp02_lopez.py` en `mi_desarrollo/mi_tp02.py` del laboratorio.
5. Ejecutar `INICIAR_SIMULADOR.bat` y seleccionar `2 - Go2`.
6. Mantener el simulador abierto y, en otra terminal, ejecutar `EJECUTAR_MI_CODIGO.bat`.

No se modificaron los archivos `robot.py` ni `misiones.py` proporcionados por la cátedra. El controlador no se distribuye como aplicación independiente.

## Misiones ejecutadas

| Misión | Recibidos | Ejecutados | Omitidos | Distancia | Duración estimada |
|---|---:|---:|---:|---:|---:|
| Básica | 4 | 4 | 0 | 0,8 m | 7,14 s |
| Con errores | 11 | 4 | 7 | 0,4 m | 5,14 s |
| Cuadrado | 9 | 9 | 0 | 1,6 m | 20,56 s |
| Propia | 6 | 5 | 1 | 0,7 m | 5,07 s |
| **Total** | **30** | **22** | **8** | **3,5 m** | **37,91 s** |

En `MISION_CON_ERRORES` se rechazaron siete órdenes incorrectas de manera intencional, sin detener el resto de la ejecución. La misión propia incluyó un giro fuera de rango y también continuó correctamente.

El robot se visualizó en MuJoCo y se generaron los cuatro reportes. **Nivel alcanzado: 10 (reporte final generado).**

## Archivos del trabajo

- `codigo/tp02_lopez.py`: controlador desarrollado.
- `BITACORA.md`: caracterización del entorno, pasos y resultados.
- `PROBLEMAS.md`: registro de problemas y de comandos inválidos deliberados.
- `ESQUEMA_TOP_DOWN.md`: organización y responsabilidades del programa.
- `INFORME_BREVE.md`: explicación del diseño y del pasaje de parámetros.
- `CONCLUSIONES.md`: respuestas finales del orientador y reflexión.
- `evidencias/`: capturas del entorno, del simulador y de las misiones, con un índice en `evidencias/README.md`.

## Alcance

Se desarrolló y probó el controlador de misiones en el entorno simulado proporcionado por UADE. No se incluye un robot físico ni una instalación completa de MuJoCo en este repositorio.
