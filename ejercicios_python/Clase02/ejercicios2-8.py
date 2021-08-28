# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:19:30 2021

@author: User
"""
#Ejercicio 2.8
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

#%%
preguntar_edad('Hugo')
#%%
#Ejercicio 2.8
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')
#%%
# ¿Qué pasa si intentás usar la función costo_camion() con un archivo que tiene datos faltantes?
    