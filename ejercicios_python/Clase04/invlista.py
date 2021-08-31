# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:46:13 2021

@author: User
"""
###############################################
# Ejercicio 4.5: Invertir una lista
#  que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso
###############################################

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        i = lista.index(e) # tomo el valor del indice
        i = len(lista)-i # acumulo el valor
        invertida.append (lista[i-1]) # para obtener el valor debo quitar una posicion, las listas empiezan en cero    
    return invertida




#%%
l = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'] 
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')
#%%
l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')