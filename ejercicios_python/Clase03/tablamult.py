# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:28:54 2021

@author: User
"""

def multiplicar():
    headers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ) # lista de Encabezado
    cero = ('0:','0', '0', '0', '0', '0', '0', '0', '0', '0', '0' ) # lista de 1era posicion de ceros
    print ( '%10s %3s %3s %3s %3s %3s %3s %3s %3s %3s' % headers) # Impresion formateada del encabezado
    print ( '----------------------------------------------') # Impresion lineas de division del encabezado
    print ( '%7s %2s %3s %3s %3s %3s %3s %3s %3s %3s %3s' % cero) # Impresion formateado de 1ra posicion de ceros
    conta = 0
    for i in range(1,10,1):
        tabla = []
        conta += 10
        for e in range(i,conta,i):
            tabla.append(e)
        print(f'{i:>6d}:  0 {tabla[0]:3d} {tabla[1]:3d} {tabla[2]:3d} {tabla[3]:3d} {tabla[4]:3d} {tabla[5]:3d} {tabla[6]:3d} {tabla[7]:3d} {tabla[8]:3d}')   
    return
#%%
multiplicar()