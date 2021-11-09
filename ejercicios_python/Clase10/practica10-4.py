# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:32:18 2021

@author: User
"""

# Productores, consumidores y cañerías
def productor():
    ...
    yield item          # yield devuelve un item que será recibido por `procesamiento`
    ...

def procesamiento(s):
    for item in s:      # item viene del `productor`
        ...
        yield newitem   # este yield devuelve un nuevo item
        ...

def consumidor(s):
    for item in s:      # item viene de `procesamiento`
        ...
        

#%% funciona un pipeline.
# No abre un archivo sino que opera directamente 
# de una secuencia de líneas que recibe como argumento.
from vigilante import vigilar
def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
        print(line)

#... esperá que aparezca la salida ...
#%% Ejercicio 10.9: Un pipeline más en serio
from vigilante import vigilar
import csv
lines = vigilar('../Data/mercadolog.csv')
rows = csv.reader(lines)
for row in rows:
        print(row)

# ¡Interesante! La salida de la función vigilar() fue usada como entrada a la función csv.reader() 

#%% Ejercicio 10.11: Filtremos los datos
def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
rows = filtrar_datos(rows, camion)
for row in rows:
    print(row)

#%% Ejercicio 10.12: El pipeline ensamblado




