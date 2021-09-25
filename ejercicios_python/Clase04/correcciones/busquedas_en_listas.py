# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:41:42 2021

@author: User
"""

##############################################################################
#  reciba una lista y un elemento y devuelva la posición de la última aparición
# de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
##############################################################################

def buscar_u_elemento(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
        else:
            continue    # y salimos del ciclo
    return pos

##############################################################################
# reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista
##############################################################################

def buscar_n_elemento(lista, e):
    pos = 0  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos += 1  # contamos las veces que aparece
        else:
            continue    # y salimos del ciclo
    return pos

##############################################################################
# busque el valor máximo de una lista de números positivos
##############################################################################

def maximo(lista):
    # Funciona para listas con valores, no funciona para listas vacías
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    conta = 0
    v1 = ''
    if conta < len(lista):
        v1 = lista[conta] #Capturo el primer valor lista
    
    while conta < len(lista): # Recorro la lista y voy guardando el mayor
        print(lista[conta])
        conta2 = conta + 1
        conta += 1
        if conta2 < len(lista): # verifico que estoy dentro de los indices de lista
            if v1 < lista[conta2]: # lo comparo
              v1 = lista[conta2] # Guardo valor
              print('mejor', lista[conta2])
            else:
                continue
        else:
            continue
        
       
    return v1

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    conta = 0
    v1 = ''    
    if conta < len(lista):
        v1 = lista[conta] #Capturo el primer valor lista
        
    while conta < len(lista): # Recorro la lista y voy guardando el mayor
        conta2 = conta + 1
        conta += 1
        if conta2 < len(lista): # verifico que estoy dentro de los indices de lista
            if v1 > lista[conta2]: # lo comparo
               v1 = lista[conta2] # Guardo valor
               
            else:
                continue
        else:
            continue
        
        
    return print(v1)

