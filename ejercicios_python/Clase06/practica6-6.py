# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:22:33 2021

@author: User
"""

# búsqueda lineal, es proporcional a len(secuencia)
# búsqueda binaria, proporcional a log2(len(secuencia))
'''
# Un algoritmo cuadrático
for p in lista :
    for q in lista :
        if m == p * q :
            print ( " %d= %d* %d " %(m, p , q ) )

Este algoritmo realiza una comparación ( m == p*q ) 
para cada elemento p y cada elemento q de la lista. 
Es decir, realiza n*n = n^2 comparaciones. 
Es un algoritmo cuadrático. Su complejidad es O(n^2).


'''
# Complejidad en el peor caso
# Al hablar de la complejidad de una algoritmo (salvo que se mencione otra cosa) 
# hablamos del tiempo que tarda ese algoritmo en el peor caso posible.

# Estructuras de datos y Tipos Abstractos de Datos

def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s
#%% Ejercicios:
# Ejercicio 6.15: Insertar un elemento en una lista 
# Ejercicio 6.16: Cálcular la complejidad de dos resoluciones de propagar
#             SECUENCIAS BINARIAS: Para nosotres, una secuencia binaria es una lista que contiene solo 0’s y 1’s. Por ejemplo s = [0, 1, 0, 0, 1] es una secuencia binaria de longitud 5. 
##################
# Ejercicio 6.17: Complejidad de incrementar()
# 
# ¿Te parece que incrementar() es una función lineal, cuadrática, logarítmica o exponencial? ¿Por qué?
##################
# Ejercicio 6.18: Un ejemplo más complejo
incrementar()
