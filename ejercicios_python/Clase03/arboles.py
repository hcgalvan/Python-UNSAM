# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:07:10 2021

@author: User
"""
import csv
from pprint import pprint
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

def leer_parque(nombre_archivo, parques):
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    encabezados = next(rows)
    busca = [parques]
    parque = []
    for k in busca:
        for n_fila, fila in enumerate(rows, start=1):
            try: #Control de registros vacíos en cualquier punto del archivo
                record = dict(zip(encabezados, fila))
                arbol = {}
                if record['espacio_ve'] == k:
                    arbol['espacio_ve'] = record['espacio_ve']
                    arbol['id_especie'] = record['id_especie']
                    arbol['nombre_com'] = record['nombre_com']
                    arbol['nombre_cie'] = record['nombre_cie']
                    arbol['nombre_fam'] = record['nombre_fam']
                    arbol['nombre_gen'] = record['nombre_gen']
                    arbol['origen'] = record['origen']
                    arbol['tipo_folla'] = record['tipo_folla']
                    arbol['altura_tot'] = float(record['altura_tot'])
                    arbol['diametro'] = record['diametro']
                    arbol['inclinacio'] = record['inclinacio']
                    parque.append(arbol)
            except ValueError:
                print('Cuidado, faltan valores')
                continue
    # headers = ('espacio_ve', 'id_especie', 'nombre_com', 'nombre_cie','nombre_fam','nombre_gen','origen','tipo_folla','altura_tot')
    #for lista in parque:
     #   if lista['espacio_ve']==parque:
            #print('%2s %2s %2s %2s %2s %2s %2s %2s %2s' % headers)
            #print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')            
            #print(f'{lista[1]:3d} {lista[2]:3s} {lista[3]:3s} {lista[4]:3s} {lista[5]:3s} {lista[6]:3s} {lista[7]:3s} {lista[8]:3d} {lista[9]:3d} {lista[10]:3d}') 
            #print('{id_especie:3s} {nombre_com:3s}'.format_map(lista))
      #      print(lista) #lista['id_especie'], lista['nombre_com'],  lista['nombre_cie'],  lista['nombre_fam'], lista['nombre_gen'],  lista['origen'])
    return parque

#############################################################
# Ejercicio 3.19: Determinar las especies en un parque
# tome una lista de árboles como la generada en el ejercicio anterior y devuelva 
# el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.
#############################################################
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
    return

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
    from collections import Counter
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    busca = leer_parque(nombre_archivo, 'ANDES, LOS')
    especie = Counter()
    for c in busca:
        especie[c['nombre_com']] += 1            
    print(especie.most_common(5))
    '''
    #### esta seccion era una forma de buscar para 3 parques
    grupo = []
    lugar = ['GENERAL PAZ','ANDES, LOS','CENTENARIO' ]
    for k in lugar:
        for v, lista in enumerate(buscar, start=0):
            parques_esp = {}
            if lista['espacio_ve'] == k:
                parques_esp['parque'] = lista['espacio_ve']
                parques_esp['nombre_com'] = lista['nombre_com']
                grupo.append(parques_esp)
            else:
                continue     
        for c in grupo:
            especie[c['nombre_com']] += 1
        print(k, especie.most_common(5))
    
    return #print(combinados.most_common(5))                
    '''
    return

###############################################################################
# Ejercicio 3.21: Alturas de una especie en una lista
###############################################################################

def obtener_alturas(lista_arboles, especie):
    from collections import Counter
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
    from collections import Counter
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
#%%
imprimir = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
print(imprimir)


#%%
especies(['Ciprés','Casuarina','Cedro del Himalaya'])  

#%%
contar_ejemplares(['Ciprés','Casuarina','Cedro del Himalaya'])  
#%%
obtener_alturas(['Jacarandá','Casuarina','Cedro del Himalaya'], 'Jacarandá')
#%%
obtener_inclinaciones(['Jacarandá','Casuarina','Cedro del Himalaya'], 'Jacarandá')
#%%
especimen_mas_inclinado(['Jacarandá','Casuarina','Cedro del Himalaya'])
#%%
especie_promedio_mas_inclinada(['Jacarandá','Casuarina','Cedro del Himalaya'])