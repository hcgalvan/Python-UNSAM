# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:55:52 2021

@author: User
"""
import informe_final

from vigilante import vigilar
from formato_tabla import crear_formateador

import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

# Convertimos los tipos de datos a diccionarios
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows    

def ticker(cam, merclog, formato):
    camion = cam
    merclog = merclog
    fmt = formato
    data_c = informe_final.leer_camion(camion)
    data_m = parsear_datos(vigilar(merclog))
    
    formateador = crear_formateador(fmt)     
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    #rows = filtrar_datos(data_m, data_c)
    rows = (fila for fila in data_m if fila['nombre'] in data_c)    
    
    
    for row in rows:
        precio = row['precio']
        rowdata = [row['nombre'], f'{precio:0.2f}', str(row['volumen'])]
        formateador.fila(rowdata)
    
def f_principal(parametros):
    if len(parametros) != 4:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    camion = parametros[1]
    merclog = parametros[2]
    fmt = parametros[3]
    ticker(camion, merclog, fmt)
        
    return

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

