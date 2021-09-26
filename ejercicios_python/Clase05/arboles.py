# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:46:34 2021

@author: User
"""
#####################################################################
# Escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y 
# devuelva una lista de diccionarios con la información de todos los árboles 
# en el archivo. La función debe devolver una lista conteniendo un diccionario
# por cada árbol con todos los datos.
# Vamos a llamar arboleda a esta lista.
#####################################################################
# long,lat,id_arbol,altura_tot,diametro,inclinacio,id_especie,nombre_com,nombre_cie,tipo_folla,espacio_ve,ubicacion,nombre_fam,nombre_gen,origen,coord_x,coord_y
import csv

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo,encoding="utf8")
    #types = [str, str, str, str, str, str, str, str, str, float, int]
    arboleda = []
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        arbol=({ name: val for name, val in zip(headers, row) })
        arboleda.append(arbol)
    

########################################################
# Ejercicio 4.16: Lista de altos de Jacarandá
# Usando comprensión de listas y la variable arboleda podés por ejemplo 
# armar la lista de la altura de los árboles.
########################################################
    H =[]
    valor = 'Jacarandá'
    H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==valor]
    H
    #    altura.append(H)    
    #return #print(arboleda)

########################################################
# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
# nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto
########################################################
    H1 =[]   
    H1 = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==valor]
    H1
    return arboleda

########################################################
# Ejercicio 4.18: Diccionario con medidas
# recibir un diccionario con tres entradas (una por especie), 
#cada una con una lista asociada conteniendo 4112, 3150 y 3255 pares de números (altos y diámetros), respectivamente.
########################################################
def medidas_de_especies(especies, arboleda):
    
    print(especies)
    headers = especies
    T = []
    H = []
    for i in especies:
        T=[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==i]
        H.append(T)
    diccio = dict(zip(headers,H))
    return diccio   
 #   diccionario = { clave: valor for clave in claves }


#%%
leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

#%%
medidas_de_especies (['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))
#%% Ejercicio 5.25: Histograma de altos de Jacarandás
import os
import matplotlib.pyplot as plt
import numpy as np
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
plt.hist(altos,bins=3)

#%% Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
h = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
d = [float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
h1 = np.array(h)
d1 = np.array(d)
N = len(h)
colors = np.random.rand(N)
area = (10 * np.random.rand(N))**2
plt.scatter(d1,h1, s=area, c=colors, alpha=0.5)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%% Ejercicio 5.27: Scatterplot para diferentes especies
import os
import matplotlib.pyplot as plt

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

