# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:06:02 2021

@author: User
"""

#%% Módulos y la instrucción import
# Todos los archivos con código Python son módulos.
# Nombre del archivo: foo.py
def grok(a):
    ...
def spam(b):
    ...
#%%
# Namespaces
# Se puede decir que un módulo es una colección de valores 
# asignados a nombres. A ésto se lo llama un namespace (espacio de nombres).
# El comando import carga un módulo y lo ejecuta.    
# programa.py
# El nombre del módulo es el nombre del archivo que lo contiene.
import foo

a = foo.grok(2)
b = foo.spam('Hola')
...
#%%
# Los módulos están aislados uno de otro.
#  Cada módulo es un pequeño universo.

#%% Ejecución de módulos    
# El comando import as
# En el momento de importar un módulo, podés cambiar el nombre que le asignás dentro del contexto en que lo importás.
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
#%% from módulo import nombre
# Este comando toma ciertos nombres selectos de un módulo, y los hace accesibles localmente.
# Es útil para nombres (funciones o variables) que se usan mucho.
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
#%%
# no modifican el funcionamiento de un módulo.
import math
# vs
import math as m
# vs
from math import cos, sin
...

#%% Carga de módulos
# Repetir la instrucción import sólo devuelve una referencia al módulo ya cargado.
# La variable sys.modules es un diccionario de los módulos cargados.
import sys
sys.modules.keys()

#%% Ejercicio 6.10: Importar módulos
# Importá sólo la función para evitar escribir el nombre del módulo:
# Ejercicio 6.11: Usemos tu módulo
# Ejercicio 6.12: Un poco más allá
