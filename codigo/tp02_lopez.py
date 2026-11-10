from robot import ErrorDeSeguridad, Robot
from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO

VELOCIDAD_MAX = 0.20
GIRO_MAX = 0.50
TIEMPO_MAX = 10.0

MISION_PROPIA = [
    ("avanzar", 0.2, 2.0),
    ("girar", 0.5, 1.57),
    ("avanzar", 0.2, 1.5),
    ("girar", 0.8, 1.0),
    ("saludar",),
    ("detenerse",)
]

def comando_es_valido(comando):
    valido = False
    if isinstance(comando, tuple) and len(comando) > 0:
        tipo = comando[0]
        if tipo in ("detenerse", "saludar") and len(comando) == 1:
            valido = True
        elif tipo in ("avanzar", "girar") and len(comando) == 3:
            velocidad = comando[1]
            tiempo = comando[2]
            if isinstance(velocidad, (int, float)) and not isinstance(velocidad, bool) and isinstance(tiempo, (int, float)) and not isinstance(tiempo, bool):
                if 0 < tiempo <= TIEMPO_MAX:
                    if tipo == "avanzar" and 0 < velocidad <= VELOCIDAD_MAX:
                        valido = True
                    elif tipo == "girar" and 0 < abs(velocidad) <= GIRO_MAX:
                        valido = True
    return valido

def ejecutar_comando(robot, comando):
    tipo = comando[0]
    resultado = "EJECUTADO"
    try:
        if tipo == "avanzar":
            robot.avanzar(velocidad=comando[1], tiempo=comando[2])
        elif tipo == "girar":
            robot.girar(velocidad=comando[1], tiempo=comando[2])
        elif tipo == "detenerse":
            robot.detenerse()
        elif tipo == "saludar":
            robot.saludar()
    except ErrorDeSeguridad as error:
        resultado = f"Error de seguridad: {error}"
    return resultado

def ejecutar_mision(robot, mision, historial):
    for comando in mision:
        registro = {"comando": comando, "ejecutado": False, "motivo": "", "distancia": 0.0, "duracion": 0.0}
        if not comando_es_valido(comando):
            registro["motivo"] = "Comando desconocido, incompleto o con parametros fuera de los limites"
            historial.append(registro)
            print(f"[OMITIDO] {comando} - {registro['motivo']}")
            continue
        resultado = ejecutar_comando(robot, comando)
        if resultado == "EJECUTADO":
            registro["ejecutado"] = True
            if comando[0] in ("avanzar", "girar"):
                registro["duracion"] = comando[2]
            if comando[0] == "avanzar":
                registro["distancia"] = comando[1] * comando[2]
            print(f"[OK] {comando}")
        else:
            registro["motivo"] = resultado
            print(f"[OMITIDO] {comando} - {resultado}")
        historial.append(registro)

def generar_reporte(historial):
    ejecutados = 0
    omitidos = 0
    distancia = 0.0
    duracion = 0.0
    print("\nREPORTE DE MISIÓN")
    print("=================")
    for registro in historial:
        if registro["ejecutado"]:
            ejecutados += 1
            distancia += registro["distancia"]
            duracion += registro["duracion"]
        else:
            omitidos += 1
            print(f"Rechazado: {registro['comando']} - {registro['motivo']}")
    print(f"Comandos recibidos: {len(historial)}")
    print(f"Comandos ejecutados: {ejecutados}")
    print(f"Comandos omitidos: {omitidos}")
    print(f"Distancia recorrida: {round(distancia, 2)} m")
    print(f"Duración estimada: {round(duracion, 2)} s\n")

def main():
    robot = Robot()
    robot.conectar()
    misiones = (("BÁSICA", MISION_BASICA), ("CON ERRORES", MISION_CON_ERRORES), ("CUADRADO", MISION_CUADRADO), ("PROPIA", MISION_PROPIA))
    try:
        for nombre, mision in misiones:
            historial = []
            print(f"\n=== MISIÓN {nombre} ===")
            ejecutar_mision(robot, mision, historial)
            generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()

if __name__ == "__main__":
    main()
