
"""
@author: hcgalvan
"""
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a() Semántica
#Comentario: El error era el uso de RETURN dentro de la sentencia if, lo que al entrar en el primer
# ciclo del While ya salia. Por otro lado no controlaba las letras mayusculas
#    Lo corregí cambiando por un contador de las veces que aparece e imprimiendo al final.
#    Corregi el control de mayusculas utilizando la función lower para dejar la expresion en minusculas
def tiene_a(expresion):
    n = len(expresion)
    valor = expresion.lower()
    i = 0
    cuenta = 0
    while i<n:
        if valor[i] == 'a':
            cuenta += 1
        i = i + 1
    print(f'tiene a la letra "a": {cuenta} veces')

#%% 
tiene_a('UNAM 2020')
#%%
tiene_a('abracadabra')
#%%
tiene_a('La novela 1984 de George Orwell')

#%%
'''
Ejercicio 3.2: Sintaxis
¿Anda bien en todos los casos de prueba?
'''
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de falta cerrar la definicion de funcion y estaba ubicado  en:
# Falta cerrar el def ->   "def tiene_a(expresion)"
# Falta cerrar del ciclo -> while i<n
# Falta cerrar la condición ademas no es correcto la expresion de igualdad -> if expresion[i] = 'a'
# No controla las mayusculas de la expresion
# Error en el return con mal escrita la palabra reservada False como "Falso"
#%%

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    valor = expresion.lower()
    while i<n:
        if valor[i] == 'a':
            return True
        i += 1
    return False

#%%
print(tiene_a('UNSAM 2020'))
#%%
print(tiene_a('La novela 1984 de George Orwell'))
#%%
'''
Ejercicio 3.3: Tipos
¿Anda bien en todos los casos de prueba?
'''
#Ejercicio 3.3. Función tiene_uno
#Comentario: El error sucede cuando la expresion es una cadena:
#La solucion es convertir a cadena cualquier expresion enviada a la funcion

def tiene_uno(expresion):
    n = len(str(expresion))
    cadena = str(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if cadena[i] == '1':
            tiene = True
        i += 1
    return tiene
#%%
print(tiene_uno('UNSAM 2020'))
#%%
print(tiene_uno('La novela 1984 de George Orwell'))
#%%
print(tiene_uno(1984))
#%%
'''
Ejercicio 3.4: Alcances
La siguiente suma no devuelve el resultado:
    El error se encuentra en colocar la variable c sin retornar el resultado
    El cambio fue hacer return de la operacion
'''
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
#%%
print(f"La suma da {a} + {b} = {c}")
#%%
'''
Ejercicio 3.5: Pisando memoria
El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
El error viene determinado por lo siguiente:
Sucede que el diccionario es un tipo compuesto que se pasa por referencia con valores inmutables.
Con el método copy() del diccionario, nos permite copiar los valores sin referencias del diccionario a una variable de "tipo simple" que es posible pasar por valor
Luego, agregamos este tipo simple por valor a la lista

'''
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            regis = registro.copy()
            camion.append(regis)
    return camion

#%%
camion = leer_camion('../Data/camion.csv')

pprint(camion)