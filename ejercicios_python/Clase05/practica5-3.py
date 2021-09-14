# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:44:14 2021

@author: User
"""
# Arreglos n-dimensionales
import numpy as np

#%%
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
#%%
print(a[0])
print(a[2])
print(a[2][3])
#%%
print(np.zeros(2)) # Crea un arreglo con dos elementos tipo cero
print(np.ones(2)) # Crea un arreglo con dos elementos tipo 1
print(np.empty(2)) # Crea un arreglo con dos elementos vacio
#%% También podés crear vectores a partir de un rango de valores:
print(np.arange(4))
#%% Vector que contiene elementos equiespaciados, especificando 
# el primer número, el límite, y el paso.
print(np.arange(2, 9, 2)) # o np.arange(2, 10, 2)
#%% crear un vector de valores equiespaciados especificando 
# el primer número, el último número, y la cantidad de elementos
print(np.linspace(0, 10, num=5))

#%%

#Ejercicio 5.7: arange() y linspace()
''' Generá un vector que tenga los números impares entre el 1 y el 19 inclusive 
 usando arange(). Repetí el ejercicio usando linspace(). 
  ¿Qué diferencia hay en el resultado? '''



#%%
# podés explicitar otro tipo de datos usando la palabra clave dtype.
x = np.ones(2, dtype=np.int64)
print(x)

#%%
# Agregar, borrar y ordenar elementos
#Ordenar un vector es sencillo usando np.sort()

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print( arr )
print(np.sort(arr))

#%%
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# los podés concatenar usado np.concatenate()
print(np.concatenate((a, b)))
#%% mas complejo
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))
#%% Conocer el tamaño, dimensiones y forma de un arreglo
array_ejemplo = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0 ,1 ,2, 3], [4, 5, 6, 7]]])
#
print(array_ejemplo.ndim) # cantidad de dimensiones
#%%
print(array_ejemplo.shape ) # cantidad de elementos en cada eje 
#%%
print(array_ejemplo.size ) # total de elementos 3*2*4
#%% Cambiar la forma de un arreglo
a = np.arange(6)
print(a)
#%%
b = a.reshape(3, 2)
print(b)
#%%
# Agregar un nuevo eje a un arreglo
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)
#%%
vec_fila = a[np.newaxis, :]
print(vec_fila.shape)
#%%
vec_col = a[:, np.newaxis]
#%% Índices y rebanadas
data = np.array([1, 2, 3])
print(data)
print(data[1])
#%% Podés imprimir todos los valores menores que cinco.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 8])

#%%
five_up = (a >= 5)
print(five_up)
#%% Podés seleccionar los elementos pares:
pares = a[a%2==0]
print(pares)
#%%
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
print(arr1)
#%%
arr1[0] = 44
print(arr1)

#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Ahora creamos b1 a partir de una rebanada de a y modificamos su primer elemento. ¡Esto va a modificar el elemento correspondiente de a también!
b1 = a[0, :]
print(b1)
#%%

b1[0] = 99
print(b1)
print(a)
#%%
b2 = a[1, :].copy()
print(b2) 
