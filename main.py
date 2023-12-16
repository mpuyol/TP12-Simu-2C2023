import random
import math
import time
    
CANTMV = 0  # Cantidad de Molinos de viento
CANTPN = 0  # Cantidad de Paneles solares
CAAEE = 0   # Cantidad de almacenamiento de energia electrica


while True:
    try:
        ### VARIABLES DE CONTROL ###
        CANTMV = int(input("Cantidad de molinos de viento (M): "))
        CANTPN = int(input("Cantidad de paneles solares (P): "))
        CAAEE = int(input("Cantidad de almacenamiento de energia electrica (CAAEE): "))

        break
    except ValueError:
        print("\nError: Solo se permiten numeros enteros.\n")
        continue

HV = 6666666666666 # Valor infinito

EVENTO = "C.I."

T = 0  # Tiempo actual
TF =   365 * 4   # 4 años


def obtener_VELV():
    while True:
        pass
       # R = random.uniform(0, 1)
       # TA = 14.5 * math.sqrt(2) * math.sqrt(-math.log(1 - R))  # Aca iria la funcion de la distribucion de probabilidad
        return 1


def obtener_VELVT():
    while True:
        pass
       # R = random.uniform(0, 1)
       # TA = 14.5 * math.sqrt(2) * math.sqrt(-math.log(1 - R))
        return 1


def obtener_EGPS():
    while True:
        pass
       # R = random.uniform(0, 1)
       # TA = 14.5 * math.sqrt(2) * math.sqrt(-math.log(1 - R))
        return 1
    

def obtener_DEC():
    while True:
        pass
       # R = random.uniform(0, 1)
       # TA = 14.5 * math.sqrt(2) * math.sqrt(-math.log(1 - R))
        return 1



def realizar_simulacion():
    T = T + 1
    R1 = random.uniform(0, 1)
    if R1 <= 0.05:
        EVENTO = "Tormenta"
        VELTV = obtener_VELVT()
        EGM = VELTV * CANTMV 
        
    elif R1 <= 0.15:

    resultados()


def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")


# Cosa de python que no importa
if __name__ == "__main__":
    main()
