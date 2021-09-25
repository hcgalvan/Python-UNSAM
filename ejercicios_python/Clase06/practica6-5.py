# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:13:52 2021

@author: User
"""
# Búsqueda sobre listas ordenadas
# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

''' 
Pregunta: 
    En la línea medio = (izq + der) // 2 efectuamos la división usando el operador // en lugar de /. 
    ¿Qué pasaría su usáramos /?
'''
#%%
# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas
#       En el peor caso, 
#         ¿cuál es nuestra nueva hipótesis sobre comportamiento del algoritmo? 
#         ¿Es realmente más eficiente?
# Ejercicio 6.14: Búsqueda binaria
# Guarda tu modificación en un archivo bbin.py

