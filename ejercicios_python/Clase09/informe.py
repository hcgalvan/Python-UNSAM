# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:53:20 2021

@author: User
"""
# Desde tabla_informe.py
from fileparse import parse_csv
from lote import Lote
import formato_tabla

def leer_camion(nombre_archivo):
   
    with open(nombre_archivo) as lines:
        camion_dicts = parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

def leer_precios(nombre_archivo):

    with open(nombre_archivo) as lines:
        precios = dict(parse_csv(lines, types = [str, float], has_headers = False))
           
    return precios

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def hacer_informe(camion, precios):
    
    lista = []
    i = 0
    
    for c in camion:
        n = precios[c.nombre]
        if i < n :
            precio_venta = precios[c.nombre]
            cambio = precio_venta - c.precio
            t = (c.nombre, c.cajones, precio_venta, cambio)
            lista.append(t)
    return lista

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Elige formato
    formateador = formato_tabla.crear_formateador(fmt)     
    imprimir_informe(data_informe, formateador)

def f_principal(parametros):
    if len(parametros) != 4:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    precios = parametros[2]
    fmt = parametros[3]
    informe_camion(camion, precios, fmt)
    return

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    
