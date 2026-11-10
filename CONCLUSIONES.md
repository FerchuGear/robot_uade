# Conclusiones - TP02 Unitree Go2

## Integrante

Santino López

## Respuestas del cierre del orientador

### a) ¿Cuál fue la principal dificultad de instalación?

No se presentaron dificultades. El repositorio, las herramientas y el simulador estuvieron disponibles y funcionaron correctamente en el primer intento informado.

### b) ¿Qué error requirió mayor investigación?

No hubo errores técnicos que requirieran investigación. Los comandos incorrectos de `MISION_CON_ERRORES` eran pruebas intencionales y no fallas del entorno.

### c) ¿Qué solución resultó efectiva y por qué?

No fue necesario aplicar reparaciones. Seguir el procedimiento vigente del laboratorio UADE y usar su puente `robot.py` permitió ejecutar el controlador. Las validaciones evitaron enviar órdenes inválidas al robot.

### d) ¿Qué intento no funcionó y qué se aprendió?

No hubo intentos fallidos de instalación. Las pruebas con comandos inválidos permitieron comprobar la importancia de validar los tipos, los límites y la cantidad de parámetros antes de ejecutar una orden.

### e) ¿Qué diferencia existe entre la guía anterior y la arquitectura actual?

El PDF original describe `unitree_sdk_sim.py` y parámetros de distancia o ángulo. El laboratorio actual utiliza `robot.py`, un socket local y órdenes basadas en velocidad y tiempo. Para este trabajo se siguió la API vigente.

### f) ¿Hasta qué nivel se logró avanzar?

Se alcanzó el **nivel 10: reporte final generado**. Se visualizaron el Go2 en MuJoCo, la conexión del controlador y la ejecución de las cuatro misiones. En total se recibieron 30 comandos, se ejecutaron 22 y se omitieron 8.

### g) ¿Cuál sería el próximo paso?

Una mejora sería mostrar el motivo específico de cada rechazo en lugar de un mensaje genérico y agregar nuevas misiones sin modificar las funciones del controlador.

## Reflexión final

El trabajo permitió aplicar el diseño Top-Down, funciones, listas de tuplas y un historial de diccionarios para controlar distintas misiones. La prueba con errores demostró que las órdenes inválidas pueden rechazarse y registrarse sin interrumpir los pasos restantes. No hubo dificultades técnicas de instalación; el aprendizaje principal estuvo relacionado con la organización del programa, la validación de comandos y la generación de reportes.
