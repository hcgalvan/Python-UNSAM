# -*- coding: utf-8 -*-
"""
# Geringoso.py
# Ejercicio 1.18
# @author: hcgalvan@gmail.com
"""
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    if c in 'aeiou':
       capadepenapa += c+'p'+c
    else:
         capadepenapa += c
         
print(capadepenapa)

"""
resultado:
    Geperipingoposopo
"""
#%%
cadena = input("Coloque su palabra: ")
capadepenapa = ''
for c in cadena:
    if c in 'aeiou':
       capadepenapa += c+'p'+c
    else:
         capadepenapa += c
         
print(capadepenapa)
