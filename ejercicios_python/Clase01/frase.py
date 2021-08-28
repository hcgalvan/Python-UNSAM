# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:01:39 2021

@author: User
"""

#%%

frase = 'todos somos programadores'
palabras = frase.split()
traduccion = []
for palabra in palabras:
    if palabra [-1] == 'o':
        nueva_palabra = palabra[:-1] +'e'
    elif len(palabra)>1 and palabra [-2] == 'o': #se llama evaluación peresoza porque la segunda proposición te da un error si lo ejecutas solo
        nueva_palabra = palabra[:-2] +'e'+ palabra[-1]
    else:
        nueva_palabra = palabra
    traduccion.append(nueva_palabra)
    #print(palabra, nueva_palabra)

frase_t = ' '.join(traduccion)
print(frase_t)