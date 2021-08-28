# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:55:42 2021

@author: User
"""

#%%
import csv
dic_precio = {}
def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1:
            dic_precio[row[0]] = float(row[1])
        else:
            continue
    return dic_precio
    f.close()   
#%%
precios = leer_precios('../Data/precios.csv')
print(precios)

