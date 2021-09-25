# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:07:10 2021

@author: User
"""
import csv
from collections import Counter

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
    parque = []
    # for k in busca:
    for fila in rows:
        try: #Control de registros vacíos en cualquier punto del archivo
            record = dict(zip(encabezados, fila))
            print(record)
            #arbol = {}
            if record['espacio_ve'] == parque:
                parque.append(record)
        except ValueError:
                print('Cuidado, faltan valores')
                continue
    f.close()
    return print(parque)

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
        
    #return especie.most_common(5)
    return ejemplares
###############################################################################
# Ejercicio 3.21: Alturas de una especie en una lista
###############################################################################

def obtener_alturas(lista_arboles, especie):

    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    buscar = parques(nombre_archivo)
    parque_nom = 'ANDES, LOS'
    parque_eleg = leer_parque(nombre_archivo, parque_nom)
    clave =[]
    for e in lista_arboles:
         for v in buscar:
            alturas = [] #Vacio lista para usar como estructura del diccionario
            if v['nombre_com'] == e:
                 l = (v['nombre_com'], v['altura_tot'] ) # Armo una tupla
                 alturas.append(l) # Agrego a una lista la tupla
                 especies = dict(alturas) # Convierto en diccionario la lista
                 clave.append(especies) # Lo agrego a lista el diccionario
                
            else:
                continue
    # El siguiente for, busca en lista de arboles la especie
    for v in clave:
        valor = list(v.keys()) #Convierto la clave en lista para poder comparar
        if valor == [especie]: #comparo lista obtenida con especie transformada en lista
            v  # por una cuestion de estructura solo coloco el valor sin imprimir, ya que será devuelto cuando obtenga el parque
        else:
            continue
    nueva_lista = []
    altura = 0
    contador = 0
    for p in parque_eleg:
        for e in clave:
            valor = list(e.keys())
            if p['nombre_com'] == valor[0]:
                if p['nombre_com'] == especie:
                    altura = p['altura_tot']
                    contador += 1
                    nueva_lista.append(altura)
                else:
                    continue
            else:
                continue
    print( 'Parque:', parque_nom, 'especie:',especie, 'Max:', max(nueva_lista), 'Prom: ', sum(nueva_lista)/contador  )       
            
    return
############################################################
# Ejercicio 3.22: Inclinaciones por especie de una lista
############################################################

def obtener_inclinaciones(lista_arboles, especie):
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    buscar = parques(nombre_archivo)
    parque_nom = 'ANDES, LOS'
    parque_eleg = leer_parque(nombre_archivo, parque_nom)
    clave =[]
    for e in lista_arboles:
         for v in buscar:
            inclinacion = [] #Vacio lista para usar como estructura del diccionario
            if v['nombre_com'] == e:
                 l = (v['nombre_com'], v['inclinacio'] ) # Armo una tupla
                 inclinacion.append(l) # Agrego a una lista la tupla
                 especies = dict(inclinacion) # Convierto en diccionario la lista
                 clave.append(especies) # Lo agrego a lista el diccionario
                
            else:
                continue
    # El siguiente for, busca en lista de arboles la especie
    for v in clave:
        valor = list(v.keys()) #Convierto la clave en lista para poder comparar
        if valor == [especie]: #comparo lista obtenida con especie transformada en lista
            print(v)
        else:
            continue
            
    return

############################################################
# Ejercicio 3.23: Especie con el ejemplar más inclinado
############################################################
# FALTA TERMINAR
def especimen_mas_inclinado(lista_arboles):

    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    buscar = parques(nombre_archivo)
    parque_nom = 'ANDES, LOS'
    parque_eleg = leer_parque(nombre_archivo, parque_nom)
    clave =[]
    for e in lista_arboles:
         for v in buscar:
            inclinacion = [] #Vacio lista para usar como estructura del diccionario
            if v['nombre_com'] == e:
                 l = (v['nombre_com'], v['inclinacio'] ) # Armo una tupla
                 inclinacion.append(l) # Agrego a una lista la tupla
                 especies = dict(inclinacion) # Convierto en diccionario la lista
                 clave.append(especies) # Lo agrego a lista el diccionario
                
            else:
                continue
    #Aqui busco el especimen mas inclinado
    nueva_lista = []
    inclina = 0
    for p in parque_eleg:
        for f in clave:
            valor = list(f.keys())
            if p['nombre_com'] == valor[0]:
                l2 = (p['nombre_com'], p['inclinacio'] )
                #print(l2)
                nueva_lista.append(l2)
            else:
                continue

    print( max(nueva_lista) )       
            
    return
############################################################ 
# Ejercicio 3.24: Especie más inclinada en promedio
############################################################
# FALTA TERMINAR

def especie_promedio_mas_inclinada(lista_arboles):
        
    return
