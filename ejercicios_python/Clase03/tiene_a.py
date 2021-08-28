#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:26:30 2021

@author: hcgalvan
Ejercicio 3.1: Semántica¶
¿Anda bien en todos los casos de prueba?
"""
def tiene_a(expresion):
    n = len(expresion)
    valor = expresion.lower()
    i = 0
    cuenta = 0
    while i<n:
        if valor[i] == 'a':
            cuenta += 1
        i = i + 1
    print(f'tiene a la letra "a": {cuenta} veces')
#%%
def tiene_a(expresion):
    n = len(expresion)
    #print(n)
    i = 0
    valor = -1
    valor = expresion.lower().find('a')
    #print(valor)
    if valor >= 0:
        return True
    else:
        return False
        
#%% 
print(tiene_a('UNAM 2020'))
#%%
print(tiene_a('abracadabra'))
#%%
print(tiene_a('La novela 1984 de George Orwell'))


#%%
'''
Ejercicio 3.2: Sintaxis
¿Anda bien en todos los casos de prueba?
'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    valor = expresion.lower()
    while i<n:
        if valor[i] == 'a':
            return True
        i += 1
    return False

#%%
print(tiene_a('UNSAM 2020'))
#%%
print(tiene_a('La novela 1984 de George Orwell'))
#%%
def tiene_uno(expresion):
    n = len(str(expresion))
    cadena = str(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if cadena[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
print(tiene_uno('UNSAM 2020'))
#%%
print(tiene_uno('La novela 1984 de George Orwell'))
#%%
print(tiene_uno(1984))
#%%
'''
Ejercicio 3.4: Alcances
La siguiente suma no da lo que debería:
'''
def suma(a,b):
    return a + b
a = 2
b = 3
c = suma(a,b)
#%%
print(f"La suma da {a} + {b} = {c}")