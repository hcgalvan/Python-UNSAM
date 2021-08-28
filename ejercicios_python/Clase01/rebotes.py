"""
# rebotes.py
# Ejercicio 1.5
@author: Hugo César Galván
"""
# Ejercicio
altura = 100
toca_piso = 1
rebota = (100*.6)

#solicito que imprima al menos 10 veces los rebotes
while toca_piso <= 10:
    print(round(rebota, ndigits=4))
    toca_piso = toca_piso + 1
    rebota = rebota * 0.6
    
"""
resultado:
    60.0
    36.0
    21.6
    12.96
    7.776
    4.6656
    2.7994
    1.6796
    1.0078
    0.6047
"""