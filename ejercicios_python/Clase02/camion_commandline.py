# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:48:15 2021
Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author: Hugo César Galván
"""

#%% Fui agregando funcion, control de errores
import csv
import sys
import re

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    valor_total = 0
    for line in rows:
        try:
            precio = line[2:]
            precio = precio[0]
            precio = re.sub(r'(\n)', r'', precio)
            cajon = line[1::2]
            cajon = cajon[0]
            valor_total += int(cajon)*float(precio)
        except ValueError:
            print('Cuidado, faltan valores')
            continue
    f.close()
    return valor_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

#%%
costo = costo_camion(nombre_archivo)
print('Costo total', costo)

"""
Salida:
    
Costo total 47671.15

"""