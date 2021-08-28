# -*- coding: utf-8 -*-
"""
Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author:  Hugo César Galván


"""
#informe.py
"""
Realiza el balance de las operaciones en frutería en base a los
precios y el valor de cada fruta por cajón
"""
import csv
# Armamos un diccionario con cada tipo de 
def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    camion = []
    lote = {}
    for row in rows:
        lote ['nombre'] = row[0]
        lote ['cajones'] = int(row[1])
        lote ['precio'] = float(row[2])
        camion.append(lote)
        lote = {}
    f.close()
    return camion


def leer_precios(nombre_archivo):
    dic_precio = {}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1:
            dic_precio[row[0]] = float(row[1])
        else:
            continue
    return dic_precio
    f.close()   

def balance (camion, precios):
    camion = leer_camion(camion)
    costo_total = 0
    precios = leer_precios(precios)
    venta = 0
    costo_unit = 0
    vta_unit = 0
    ganancia = 0
    gcia_total = 0
    for row in camion:
        #print (row['nombre'],row['precio'])
        for k, v in precios.items():
            if row['nombre'] == k:
                #print (k,'=',v, row['nombre'],row['precio'])
                costo_unit = (int(row['cajones'])*float(row['precio']))
                vta_unit = int(row['cajones'])*float(v)
                ganancia = vta_unit - costo_unit
                costo_total += costo_unit
                venta += vta_unit
                gcia_total += ganancia
                print (f'fruta: {k} Costo: {costo_unit:0.2f} Venta: {vta_unit:0.2f} Ganancia: {ganancia:0.2f}')
            else:
                continue
    return print(f'Costo Total: {costo_total:0.2f} Vta Total: {venta:0.2f} Ganancia: {gcia_total:0.2f}')
#%%
print ( balance('../Data/camion.csv', '../Data/precios.csv'))

"""
Salida :
    
fruta: Lima Costo: 3220.00 Venta: 4022.00 Ganancia: 802.00
fruta: Naranja Costo: 4555.00 Venta: 5314.00 Ganancia: 759.00
fruta: Caqui Costo: 15516.00 Venta: 15819.00 Ganancia: 303.00
fruta: Mandarina Costo: 10246.00 Venta: 16178.00 Ganancia: 5932.00
fruta: Durazno Costo: 3835.15 Venta: 6980.60 Ganancia: 3145.45
fruta: Mandarina Costo: 3255.00 Venta: 4044.50 Ganancia: 789.50
fruta: Naranja Costo: 7044.00 Venta: 10628.00 Ganancia: 3584.00
Costo Total: 47671.15 Vta Total: 62986.10 Ganancia: 15314.95
"""