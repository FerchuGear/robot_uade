# Informe breve - Diseño Top-Down y pasaje de parámetros

## Integrante

Santino López

## Descripción

El controlador se construyó mediante diseño Top-Down, dividiendo la ejecución de una misión en funciones específicas. `comando_es_valido()` comprueba los parámetros, `ejecutar_comando()` envía las órdenes al robot, `ejecutar_mision()` recorre la secuencia y almacena los resultados, y `generar_reporte()` calcula las estadísticas.

## Estructuras y pasaje de parámetros

Cada misión es una lista de tuplas que puede cambiar sin modificar las funciones. Se utilizan condicionales y un ciclo `for` con `continue` para omitir comandos inválidos y conservar el resto de la ejecución.

Las velocidades y los tiempos son valores numéricos que las funciones consultan sin modificarlos. En cambio, `historial` es una lista mutable: la función `ejecutar_mision()` agrega diccionarios mediante `append()` y después `generar_reporte()` utiliza esos registros. En Python las funciones reciben referencias a objetos, y esta diferencia se observa al trabajar con objetos mutables.

## Misión propia

Para ejecutar la misión propia solo se definió una lista nueva de seis comandos, sin reescribir las funciones. Cinco se ejecutaron y uno se rechazó porque la velocidad angular superaba el límite. El reporte indicó 0,7 m recorridos y 5,07 s de duración estimada.

Las otras misiones también finalizaron: básica (4 ejecutados), con errores (4 ejecutados y 7 omitidos) y cuadrado (9 ejecutados). El Go2 se observó en MuJoCo. La experiencia mostró que separar responsabilidades facilita reutilizar el código y analizar los resultados.
