# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:19:38 2021

@author: User
"""
# 7.4 Cuestiones de diseño
# Archivos versus iterables
# Compará estos dos programas que resultan en la misma salida.

# Necesita el nombre de un archivo
def read_data(nombre_archivo):
    records = []
    with open(nombre_archivo) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')

# Necesita líneas de texto
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
    
# ¿Cuál de las funciones read_data() preferís y por qué?
# ¿Cuál de las funciones permite mayor flexibilidad?

#%% Una idea profunda: "Duck Typing" (Identificación de patos)
#  "Test del pato" es un concepto usado en programación para determinar si un objeto puede ser usado para un propósito en particular.
# Si algo se parece a un pato, nada como un pato, y hace el mismo ruido que un pato, entonces probablemente se trate de un pato.
# esta segunda versión funciona con cualquier iterable.
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
# Esto implica que la podemos usar con otro tipo de líneas, no necesariamente archivos.

# Ejemplos:
# Un archivo .csv
lines = open('data.csv')
data = read_data(lines)

# Un archivo zipeado 
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# La entrada estándar (Standard Input), por teclado
lines = sys.stdin
data = read_data(lines)

# Una lista de cadenas
lines = ['Quinoto,50,91.1','Naranja,75,123.45', ... ]
data = read_data(lines)

#%%
lines = open('data.csv')
lines = gzip.open('data.csv.gz','rt')
lines = sys.stdin
lines = ['Quinoto,50,91.1','Naranja,75,123.45', ... ]
# Pregunta: ¿Debemos favorecer u oponernos a esta flexibilidad?
#%%  Buenas prácticas en el diseño de bibliotecas
# Las bibliotecas de código suelen ser más útiles si son flexibles.
# No restrinjas las opciones innecesariamente. 
# Con mayor flexibilidad suele venir asociada una mayor potencia.
#%% EJERCICIOS
# Ejercicio 7.6: De archivos a "objetos cual archivos"
# Ejercicio 7.7: Arreglemos las funciones existentes
