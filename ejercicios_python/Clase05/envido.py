# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:51:01 2021

@author: User
"""
# La última función que queremos introducir es útil en muchos contextos. 
# En los juegos de naipes, para continuar con nuestro ejemplo, es muy usual mezclar
#  el mazo entero antes de repartir. 

# Valores discretos

import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.shuffle(naipes)
print(naipes)

print(naipes[-3:])

#%%
# o directamente sacarlas del mazo:
n1 = naipes.pop()
n2 = naipes.pop()
n3 = naipes.pop()
print(f'Repartí el {n1[0]} de {n1[1]}, el {n2[0]} de {n2[1]} y el {n3[0]} de {n3[1]}. Quedan {len(naipes)} naipes en el mazo.')

#%%
#############################
# Valores continuos
#############################
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

#%%
print( generar_punto())
