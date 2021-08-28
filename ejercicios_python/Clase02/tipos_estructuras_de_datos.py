# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:29:32 2021

@author: User
"""

email_address = None
if email_address:
    send_email(email_address, msg)

#Tuplas es como la fila de una base de datos y estan ordenadas como en las listas
s = ('Manzanas', 100, 490.1)
nombre = s[0]
cantidad = s[1]
precio = s[2]
print(nombre)
s = (s[0], 75, s[2]) #
#%% desempaquetar una tupla se hace con variables
fruta, cajones, precio = s

#%% arroja error porque no es la misma cantidad de variables que la estructura de la tupla
fruta, cajones = s
#%% tupla vs listas
record = ('Manzanas', 100, 490.1) # es una tupla se usan para un solo items
symbols = ['Manzanas','Peras','Mandarinas'] # es una lista, se usan para coleccion de diferentes elementos
#%% Diccionarios es una funcion que manda claves
s = {
     'fruta':'Manzana',
     'cajones': 100,
     'precio': 490.1
     }
#%% Operaciones con diccionarios
print(s['fruta'],s['cajones'])
s['precio']
#%% Agregar o modificar valores de diccionarios
s['cajones'] = 75
s['fecha'] = '6/8/2020'
print(s['fecha'])
#%%
del s['fecha']
#%%
print(s['precio']) #diccionario
print(symbols[1]) #lista

#%%

#%% EJERCICIO 2.11
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
next( filas )
#%%
fila = next(filas)
print(fila)
#%%
t = (fila[0], int(fila[1]), float(fila[2]))
print(t)
#%%
cost = t[1]*t[2]
print(cost)
#%%
print(f'{cost:0.2f}')
#%%
t = (t[0], 75, t[2])
print(t)
#%% desempaquetar la tupla
nombre, cajones, precio = t
print(nombre)
#%%
print(cajones, precio)
#%% Empaquetar la tupla
t = (nombre, 2*cajones, precio)
print(t)
#%%
f.close()
#%% EJERCICIO 2.12 Diccionarios como estructuras de datos
d = {
     'nombre': fila[0],
     'cajones': int(fila[1]),
     'precio': float(fila[2])
     }
print(d)
#%%
cost = d['cajones']*d['precio']
print(cost)
#%% cambia el numero de cajones, los diccionarios permiten modificar los valores libremente
d['cajones'] = 75
print(d)
#%%
d['fecha'] = (14, 8, 2020)
d['cuenta']= 12345
print(d)
#%% EJERCICIO 2.13
for k in d:
    print('k =', k)

#%%
for k in d:
    print(k,'=',d[k])
    
#%%
items = d.items()
print(items)
#%%
for k, v in d.items():
    print(k, '=', v)
#%% pasar un diccionario a lista
list(d)
#%%
print(list(d))
#%% obtener las claves del diccionario con metodo keys()
claves = d.keys()
print(claves)
#%% crear diccionario usando dict()
nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
print(nuevos_items)
#%%
d = dict(nuevos_items)
print(d)
