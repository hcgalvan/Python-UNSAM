# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:15:48 2021

@author: Hugo Cesar Galvan
"""
# devuelva una tupla con el valor máximo, el mínimo, el promedio y la mediana (en ese orden) 
import random
import numpy as np
def medir_temp(n):
    a = []
    for i in range(n):
         a.append(random.normalvariate(0,0.2))

    return np.array(a)

def resumen_temp(n):
    for i in range(n):
         temp = medir_temp(n)
         maximo = max(temp)
         minimo = min(temp)
         prome = (sum(temp)/n)
         dat = np.sort(temp)
         dat1 = round(len(dat)/2)
         mediana = dat[dat1]
         tup = (maximo, minimo, prome, mediana)
         print(tup) #imprimo cada tupla
    return #print(tup)

#%%
resumen_temp(10)
