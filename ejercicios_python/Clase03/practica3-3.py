# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:20:03 2021

@author: User
"""
#%%
a = 'Hello'               # String o cadena
b = [1, 4, 5]             # Lista
c = ('Pera', 100, 490.1)  # Tupla
print(a, b, c)
#%%
# Orden indexado
print(a[0])                      # 'H'
print(b[-1])                     # 5
print(c[1])                      # 100
#%%
# Longitud de secuencias
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3

#%%
#Las secuencias pueden ser replicadas
print(a*3)
#%%
# Las secuencias del mismo tipo también pueden ser concatenadas
a = (1, 2, 3)
b = (4, 5, 6)
print(a+b)
#%%
# Rebanadas (slicing)
a = [0,1,2,3,4,5,6,7,8]
print(a[2:5])
print(a[2:])
#%%
# Reasigación de rebanadas
a = [0,1,2,3,4,5,6,7,8]
a[3:4]=[10,10]
print(a)
#%%
# Reducciones de secuencias
s = [1, 2, 3, 4]
print (sum(s))
print(min(s))
print(max(s))
#%%
#Iterar sobre una secuencia
s = [1, 4, 9, 16, 19]
for i in s:
    print(i)
#%%
# El comando break    
for i, ss in enumerate(s):
    print(i, ss)
    if ss == 9:
        print('cruzo por aqui')
        break #no rompe el ciclo superior si existen varios for
    else:
        print(f'no tiene aqui el {ss}')
        # break en la 1era ya sale del ciclo for
        
    
#%%
# El comando continue

#%%
# Ciclos sobre enteros
# for i in range(100):
    # i = 0,1,...,99
# for j in range(10,20):
    # j = 10,11,..., 19
  
# for k in range(10,50,2):
    # k = 10,12,...,48
    # Observá que va de a dos.
  
#%%
# La función enumerate()
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    print(i, nombre)
#%%
with open('../Data/precios.csv') as f:
    for nlinea, line in enumerate(f, start=0):
        print(nlinea, line)
#%%
# Tuplas y ciclos for
# Podés iterar con múltiples variables de iteración.
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    print(x, y)
#%%
# La función zip()
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
for columnas, valores in pares:
    print(columnas, valores)

#%%
# Un uso frecuente de zip es para crear pares clave/valor y construir diccionarios.
columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
d = dict(zip(columnas, valores))
items = d.items() # trabajar con claves y valores simultáneamente es usar el método items()
print(d)
print(items)
for k in d: # itera solo los indices
       print('k =', k)

for k, v in d.items(): # es para iterar con diccionario y ver sus valores
    print(k, '=', v)
#%%
# Ejercicio 3.6: Contar
for n in range(10):
    print(n, end='-')
#%%
for n in range(10, 0, -1):
    print(n, end= '*')
#%%
for n in range(0,10,2):
    print(n, end='/')
#%%
# Ejercicio 3.7: Más operaciones con secuencias
data = [4, 9, 1, 25, 16, 100, 49]
print(min(data), max(data), sum(data))
#%%
# Probá iterar sobre los datos.
for x in data:
    print(x)
#%%
for n, x in enumerate(data):
    print(n, x)
#%%
# A veces los comandos for, len(), y range() son combinados para recorrer listas:
for n in range(len(data)):
    print(data[n])
#%%
# Ejercicio 3.8: Un ejemplo práctico de enumerate()    
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
encabezados= next(filas)
fila = next(filas)
# print(encabezados)
print(list(zip(encabezados,fila)))
#%%
# Este apareamiento es un paso intermedio para construir un diccionario. Probá lo siguiente:
record = dict(zip(encabezados,fila))
print(record)
#f.close()
#%%
# Ejercicio 3.10: Invertir un diccionario
precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
print(precios.items())
#%%
lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)
#%%
print(min(lista_precios))
print(max(lista_precios))
print(sorted(lista_precios))
#%%
# zip() se detiene cuando la más corta de las entradas se agota.
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))

