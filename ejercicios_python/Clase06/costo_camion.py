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

Este programa funciona si estas ubicado en "..\Ejercicio\Clase03\"

@author: Hugo César Galván

"""
#%% 3.8 Fui agregando funcion, control de errores
# Usando enumerate(), modificá tu programa costo_camion.py 
# de forma que imprima un aviso (warning) cada vez que
# encuentre una fila incorrecta.
import csv
def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    encabezados = next(rows)
    valor_total = 0
    for n_fila, fila in enumerate(rows, start=1):
        record = dict(zip(encabezados, fila))
        try: #Control de registros vacíos en cualquier punto del archivo
            cajon = int(record['cajones'])
            precio = float(record['precio'])
            valor_total += int(cajon)*float(precio)
        except ValueError:
            print(f'Fila {n_fila}: No puede interpretar: {fila}')
            continue
    f.close()
    return valor_total

#%%
# costo = costo_camion('../Data/fecha_camion.csv') #Aqui utilizo missing puede ser camion
# print('Costo total', costo)

"""
----------------
Salida: utilizando camion.csv
Costo total 47671.15
----------------
Salida: utilizando missing.csv
    Fila 4: No puede interpretar: ['Mandarina', '', '51.23']
    Fila 7: No puede interpretar: ['Naranja', '', '70.44']
    Costo total 30381.15

"""


    
    

