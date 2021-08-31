# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:18:36 2021

@author: User
"""
#########
# Asignaciones
'''
a = valor         # Asignación a una variable
s[n] = valor      # Asignación a una lista
s.append(valor)   # Agregar a una lista
d['key'] = valor  # Agregar a una diccionario

'''
#%%
a = [1,2,3]
b = a
c = [a,b]
print (c)
a.append(999)
print(b)
print(c)

#%%
# Reasignar valores
a = [1,2,3]
b = a
a = [4,5,6]

print(a)      # [4, 5, 6]
print(b)      # [1, 2, 3]

#%%
# Identidad y referencias
a = [1,2,3]
b = a
print(a is b)

print(id(a))
print(id(b))

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c) ## es algo inesperado porque deberia dar true
print(a == c) ## es lo mas usual

#%%
# Copias superficiales

a = [2,3,[100,101],4]
b = list(a) # Hacer una copia
print(a is b)

a.append(5)
print(a)
print(b)
#%%
a[2].append(102)

print(b[2])

print(a[2] is b[2])

#%%
## Copias profundas

a = [2,3,[100,101],4]
print(a)
import copy
b = copy.deepcopy(a)
print(b)
a[2].append(102)
print(a)
b[2]
print(a[2] is b[2])
#%%
# Nombre, valores y tipos

a = 42
b = 'Hello World'
print(type(a))
print(type(b))
#%%
## Verificación de tipos
if isinstance(a, list):
    print('a es una lista')
#%%
if isinstance(a, (list,tuple)):
    print('a una lista o una tupla')

#%%
# Todo es un objeto    
import math
items = [abs, math, ValueError ]
print(items)

print(items[0](-45))
print(items[1].sqrt(2))
#%%
try:
    x = int('not a number')
except items[2]:
   print('Failed!')
#Failed!
#%%
types = [str, int, float]
import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
#%%
row[1] * row[2]

#%%
print(types[1])

print(row[1])
print(types[1](row[1]))     # Es equivalente a int(row[1])
print(types[2](row[2]))
#%%
print(types[1](row[1])*types[2](row[2]))
#%%
# Hagamos un Zip de la lista de tipos con la de datos y veamos el resultado:
r = list(zip(types, row))
print(r)
#%%
converted = []
for func, val in zip(types, row):
    converted.append(func(val))

print(converted)    
print(converted[1] * converted[2])
#%%
converted = [func(val) for func, val in zip(types, row)]
print(converted)
#%%
print(headers)
print(converted)
print(dict(zip(headers, converted)))
#%%
# Si estás en sintonía con la comprensión de listas podés escribir una sola línea usando comprensión de diccionarios:
print({ name: func(val) for name, func, val in zip(headers, types, row) })

#%%
# Ejercicio 4.14: Fijando ideas
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
print(headers)
#%%
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
print(converted)
record = dict(zip(headers, converted))
print(record)










