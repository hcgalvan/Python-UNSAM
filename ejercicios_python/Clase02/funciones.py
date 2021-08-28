# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:06:13 2021

@author: Hugo César Galván
"""
#%%
def sumcount(n):
    '''
    devuelve los primeros enteros

    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
#%%
a = sumcount(100)
print(a)

#%% Funciones de Biblioteca
import math
x = math.sqrt(10)
print(x)

import urllib.request
u = urllib.request.urlopen('http://python.org/')
data = u.read()
print(data)

#%% Errores y excepciones
int('N/A')
#%% Atrapar y administrar excepciones
numero_valido = False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')
#%% Errores y excepciones
raise RuntimeError('Que moco!')
#%% Ejercicio 2.5
def saludar(nombre):
    'Saluda a alguien'
    print('hola', nombre)
#%% 
saludar('Guido')
saludar('Paula')

help(saludar)


