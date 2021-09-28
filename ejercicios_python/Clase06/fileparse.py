# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:15:45 2021

@author: User
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            #Para hacer la selección correctamente, tenés que convertir 
            #los nombres de las columnas listadas en select a índices (posiciones) de columnas en el archivo.
            encabezados = select
            
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            if has_headers:  
                if indices:
                    fila = [fila[index] for index in indices]
                
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]

                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                    t = (fila[0], fila[1])
                else:
                    t = (fila[0], fila[1], fila[2] )
                registros.append(t)    
        
        
        return registros                

 #%%
camion = parse_csv('../Data/camion.csv', types=[str, int, float])
camion1 = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones'])
camion2 = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones'], types=[str, float])
camion3 = parse_csv('../Data/camion.csv', types=[str, float], has_headers=False)