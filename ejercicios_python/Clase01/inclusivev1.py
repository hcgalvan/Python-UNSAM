# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% nombre del bloque

frase = 'todos somos programadores'
palabras = frase.split()
traduccion = []
for palabra in palabras:
    if palabra [-1] == 'o':
        nueva_palabra = palabra[:-1] +'e'
    elif len(palabra)>1 and palabra [-2] == 'o': 
        # elsif anterior se llama evaluación peresoza porque la segunda proposición te da un error si lo ejecutas solo
        nueva_palabra = palabra[:-2] +'e'+ palabra[-1]
    else:
        nueva_palabra = palabra
    traduccion.append(nueva_palabra)
    #print(palabra, nueva_palabra)

frase_t = ' '.join(traduccion)
print(frase_t)

#%%