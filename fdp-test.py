import math
import random
from scipy.stats import beta
import numpy as np

pi = math.pi
max_val = 0
min_val = float('inf')
promedio = 0


# Parámetros de la distribución
a, b = 305.06, 174.02

# Generar números aleatori


for i in range(5000):
    x = random.uniform(0.0005, 1)  # Ensure x is not too small
    y = 99 + (0.000004929 * math.sqrt(135.48079e8 * x - 0.1181e8 * x**2)) / x
    if y > max_val:
        max_val = y
    if y < min_val:
        min_val = y
    promedio = promedio + y

print("max: ", max_val)
print("min: ", min_val)
print("promedio: ", promedio/i+1)
print("corridas: ", i+1)

#     y =  (8.2 + 0.00024 * math.sqrt(2.56e10 - 7.4018e8 * math.log(1.042641726081656e15 * x)))  VELVT
#     y = 14.2 - 0.0000021 * math.sqrt(9.92016e13 - 4.19716e12 * math.log(1.829920032919027e10 * x))  VELV