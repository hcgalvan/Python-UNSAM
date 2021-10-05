# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:07:10 2021

@author: User
"""
import csv
from collections import Counter

############################################################
# Ejercicio 3.18: Lectura de los árboles de un parque.
############################################################

def leer_parque(nombre_archivo, parque):
    ''' 
    El nombre de archivo tiene que tener la ubicacion del archivo "../Data/" 
    '''
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    encabezados = next(rows)
    #busca = [parques]
    arboles = []
    # for k in busca:
    for fila in rows:
        try: #Control de registros vacíos en cualquier punto del archivo
            record = dict(zip(encabezados, fila))
            #arbol = {}
            if record['espacio_ve'] == parque:
                arboles.append(record)

        except ValueError:
                print('Cuidado, faltan valores')
                continue
    f.close()
    return arboles

#############################################################
# Ejercicio 3.19: Determinar las especies en un parque
# tome una lista de árboles como la generada en el ejercicio anterior y devuelva 
# el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.
#############################################################
def especies(lista_arboles):
    especie = []
    for k, a in enumerate(lista_arboles):
        especie.append(a['nombre_com'])
        
    return set(especie)

################################################################################    
#Ejercicio 3.20: Contar ejemplares por especie
# Combiná esta función con leer_parque() y con el método most_common() 
# para informar las cinco especies más frecuentes en cada uno de los siguientes parques:
# 'GENERAL PAZ'
# 'ANDES, LOS'
# 'CENTENARIO'
###############################################################################
def contar_ejemplares(lista_arboles): #No esta terminado
# Esta funcion realiza la busqueda de las 5 especies más frecuentes por parque
# Los imprime
    ejemplares = Counter()
    for c in lista_arboles:
        ejemplares[c['nombre_com']] += 1            
        
    return ejemplares
###############################################################################
# Ejercicio 3.21: Alturas de una especie en una lista
###############################################################################

def obtener_alturas(lista_arboles, especie):
    alturas = [] #Vacio lista para usar como estructura del diccionario
    for e in lista_arboles:
        if e['nombre_com'] == especie:
            alturas.append(float(e['altura_tot']))
  
    return alturas
############################################################
# Ejercicio 3.22: Inclinaciones por especie de una lista
############################################################

def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []

    for e in lista_arboles:
        if e['nombre_com'] == especie:
            inclinacion.append(int(e['inclinacio']))
            
    return inclinacion

############################################################
# Ejercicio 3.23: Especie con el ejemplar más inclinado
############################################################
def especimen_mas_inclinado(lista_arboles):
    
    especie = especies(lista_arboles)
    inclinacion = []
    
    for e in especie:
        dato = max(obtener_inclinaciones(lista_arboles, e))
        tupla = (dato, e)
        inclinacion.append(tupla)
    
    masinclinado = max(inclinacion)
    
    return masinclinado[1], masinclinado[0]


############################################################ 
# Ejercicio 3.24: Especie más inclinada en promedio
############################################################

def especie_promedio_mas_inclinada(lista_arboles):
    
    especie = especies(lista_arboles)
    promedio = 0
 
    for e in especie:
        dato = sum(obtener_inclinaciones(lista_arboles, e))/len(obtener_inclinaciones(lista_arboles, e))
        if promedio < dato:
            promedio = dato
            especie = e
   
    return especie, promedio 

'''
#%%
generalpaz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
#%%
print(especies(generalpaz))
#%%
print(contar_ejemplares(generalpaz).most_common(5))
#%%
print(obtener_alturas(generalpaz,"Casuarina"))
#%%
print(obtener_inclinaciones(generalpaz,"Casuarina"))
#%%
print(especimen_mas_inclinado(generalpaz))
#%%
print(especie_promedio_mas_inclinada(generalpaz))
'''
