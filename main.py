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
EA = 0
SEGM = 0
SEGP = 0
CDISA = 0
CDI = 0
PMEGMV = 0
PMEGPS = 0
PPENCD = 0
PPEANCD = 0
PMEPE = 0

def obtener_VELV():
    # TODO: Poner la fdp que realmente es
    return random.uniform(3.888, 11.94)

def obtener_VELVT():
    # TODO: Poner la fdp que realmente es
    return random.uniform(8.431, 18.217)

def obtener_potencia(Velocidad_viento):
    # TODO: Poner la funcion que realmente es
    return 2000 + Velocidad_viento

def obtener_EGPS():
    # TODO: Poner la fdp que realmente es
    return random.uniform(21, 42)

def obtener_DEC():
    # TODO: Poner la fdp que realmente es 
    return random.uniform(100, 120)

def impresion_de_resultados():
    print("\n\n### Resultados ###\n\n")
    print("Cantidad de molinos de viento: ", CANTMV)
    print("Cantidad de paneles solares: ", CANTPN)
    print("Cantidad de almacenamiento de energia electrica: ", CAAEE)

    print("Promedio Mensual de Energía Generada por Molinos de Viento: PMEGMV = ", PMEGMV, "MW")
    print("Promedio Mensual de Energía Generada por Paneles Solares: PMEGPS = ", PMEGPS, "MW")
    print("Promedio Mensual de Energía Generada en Total: PMEGT = ", PMEGMV + PMEGPS)
    print("Porcentaje de días en el que la Producción Energética del día no logró cubrir la demanda de la ciudad: PPENCD = ", PPENCD, "%")
    print("Porcentaje de días en que la Producción energética del día y la energía almacenada no lograron cubrir la demanda de la ciudad: PPEANCD = ", PPEANCD, "%")
    print("Promedio Mensual de Excedente de Producción Energética Desperdiciada: PMEPE = ", PMEPE, "MW")

    print("\n\n### Fin de la simulacion ###\n\n")


def realizar_simulacion():
    global T, TF, EVENTO, SE, EGPS, EGM, EGP, VELV, VELTV, CANTMV, CANTPN, CAAEE, HV, DESP, FAL, DEC, EA, SEGM, SEGP, CDISA, CDI, PMEGMV, PMEGPS, PPENCD, PPEANCD, PMEPE

    while True:
        T = T + 1
        EGPS = obtener_EGPS()
        R1 = random.uniform(0, 1)
        if R1 <= 0.05:
            EVENTO = "Tormenta"
            VELTV = obtener_VELVT() 
            EGM = obtener_potencia(VELTV) * CANTMV 
            EGP = EGPS * CANTPN * 0.2 # 20% de eficiencia en tormenta para los paneles
        else:
            VELV = obtener_VELV()
            EGM = obtener_potencia(VELV) * CANTMV  
            if R1 <= 0.23:
                EVENTO = "Lluvia"
                EGP = EGPS * CANTPN * 0.4 # 40% de eficiencia en dia lluviso para los paneles
            else:
                EVENTO = "Soleado"
                EGP = EGPS * CANTPN # 100% de eficiencia en normal para los paneles
        
        EA = SE # Energia almacenada del dia anterior
        SE = SE + (EGP + EGM)/1000
        R2 = random.uniform(0, 1)

        if R2 <= 0.05:
            EVENTO = "Mantenimiento"
            SE = SE - (EGM * 0.2)/1000 # 20% de produccion perdida por mantenimiento
            SEGM = SEGM + (EGM * 0.2)/1000 # Sumatoria de energia generada por molinos
        else:
            SEGM = SEGM + EGM/1000 

        SEGP = SEGP + EGP/1000 # Sumatoria de energia generada por paneles

        DEC = obtener_DEC()
        if (SE - EA) < DEC:
            CDISA = CDISA + 1 # Cantidad de veces que no se cumplio la demanda sin usar lo almacenado
            if SE > DEC:
                SE = SE - DEC
            else:
                CDI = CDI + 1 # Cantidad de demandas diarias incumplidas
                FAL = FAL + DEC - SE # Cantidad de energia faltante # TODO: Revisar si se deja porque no se usa
                SE = 0
        else:
            SE = SE - DEC
            if SE > CAAEE:
                DESP = DESP + SE - CAAEE # Cantidad de energia desperdiciada
                SE = CAAEE

        if T == TF:
            break
        else:
            continue
    
    PMEGMV = (SEGM/T)*30
    PMEGPS = (SEGP/T)*30
    PPENCD = (CDISA/T)*100
    PPEANCD = (CDI/T)*100
    PMEPE = (DESP/T) *30

    impresion_de_resultados()

def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")


# Cosa de python que no importa
if __name__ == "__main__":
    main()
