# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:15:45 2021

@author: User
"""

# fileparse.py
import csv
import gzip

def parse_csv(lines, select = None, types = None, has_headers=True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.

    with open(nombre_archivo) as f:
    '''
    filas = csv.reader(lines)
    # Lee los encabezados del archivo

    if has_headers:
        encabezados = next(filas)

    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    registros = []
    #for fila in filas:
        #print(fila)
    for fila in filas:
        if has_headers:
            if indices:
                fila = [fila[index] for index in indices]
            
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]

            registro = dict(zip(encabezados, fila))
            registros.append(registro)

        else:
            if types:
                if len(fila)>1:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    t = (fila[0], fila[1])
                    #dic_precio[row[0]] = float(row[1])
                    registros.append(t)
                    #print(fila)
                else:
                    continue
                 
            else:
                t = (fila[0], fila[1], fila[2] )
                registros.append(t) 
    
        
    return registros
'''
#%%

with open('../Data/missing.csv') as lines:
   #lines = csv.reader(f)
   precios = dict(parse_csv(lines, types = [str, int, float], has_headers = False))

#%%
with open('../Data/missing.csv') as lines:
    #lines = csv.reader(f)
    camion = parse_csv(lines, types = [str, int, float])
'''