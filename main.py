import random
import math
import time
import numpy as np
from scipy.interpolate import Rbf
from scipy.optimize import minimize

CANTMV = 0  # Cantidad de Molinos de viento
CANTPN = 0  # Cantidad de Paneles solares
CAAEE = 0   # Cantidad de almacenamiento de energia electrica


while True:
    try:
        ### VARIABLES DE CONTROL ###
        CANTMV = int(input("Cantidad de molinos de viento (M): "))
        CANTPN = int(input("Cantidad de paneles solares (P): "))
        CAAEE = int(input("Cantidad de almacenamiento de energia electrica (MW) (CAAEE): "))

        break
    except ValueError:
        print("\nError: Solo se permiten numeros enteros.\n")
        continue

HV = 6666666666666 # Valor infinito

EVENTO = "C.I."


# Datos de la Curva de Potencia
velocidad_viento = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30, 30.5, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 35])
potencia = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 73, 169, 280, 404, 585, 768, 1069, 1374, 1835, 2295, 2685, 3072, 3300, 3400, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 3450, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


T = 0  # Tiempo actual
TF = 365 * 10 # 10 años
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
COSTOS = 0
COSTOMV = 1500000
COSTOPN = 300

# Definir la función de error para minimizar
def error_function(params, velocidad, potencia):
    epsilon = params[0]
    rbf = Rbf(velocidad, potencia, function='multiquadric', epsilon=epsilon)
    potencia_fit = rbf(velocidad)
    error = np.sum((potencia - potencia_fit)**2)
    return error

# Establecer valores iniciales para la optimización
initial_params = [2.0]

# Optimizar la función de error
result = minimize(error_function, initial_params, args=(velocidad_viento, potencia), method='Nelder-Mead')

# Obtener los parámetros óptimos
optimal_epsilon = result.x[0]

# Crear la función RBF con los parámetros óptimos
rbf = Rbf(velocidad_viento, potencia, function='multiquadric', epsilon=optimal_epsilon)

def potencia_generada_en_velocidad(velocidad, velocidad_viento, potencia, optimal_epsilon):
    # Crear la función RBF con los parámetros óptimos
    rbf = Rbf(velocidad_viento, potencia, function='multiquadric', epsilon=optimal_epsilon)
    # Evaluar la función RBF en la velocidad dada
    potencia_estimada = rbf(velocidad)
    return potencia_estimada



## Definición de las FDP
def obtener_VELV():
    R = random.uniform(0.0000005, 1)  
    VEL = 14.2 - 0.0000017 * math.sqrt(9.92016e13 - 4.19716e12 * math.log(1.829920032919027e10 * R))
    return round(VEL, 2)

def obtener_VELVT():
    R = random.uniform(0,1)
    VEL =  (8.2 + 0.00024 * math.sqrt(2.56e10 - 7.4018e8 * math.log(1.042641726081656e15 * R)))
    return round(VEL, 2)

def obtener_potencia(velocidad_dada):
  potencia_estimada = round(int(potencia_generada_en_velocidad(velocidad_dada, velocidad_viento, potencia, optimal_epsilon)),2)
  if (potencia_estimada < 2):
    potencia_estimada = 0
  return potencia_estimada

def obtener_EGPS():
    R = random.uniform(0, 1)
    EGPS = 21 + 0.0000038 * math.sqrt(9.92013e13 - 4.19721e12 * math.log(1.829920032919018e10 * R)) 
    return round(EGPS, 2)

def obtener_DEC():
    R = random.uniform(0.0005, 0.5) 
    DEC = 100 + (0.000005929 * math.sqrt(58.48079e8 * R - 0.1181e8 * R**2)) / R
    return round(DEC, 2)

## Calculo de Resultados
def calculo_de_resultados():
    global PMEGMV, PMEGPS, PPENCD, PPEANCD, PMEPE, COSTOS, CANTMV, COSTOMV, CANTPN, COSTOPN

    PMEGMV = round((SEGM/T) *30, 2)
    PMEGPS = round((SEGP/T) *30, 2)
    PPENCD = round((CDISA/T) * 100, 2)
    PPEANCD = round((CDI/T) * 100, 2)
    PMEPE = round( (DESP/T) * 30, 2)
    COSTOS = COSTOMV * CANTMV + COSTOPN * CANTPN

## Impresión de Resultados
def impresion_de_resultados():
    print("\n\n### Resultados ###\n\n")
    print(f"Cantidad de molinos de viento: {CANTMV}")
    print(f"Cantidad de paneles solares: {CANTPN}")
    print(f"Cantidad de almacenamiento de energia electrica: {CAAEE} MW\n")

    print(f"Promedio Mensual de Energía Generada por Molinos de Viento: PMEGMV = {PMEGMV} MW")
    print(f"Promedio Mensual de Energía Generada por Paneles Solares: PMEGPS = {PMEGPS} MW")
    print(f"Promedio Mensual de Energía Generada en Total: PMEGT = {round(PMEGMV + PMEGPS, 2)} MW")
    print(f"Porcentaje de días en el que la Producción Energética del día no logró cubrir la demanda de la ciudad: PPENCD = {PPENCD} %")
    print(f"Porcentaje de días en que la Producción energética del día y la energía almacenada no lograron cubrir la demanda de la ciudad: PPEANCD = {PPEANCD} %")
    print(f"Promedio Mensual de Excedente de Producción Energética Desperdiciada: PMEPE = {PMEPE} MW")
    print(f"El Costo total para implementar el Parque Renovable es de {COSTOS} U$")


## Ejecución de la simulación
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

    calculo_de_resultados()
    impresion_de_resultados()

def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")


# Cosa de python que no importa
if __name__ == "__main__":
    main()
