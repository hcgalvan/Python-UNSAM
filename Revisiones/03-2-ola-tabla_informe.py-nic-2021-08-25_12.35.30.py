#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:30:35 2021

@author: nicolas
"""
import csv

def leer_camion(nombre_archivo):
    camion_lista = []

    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                camion_lista.append(record)
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return camion_lista


def leer_precios(nombre_archivo):
    diccionario_precios = {}
    with open(nombre_archivo, "rt", encoding = "utf8") as f:
        rows = csv.reader(f)
        for n_row, row in enumerate(rows, start=1):
            try:
                diccionario_precios[row[0]] = float(row[1])
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return diccionario_precios


def hacer_informe(camion, precios):
    lista = []
    cambio = 0
    for c in camion:
        nombre = c["nombre"]
        cajones = int(c["cajones"])
        precio = float(c["precio"])
        
        if nombre in precios:
            cambio = float(precios[nombre]) - precio
            
        camion_tupla = (nombre, cajones, precio, cambio)
        lista.append(camion_tupla)
    
    return lista

    
precios = leer_precios("../Data/precios.csv") #precio de venta
camion_leido = leer_camion("../Data/camion.csv") #precio de compra
informe = hacer_informe(camion_leido, precios)

headers = ("Nombre", "Cajones", "Precio", "Cambio")
encabezado = f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}"
separador = "---------- ---------- ---------- ----------"

print(encabezado,separador, sep="\n")

for nombre, cajones, precio, cambio in informe:
    print(f"{nombre:>10s} {cajones:>10d} {'$' + str(precio):>10s} {cambio:>10.2f}") 