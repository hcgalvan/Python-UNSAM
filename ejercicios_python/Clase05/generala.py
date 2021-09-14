# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:13:43 2021

@author: Hugo Cesar Galvan
"""

import random

## Ejercicio 5.1: Generala servida
# devuelva una lista con cinco dados generados aleatoriamente.
##
def tirar():
    listdados = []
    for i in range(5):
        dados = random.randint(1,6)
        listdados.append(dados)
    
    return listdados

def tirar2():
    listdados = []
    for i in range(5):
        dados = random.randint(1,6)
        listdados.append(dados)
    
    return listdados



def es_generala(tirada):
    pos = 0  # comenzamos suponiendo que e no está
    valor = tirada[pos]
    
    for i, z in enumerate(tirada): # recorremos la lista
        if z == valor:   # si encontramos a e
            pos += 1
        else:
            continue    # y salimos del ciclo

    if pos == len(tirada):
        return True
    else:
        return False

# con N repeticiones, para estimar la probabilidad de obtener
# una generala al finalizar una mano de tres tiradas. 
# La función debe devolver un número entre 0 y 1
def prob_generala(N):
    # Estrategia 1, si en 1era tirada
    G = es_generala(tirar())
    G2 = es_generala(tirar())
    if (G/3) == 0:
        for i in range(N):
            G += sum([es_generala(tirar()) for k in range(3)])
    else:    
        for i in range(N):
            G2 += sum([es_generala(tirar2()) for k in range(3)])
            
    if (G/N) == (G2/N):
        print('no tienen diferencias las estrategias 1 y 2')
        return (G/N)
    else:
        if (G/N) > (G2/N):
             print('Mejor estrategia 1: mano con 3 tiradas, volver a tirar')
             return (G/N)
        else:
             print('Mejor estrategia 2: mano con 3 tiradas, continuar con 4 dados')
             return (G2/N)
 


#%%
print(prob_generala(1))

#%%
tirar()

#%%
es_generala(tirar())
#%%
N = 100000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
