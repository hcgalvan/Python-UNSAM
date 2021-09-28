# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:16:31 2021

@author: User

"""
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.pyplot as plt

def crear_album(figus_total):
    
    
    figuritas = np.zeros(figus_total)
      
    return figuritas

def album_incompleto(A):
    
    if (sum(A)/len(A)) < 1:
        return True
    else:
        return False


def comprar_figu(figus_total):

    figurita = random.randint(1,figus_total)
    
    return figurita

# Cantidad de compras
def cuantas_figus(figus_total):
  #genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo  
    album = crear_album(figus_total)
    compra = 0
    while album_incompleto(album):
        figura = comprar_figu(figus_total)
        compra += 1
        album[figura-1] = 1
    return compra
        
       
def experimento_figus(n_repeticiones, figus_total):
    
    lista =  []
    promedio = 0
    i = 0
    while i < n_repeticiones:
        lista.append(cuantas_figus(figus_total))
        i += 1
    promedio = sum(lista)/n_repeticiones
    
    return promedio

def comprar_paquete(figus_total, figus_paquete):

    #random.seed(figus_total)

    paquete=[]
    for i in range(figus_paquete):
        paquete.append(random.randint(1,figus_total)) 
    
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    
    album = crear_album(figus_total)
    compra = 0
    while album_incompleto(album):
        figura = comprar_paquete(figus_total, figus_paquete)
        for k, i in enumerate(figura):
            album[i-1] = 1
        compra += 1
            
    return compra


def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    
    conta =  Counter()
    promedio = 0
    i = 0
    while i < n_repeticiones:
        lista = cuantos_paquetes(figus_total, figus_paquete)
        conta['paquetes'] += lista
        i += 1
    #print(conta)
    promedio = conta['paquetes']/n_repeticiones
    
    return promedio

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

# Ejercicio 5.21: Plotear el histograma
plt.hist(cuantos_paquetes(100, 20),bins=4)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.



#%%
print( experimento_paquetes(100, 30, 10))
#%%
print(cuantos_paquetes(100, 20))
#%%
print(experimento_figus(100, 20))

#%%
print(comprar_paquete(50, 20))
#%%
print(cuantas_figus(10))

#%%
album = (crear_album(10))

#%%
print(album_incompleto(album))

#%%
print(comprar_figu(10))
#%%
figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#%%
