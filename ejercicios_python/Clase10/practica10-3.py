# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:32:08 2021

@author: User
"""

# 10.3 Iteración a medida
def regresiva(n):
    # Agreguemos este print para ver qué pasa...
    print('Cuenta regresiva desde', n)
    while n > 0:
        yield n
        n -= 1


# Ejercicio 10.4: Un generador simple
def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

