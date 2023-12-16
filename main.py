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
SE = 0  # Suma de energia electrica
EGPS = 0  # Energia generada por los paneles solares
EGM = 0  # Energia generada por los molinos de viento
EGP = 0  # Energia generada por los paneles solares
VELV = 0  # Velocidad del viento
VELTV = 0  # Velocidad del viento en tormenta
DESP = 0  # Cantidad de energia desperdiciada
FAL = 0  # Cantidad de energia faltante
DEC = 0  # Demanda de energia electrica



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

def resultados():
    print("\n\n### Resultados ###\n\n")
    print("Cantidad de molinos de viento: ", CANTMV)
    print("Cantidad de paneles solares: ", CANTPN)
    print("Cantidad de almacenamiento de energia electrica: ", CAAEE)
    print("Cantidad de energia electrica desperdiciada: ", DESP)
    print("Cantidad de energia electrica faltante: ", FAL)
    print("Cantidad de energia electrica producida: ", SE)
    print("Cantidad de energia electrica consumida: ", DEC)
    print("Cantidad de energia electrica producida por los molinos de viento: ", EGM)
    print("Cantidad de energia electrica producida por los paneles solares: ", EGP)
    print("\n\n### Fin de la simulacion ###\n\n")


def realizar_simulacion():
    global T, TF, EVENTO, SE, EGPS, EGM, EGP, VELV, VELTV, CANTMV, CANTPN, CAAEE, HV, DESP, FAL, DEC

    while True:
        T = T + 1
        EGPS = obtener_EGPS()
        R1 = random.uniform(0, 1)

        if R1 <= 0.05:
            EVENTO = "Tormenta"
            VELTV = obtener_VELVT() 
            EGM = VELTV * CANTMV 
            EGP = EGPS * CANTPN * 0.2 # 20% de eficiencia en tormenta para los paneles
        else:
            VELV = obtener_VELV()
            EGM = VELV * CANTMV  
            if R1 <= 0.22:
                EVENTO = "Lluvia"
                EGP = EGPS * CANTPN * 0.4 # 40% de eficiencia en dia lluviso para los paneles
            else:
                EVENTO = "Soleado"
                EGP = EGPS * CANTPN # 100% de eficiencia en normal para los paneles
        
        SE = SE + EGP + EGM
        R2 = random.uniform(0, 1)

        if R2 <= 0.05:
            EVENTO = "Manetenimiento"
            SE = SE - EGM * 0.2 # 20% de produccion perdida por mantenimiento

        DEC = obtener_DEC()
        if SE > DEC:
            SE = SE - DEC
            if SE > CAAEE:
                SE = CAAEE
                DESP = DESP + SE - CAAEE # Cantidad de energia desperdiciada
        else:
            FAL = FAL + DEC - SE # Cantidad de energia faltante
            SE = 0
        
        if T == TF:
            break
        else:
            continue
    
    resultados()

def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")


# Cosa de python que no importa
if __name__ == "__main__":
    main()
