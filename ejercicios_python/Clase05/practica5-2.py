# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:57:16 2021

@author: User
"""

import random
######################
# Valores discretos
######################
random.seed(31415)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)

#%%
# La función random.choice() toma una secuencia y devuelve un elemento aleatorio.
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

#%%
# Si queremos realizar múltiples elecciones aleatorias de la lista 
# podemos usar la función random.choices()
print(random.choices(caras,k=5))


#%%
# Ejercicio 5.3: Cocumpleaños

#%%
# Elecciones sin reposición
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

#%%
#  En este caso tenemos que usar elecciones múltiples sin reposición. 
# Para eso usamos la función sample del módulo
random: random.sample(naipes,k=3)

#%%
random.sample(naipes,k=?)