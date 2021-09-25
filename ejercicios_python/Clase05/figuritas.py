# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:16:31 2021

@author: User

"""
import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    
    
    return

def album_incompleto(A):
    
    return

def comprar_figu(figus_total):
   
    return

def cuantas_figus(figus_total):
    return

def experimento_figus(n_repeticiones, figus_total):
    return

def comprar_paquete(figus_total, figus_paquete):
    return

def cuantos_paquetes(figus_total, figus_paquete):
    return

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
#%%
figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

#%%
plt.hist(temperaturas,bins=25)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.