# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:46:33 2021

@author: PC
"""

#Ejercicio 2.18: Balances

print ('\n Ejercicio 2.18\n')

#Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
# juntá las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión  y los de venta en el negocio 
# calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

import csv

def leer_camion (archivo):
    with open(archivo, 'rt') as f:
       camion = []
       next(f) 
       rows = csv.reader(f)# para saltear la primer fila
       for row in rows:
           lote = (row[0], int(row[1]), float(row[2]))
           camion.append(lote)
       return camion

costo_camion = 0.0
camion= (leer_camion ('../Data/camion.csv')) 

def leer_camion_dic (archivo):
    with open(archivo, 'rt') as f:
       camion= []
       next(f) 
       rows = csv.reader(f)# para saltear la primer fila
       for row in rows:
           lote= {'nombre': row[0], 'n_cajones': int(row[1]), 'precio': float(row[2])}
           camion.append (lote)
       return camion

for nombre, cajones, precio in camion:
    costo_camion += cajones*precio
print('El costo total del camion fue de $ ' + str(costo_camion))

def leer_precios (archivo):
    with open(archivo, 'rt') as f:
       precio = []
       rows = csv.reader(f)
       for row in rows:
          if len(row)>1: #Control de index out of range
              fruta = (row[0], float(row[1]))
              precio.append(fruta)
          else:
              continue

       return dict(precio)

def fruta_cajon_camion (archivo_camion): #lista de fruta y n_cajones del camion
    camion = leer_camion (archivo_camion)
    fruta_cajon_camion=[] 
    for row in camion:
        fruta= {'nombre': row[0], 'n_cajones': float(row[1])} #cambié int a float
        fruta_cajon_camion.append(fruta)
    return  fruta_cajon_camion


precios_dic= leer_precios('../Data/precios.csv')   
camion_lista=  leer_camion ('../Data/camion.csv')       

precios_venta= 0.00

for row in camion:
    if row[0] in precios_dic:
        precios_venta += (float(precios[row[0]]) * row[1]) # el precio de la fruta * el n de cajones
            
print ('\nEl vendedor recaudó $ ' + str(precios_venta))    

balance = round((precios_venta) - (costo_camion), 2)
        
print('\nEl Balance del vendedor es de $ ' + str(balance))    

if precios_venta > costo_camion:
    print ('\nEl vendedor tuvo ganancias por la venta de frutas')
elif precios_venta == costo_camion:
    print('\nEl vendedor saldó sus gastos')
else:
    print('\nEl vendedor fue a pérdida')
    