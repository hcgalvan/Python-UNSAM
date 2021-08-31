# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:35:10 2021

@author: User
"""

nombres = ['Edmundo', 'Juana']
a = [nombre.lower() for nombre in nombres]
print(a)
#%%

a = [1, -5, 4, 2, -2, 10]
b = [2*x for x in a if x > 0]
print(b)

#%%
#Casos de uso

frutas = [s['nombre'] for s in camion]
a = [s for s in camion if s['precio'] > 100 and s['cajones'] > 50]
costo = sum([s['cajones']*s['precio'] for s in camion])
print (costo)
#%%
# Ejercicio 4.8: Reducción de secuencias
#######################
camion = leer_camion('../Data/camion.csv')
costo = sum([s['cajones'] * s['precio'] for s in camion])
print(costo)

#%%
precios = leer_precios('../Data/precios.csv')
valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
print(valor)
#%%
print([s['cajones'] * s['precio'] for s in camion])

print(sum([s['cajones'] * s['precio'] for s in camion]))

#%%
# Ejercicio 4.9: Consultas de datos
mas100 = [s for s in camion if s['cajones'] > 100]
print(mas100)

#%%
# Ahora, una con la info sobre cajones de Mandarina y Naranja.
myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]
print( myn )
#%%
# O una con la info de las frutas que costaron más de $10000.
costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
print(costo10k)

#%%
# Si cambiás los corchetes ([,]) por llaves ({, }), 
# obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.
nombres = {s['nombre'] for s in camion}
print (nombres)

#%%
# Si especificás pares clave:valor, podés construir un diccionario.

stock = {nombre: 0 for nombre in nombres}
print (stock)

#%%
## Ejercicio 4.11: Extraer datos de un archivo CSV
##################

import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
select = ['nombre', 'cajones', 'precio']
print(select)
indices = [headers.index(ncolumna) for ncolumna in select]
print(indices)

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}   # comprensión de diccionario
print(record)
#%%
camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
print (camion)