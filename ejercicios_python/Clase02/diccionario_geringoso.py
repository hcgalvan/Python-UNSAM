# -*- coding: utf-8 -*-
"""

Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author: Hugo César Galván
"""
#%%
def geringoso(palabras):
    largo =len(palabras)
    capadepenapa = ''
    c = 0
    lista = []
    armado = []
    while c < largo:
        palabra = palabras[c]
        palabra.strip()
        for d in palabra:
            if d in 'aeiou':
                capadepenapa += d+'p'+d
            else:
                capadepenapa += d
        lista.insert(c, capadepenapa ) #inserte 1er list = lista que será el valor
        item = (palabras[c], lista[c]) # armé una tupa con palabra (clave) y lista (valor)
        armado.insert(c,item) #inserté esta tupla en un list llamado armado
        capadepenapa = '' # dejo en vacío la variable
        c += 1 
    diccionario = dict(armado) # con lo obtenido en list = armado transformo en diccionario
    return print(diccionario)
#%%
geringoso(['banana', 'manzana', 'mandarina'])

"""
Salida:
    
{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}

"""