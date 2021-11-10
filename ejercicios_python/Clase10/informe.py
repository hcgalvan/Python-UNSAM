
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:53:20 2021

@author: User
"""
# Desde tabla_informe.py
from fileparse import parse_csv
from lote import Lote
import formato_tabla
from camion import Camion

def leer_camion(nombre_archivo):
    '''
    with open(nombre_archivo) as lines:
        camion_dicts = parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion
    
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo) as file:
         camiondicts = parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)

def leer_precios(nombre_archivo):

    with open(nombre_archivo) as lines:
        precios = dict(parse_csv(lines, types = [str, float], has_headers = False))
           
    return precios

def imprimir_informe_1(informe):
    
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
    return

def imprimir_informe_2(data_informe):
    '''
    Imprime una tabla prolija desde una lista de tuplas con (nombre, cajones, precio, cambio) 
    '''
    headers = ('Nombre','Cajones','Precio','Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in data_informe:
        print('%10s %10d %10.2f %10.2f' % row)

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion_1(camion, precios):
    
    camion_ = leer_camion(camion)
    precios_ = leer_precios(precios)
    
    lista = []
    i = 0
    
    for c in camion_:
        n = precios_[c.nombre]
        if i < n :
            precio_venta = precios_[c.nombre]
            cambio = precio_venta - c.precio
            t = (c.nombre, c.cajones, precio_venta, cambio)
            lista.append(t)

    imprimir_informe(lista)
    return

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
    ''' if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}') '''
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
    