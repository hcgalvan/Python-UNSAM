# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:06:15 2021

@author: User
"""


#%%
import random
for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}', end=', ')
#%%
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.shuffle(naipes)
print(naipes)
#%%
#Observá que la función shuffle() modificó la lista que le pasamos como parámetro. 
#Una vez mezclado el mazo, podemos consultar las tres cartas que quedaron al final: 
print(naipes[-3:])
#%%
# o directamente sacarlas del mazo:
n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')

#%%
#Por definición pi es el área del círculo de radio uno. Si generamos puntos (x,y) con:
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y
#%%
print(generar_punto())
#%%
# La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades.
#Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así:
for i in range(6):
        print(f'{random.normalvariate(0,1):.2f}', end=', ')
