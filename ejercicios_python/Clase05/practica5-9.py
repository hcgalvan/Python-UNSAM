# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:32:03 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[0]) 
print(a.ndim) #te dice la cantidad de ejes (o dimensiones) del arreglo
print(a.shape) #Te va a dar una tupla de enteros que indican la cantidad de elementos en cada eje.
print(a.size)
#%%
vec_fila = a[np.newaxis, :]
print(vec_fila.shape, a.shape)
#%%
print(a.sum())
print(a.min())
print(a.max())
#%%
print(a)
print(a.max(axis=1))
print(a.max(axis=0))
#%%
print(np.random.random(3))