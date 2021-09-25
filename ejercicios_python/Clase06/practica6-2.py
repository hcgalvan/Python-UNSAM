# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:51:17 2021

@author: User
"""
# LOS PROBLEMAS. un script útil, éste va a comenzar a crecer en funciones y opciones. 
# Definir nombre. Los nombres deben estar definidos antes de usarse
# El orden importa. Casi siempre definimos las variables y las funciones al comienzo.
import csv
def cuadrado(x):
    return x*x

a = 42
b = a + 2     # Requiere que 'a' haya sido definido antes.

z = cuadrado(b) # Requiere que 'cuadrado' y 'b' estén definidos.
print(z)
#%%
# Definir funciones
def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
#%% El estilo Bottom-Up
# miprograma.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Definida antes
    ...

def spam(x):
    ...
    bar(x)          # Definida antes
    ...

spam(42)            # El código que *usa* la función está al final

#%% Notas sobre el tipo de dato
def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
#%% EJERCICIOS
# Ejercicio 6.4: Estructurar un programa como una colección de funciones
# Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa


