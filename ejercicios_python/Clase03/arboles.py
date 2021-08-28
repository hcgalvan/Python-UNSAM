# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:07:10 2021

@author: User
"""
import csv
def parques(archivo):
    f = open(archivo,encoding="utf8")
    rows = csv.reader(f)
    encabezados = next(rows)
    parque = []
    for n_fila, fila in enumerate(rows, start=1):
        try: #Control de registros vacíos en cualquier punto del archivo
            record = dict(zip(encabezados, fila))
            arbol = {}
            arbol['espacio_ve'] = record['espacio_ve']
            arbol['id_especie'] = record['id_especie']
            arbol['nombre_com'] = record['nombre_com']
            arbol['nombre_cie'] = record['nombre_cie']
            arbol['nombre_fam'] = record['nombre_fam']
            arbol['nombre_gen'] = record['nombre_gen']
            arbol['origen'] = record['origen']
            arbol['tipo_folla'] = record['tipo_folla']
            arbol['altura_tot'] = record['altura_tot']
            arbol['diametro'] = record['diametro']
            arbol['inclinacio'] = record['inclinacio']
            parque.append(arbol)
        except ValueError:
            print('Cuidado, faltan valores')
            continue
    return parque

def leer_parque(nombre_archivo, parque):
    buscar = parques(nombre_archivo)
    headers = ('espacio_ve', 'id_especie', 'nombre_com', 'nombre_cie','nombre_fam','nombre_gen','origen','tipo_folla','altura_tot')
    for lista in buscar:
        if lista['espacio_ve']==parque:
            #print('%2s %2s %2s %2s %2s %2s %2s %2s %2s' % headers)
            #print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')            
            #print(f'{lista[1]:3d} {lista[2]:3s} {lista[3]:3s} {lista[4]:3s} {lista[5]:3s} {lista[6]:3s} {lista[7]:3s} {lista[8]:3d} {lista[9]:3d} {lista[10]:3d}') 
            #print('{id_especie:3s} {nombre_com:3s}'.format_map(lista))
            print(lista)
    return lista

def especies(lista_arboles):
    from collections import Counter
    buscar = parques('../Data/arbolado-en-espacios-verdes.csv')
    arboles = set(lista_arboles)
    especie = Counter()
    for k in buscar:
        if k['nombre_com'] in arboles:
            especie[k['nombre_cie']] += 1 # Cuenta las especies y la cantidad de arboles
        else:
            continue
    print(especie)     
    
def contar_ejemplares(lista_arboles): #No esta terminado
    from collections import Counter
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    buscar = parques(nombre_archivo)
    arboles = set(lista_arboles)
    lugar1 = Counter()
    combinados = Counter()
    lugar1 = leer_parque(nombre_archivo, 'GENERAL PAZ')
    lugar2 = leer_parque(nombre_archivo, 'ANDES, LOS')
    lugar3 = leer_parque(nombre_archivo, 'CENTENARIO')
    especie = Counter()
    for k in buscar:
        if k['nombre_com'] in arboles:
            especie[k['nombre_com']] += 1 # Cuenta las especies y la cantidad de arboles
        else:
            continue
    
    print( especie, lugar1)
    
    return #print(combinados.most_common(5))                
    #especie.most_common(3)

#%%
leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

#%%
especies(['Ciprés','Casuarina','Cedro del Himalaya'])  

#%%
contar_ejemplares(['Ciprés','Casuarina','Cedro del Himalaya'])  