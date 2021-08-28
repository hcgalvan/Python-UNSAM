# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:28:36 2021

@author: User
"""

#%%
assert isinstance(10, int), 'Necesito un entero (int)'

#%%
def add(x, y):
    assert isinstance(x, int), 'Necesito un entero (int)'
    assert isinstance(y, int), 'Necesito un entero (int)'
    return x + y

#%%
print(add(2,3))
#%%
print(add('2','3'))

#%%
# Ejercicio 4.1: Debugger
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

#%%
rta = tiene_a('palabra')
print(rta)

#%%
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

