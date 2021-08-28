# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:51:08 2021
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, 
y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo como punto flotante, usá float(s).
Tu programa debería imprimir una salida como la siguiente:
Costo total 47671.15
Acordate de guardar tu archivo en el directorio Clase02; vamos a volver a trabajar sobre él.

Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author: Hugo César Galván

"""
#%% Fui agregando funcion, control de errores
import csv
import re
def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    valor_total = 0
    for line in rows:
        try: #Control de registros vacíos en cualquier punto del archivo
            precio = line[2:]
            precio = precio[0]
            precio = re.sub(r'(\n)', r'', precio)
            cajon = line[1::2]
            cajon = cajon[0]
            valor_total += int(cajon)*float(precio)
        except ValueError:
            print('Cuidado, faltan valores')
            continue
    f.close()
    return valor_total

#%%
costo = costo_camion('../Data/missing.csv') #Aqui utilizo missing puede ser camion
print('Costo total', costo)

"""
Salida: utilizando missing.csv
    
Cuidado, faltan valores
Cuidado, faltan valores
Costo total 30381.15

"""


    
    

