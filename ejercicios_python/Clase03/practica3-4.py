# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:17:33 2021

@author: User
"""

#%%
# 3.4 Contadores del módulo collections
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]
#%%
# existen repetidos utilizamos Counter para combinar
from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

print(total_cajones['Naranja'])
#%%
import csv
# Armamos un diccionario con cada tipo de 
def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    encabezados = next(rows)
    # next(rows)
    camion = []
    lote = {}
    for n_fila, fila in enumerate(rows, start=1):
        record = dict(zip(encabezados, fila))
        lote ['nombre'] = record['nombre']
        lote ['cajones'] = int(record['cajones'])
        lote ['precio'] = float(record['precio'])
        camion.append(lote)      
        lote = {}
    f.close()
    return camion
#%%
camion = leer_camion('../Data/camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias)
#%%
print(tenencias['Naranja'])
print(tenencias['Mandarina'])
print(tenencias.most_common(3))
#%%
camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']
print(tenencias2)
#%%
# Y finalmente combinemos las tenencias de ambos camiones con una
combinada = tenencias + tenencias2
print(combinada)
