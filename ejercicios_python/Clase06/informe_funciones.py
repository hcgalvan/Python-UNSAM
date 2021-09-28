#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:34:08 2021

@author: mcerdeiro
"""
# Desde tabla_informe.py
from fileparse import parse_csv
def leer_camion(nombre_archivo):
   
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

    return camion

def leer_precios(nombre_archivo):

    precios = dict(parse_csv(nombre_archivo, types = [str, float], has_headers = False))
    
    return precios

def hacer_informe(camion, precios):
    lista = []
    i = 0
    for lote in camion:
        n = precios[lote['nombre']]
        if i < n :
            precio_venta = precios[lote['nombre']]
            cambio = precio_venta - lote['precio']
            t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
            lista.append(t)
        else:
            continue            
    return lista

#%%
camion = leer_camion('../Data/fecha_camion.csv')
#%%
precios = leer_precios('../Data/precios.csv')
#%%
dato = hacer_informe(camion, precios)