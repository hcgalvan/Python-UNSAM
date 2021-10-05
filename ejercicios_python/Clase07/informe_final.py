# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:35:41 2021

@author: User
"""
# Desde tabla_informe.py
from fileparse import parse_csv

def leer_camion(nombre_archivo):
   
    with open(nombre_archivo) as lines:
       #lines = csv.reader(f)
       camion = parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
       #camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

    return camion

def leer_precios(nombre_archivo):

    with open(nombre_archivo) as lines:
       #lines = csv.reader(f)
       precios = dict(parse_csv(lines, types = [str, float], has_headers = False))
 
       #precios = dict(parse_csv(nombre_archivo, types = [str, float], has_headers = False))
    
    return precios

def imprimir_informe(informe):
    
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
    return

def informe_camion(camion, precios):
    
    camion_ = leer_camion(camion)
    precios_ = leer_precios(precios)
    
    lista = []
    i = 0
    for lote in camion_:
        n = precios_[lote['nombre']]
        if i < n :
            precio_venta = precios_[lote['nombre']]
            cambio = precio_venta - lote['precio']
            t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
            lista.append(t)
        else:
            continue            
    imprimir_informe(lista)
    return lista

def f_principal(parametros):
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    precios = parametros[2]
    informe_camion(camion, precios)
    return

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    