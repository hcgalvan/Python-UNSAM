# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:36:18 2021

@author: User
"""

#%% FUNCIONES
# Si un argumento es opcional, dale un nombre.
'''
Llamando a una función
Imaginá la siguiente función:

def leer_precios(nombre_archivo, debug):
    ...
Podés llamar a la función pasando los argumentos por orden:

precios = leer_precios('precios.csv', True)
O podés llamarla usando palabras clave (keywords):

precios = leer_precios(nombre_archivo = 'precios.csv', debug = True)
'''
# Argumentos por omisión
# Si preferís que un argumento sea opcional (que tenga un valor por omisión o by default), en ese caso asignale un valor en la definición de la función.
def leer_precios(nombre_archivo, debug = False):

# 2 formas de invocar la función, la 1era tomará el valor por defecto, la 2da define el valor    
d = leer_precios('precios.csv')
e = leer_precios('precios.dat', True)

#%% Si un argumento es opcional, dale un nombre
#Comparemos estos dos estilos de invocar funciones:
cortar_datos(data, False, True) # ?????

cortar_datos(data, ignore_errores = True)
cortar_datos(data, debug = True)
cortar_datos(data, debug = True, ignore_errores = True)
#%% Buenas prácticas de diseño
# Quien use la función podría elegir llamarla con argumentos nombrados.

def leer_precios(f, d = False):
    return valor

def leer_precios(nombre_archivo, debug = False):
    return valor

# Quien use la función podría elegir llamarla con argumentos nombrados.
d = leer_precios('precios.csv', debug = True)
#%% Devolver un resultado
# 
# return termina la función y devuelve un valor

def cuadrado(x):
    return x * x

# si no se define el comando return devuelve None
def bar(x):
    instrucciones
    return

a = bar(4)          # a = None

# O TAMBIEN...
def foo(x):
    instrucciones   # No hay `return`

b = foo(4)          # b = None

#%% Devolver múltiples resultados
# 
def dividir(a,b):
    c = a // b      # Cociente
    r = a % b       # Resto
    return c, r     # Devolver una tupla con c y r

#%% Alcance de variables
# En un programa se declaran variables y se les asignan valores. Esto ocurre dentro y fuera de funciones.

x = valor # Variable Global

def foo():
    y = valor # Variable Local
#%% Las variables locales
# declaradas dentro de funciones, son privadas.
def leer_camion(nombre_archivo):
    camion = []
    for linea in open(nombre_archivo):
        campos = line.split(',')
        s = (campos[0], int(campos[1]), float(campos[2]))
        camion.append(s)
    return camion

#%% Variables globales
# Desde cualquier función se puede acceder a las variables globales declaradas en ese mismo archivo.

nombre = 'Dave'

def saludo():
    print('Hola', nombre)  # Usa la variable global `nombre`
    
#%%
# acordate: Las asignaciones de valores a variables y las declaraciones de variables dentro de funciones son locales.
# En este caso no modifica la variable global
nombre = 'Dave'

def spam():
  nombre = 'Guido'

spam()
print(nombre) # imprime 'Dave'
# usar variables globales se considera una mala práctica. 
#%%
# Modificar el valor de una variable global
nombre = 'Dave'

def spam():
    global nombre
    nombre = 'Guido' # Cambia el valor de la variable global

#%% Pasaje de argumentos
# Fundamental: Las funciones no reciben una copia de los argumentos, sino los argumentos mismos.
def foo(items):
    items.append(42)    # Cambia el valor de items

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
#%% Reasignar versus modificar
# Recordá: reasignar una variable nunca sobreescribe la memoria que ocupaba. Sólo se asocia el nombre de la variable a un nuevo valor.
def foo(items):
    items.append(42)    # Modifica el valor de 'items'

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# Versus
def bar(items):
    items = [4,5,6]    # Cambia la variable local 'items' y
    # hace que apunte a otro objeto completamente diferente.

b = [1, 2, 3]
bar(b)
print(b)               # imprime [1, 2, 3]
#%%
# Ejercicios
# Ejercicio 6.6: Parsear un archivo CSV
# Ejercicio 6.7: Selector de Columnas
# Ejercicio 6.8: Conversión de tipo
# Ejercicio 6.9: Trabajando sin encabezados
# Comentario
