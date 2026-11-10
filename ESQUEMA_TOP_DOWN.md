# Esquema Top-Down - Controlador de misiones

## Integrante

Santino López

## Descripción

El programa utiliza un diseño Top-Down, dividiendo la ejecución de misiones para el robot Unitree Go2 en funciones con responsabilidades específicas.

La función principal coordina la conexión con el simulador, la ejecución de las misiones y la generación de reportes.

## Descomposición del programa

```text
main()
│
├── Conectar el robot
│
├── Por cada misión
│   │
│   ├── Crear historial
│   │
│   ├── ejecutar_mision(robot, mision, historial)
│   │   ├── comando_es_valido(comando)
│   │   ├── ejecutar_comando(robot, comando) si es válido
│   │   └── Registrar el resultado en historial
│   │
│   └── generar_reporte(historial)
│       ├── Contar comandos ejecutados y omitidos
│       ├── Calcular distancia y duración estimada
│       └── Mostrar el reporte
│
└── Detener y desconectar el robot
```

## Funciones principales

### comando_es_valido(comando)

Recibe un comando y comprueba que su tipo, cantidad de parámetros y valores sean correctos. Devuelve un valor booleano que indica si puede ejecutarse.

### ejecutar_comando(robot, comando)

Recibe el robot y un comando válido. Ejecuta la acción correspondiente mediante el puente de comunicación con el simulador y devuelve el resultado de la operación.

### ejecutar_mision(robot, mision, historial)

Recibe una lista de comandos y los procesa mediante un ciclo `for`. Registra los comandos ejecutados y omitidos en la lista `historial`, utilizando `continue` para no interrumpir la misión cuando encuentra una orden inválida.

### generar_reporte(historial)

Recorre el historial y muestra la cantidad de comandos recibidos, ejecutados y omitidos, junto con la distancia recorrida y la duración estimada.

### main()

Coordina la conexión con el simulador, ejecuta las cuatro misiones, genera los reportes correspondientes y desconecta el robot al finalizar.

## Estructuras utilizadas

### Lista de tuplas

Las misiones se representan mediante listas de tuplas. Cada tupla contiene el tipo de comando y sus parámetros.

### Lista de diccionarios

El historial utiliza diccionarios para registrar los resultados de los comandos y almacenar la información necesaria para generar los reportes.

### Decisiones e iteraciones

Se utilizan estructuras condicionales y ciclos para validar las órdenes, ejecutar los comandos correctos y continuar ante comandos inválidos.

## Ventaja del diseño

La división en funciones permite ejecutar diferentes misiones modificando únicamente la lista de comandos, sin necesidad de reescribir la lógica de validación, ejecución y generación de reportes.
