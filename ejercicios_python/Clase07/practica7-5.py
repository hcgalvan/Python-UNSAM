# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:48:29 2021

@author: User
"""

# 7.5 Contratos: Especificación y Documentación
def elegir_codigo():
    '''Devuelve un codigo de 4 digitos elegido al azar'''
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ""
    for i in range(4):
        candidato = random.choice(digitos)
        # Debemos asegurarnos de no repetir digitos
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo
#%% Código autodocumentado
# existe una técnica de programación llamada código autodocumentado,
a = 9.81
b = 5
c = 0.5 * a * b**2

# Otra tecnica de código autodocumentado
aceleracion_gravitacional = 9.81
tiempo_segundos = 5
desplazamiento_metros = 0.5 * aceleracion_gravitacional * tiempo_segundos ** 2

#%% Un error común: la sobredocumentación
def buscar_elemento(lista_de_numeros, numero):
    '''Esta función devuelve el índice (contando desde 0) en el que se
       encuentra el número `numero` en la lista `lista_de_numeros`.
       Si el elemento no está en la lista devuelve -1.
    '''
    # Recorremos todos los índices de la lista, desde 0 (inclusive) hasta N
    # (no inclusive)
    for indice in range(len(lista_de_numeros)):
        # Si el elemento en la posicion `indice` es el buscado
        if lista_de_numeros[indice] == numero:
            # Devolvemos el índice en el que está el elemento
            return indice
    # No lo encontramos, devolvemos -1
    return -1
# Algunas cosas que podemos mejorar, y resultará lo siguiente
def indice(lista, elemento):
    '''Devuelve el índice en el que se encuentra el `elemento` en la `lista`,
       o -1 si no está.
    '''
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1
#%% CONTRATOS
'''
Cuando hablamos de contratos o programación por contratos, 
nos referimos a una forma de estipular tanto lo que nuestro código
 asume sobre los parámetros, como lo que devuelve.
'''
# Precondiciones: debe cumplirse antes de ejecutarla para que se comporte correctamente
# Poscondiciones: caracterizará cómo será el valor de retorno y cómo se modificarán las variables de entrada (en caso de que corresponda) al finalizar la ejecución siempre asumiendo que se cumplió la precondición al inicio.
#%% El qué, no el cómo
# un problema con pre y poscondición estamos definiendo qué es lo que debe suceder. En ningún momento decimos cómo es que esto sucede. 
#%% ASEVERACIONES  (en inglés assertions)
# En algunos casos puede ser útil incorporar estas afirmaciones desde el código, y para eso podemos utilizar la instrucción assert
>>> assert True
>>> assert False
(Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
AssertionError^)
# assert puede recibir un mensaje de error 
# Atención: Es importante tener en cuenta que assert está pensado para ser usado en la etapa de desarrollo. 
#%% EJEMPLOS
# EJEMPLO 1
def division(dividendo, divisor):
    '''Cálculo de la división

    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    assert divisor != 0, 'El divisor no puede ser 0'
    return dividendo / divisor

# o directamente

def division(dividendo, divisor):
    '''Cálculo de la división

    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    return dividendo / divisor 
# EJEMPLO 2 - Precondicion: enteros 
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
#%%    
# EJERCICIOS
# Ejer cicio 7.8: Sumas : Ayuda: Estas sumas se pueden escribir como diferencia de dos números triangulares.
#     Invariantes de ciclo: es una aseveración que debe ser verdadera al comienzo de cada iteración del ciclo y al salir del mismo.
def maximo(lista):
    'Devuelve el elemento máximo de la lista o None si está vacía.'
    if not lista:
        return None
    max_elem = lista[0]
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem

def potencia(base, exp):
    'Calcula la potencia exp del número base, con exp entero mayor que 0.'
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado
#--------
def suma(lista):
    'Devuelve la suma de todos los elementos de la lista.'
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

# Ejercicio 7.9: Invariante en sumas
# Parámetros mutables e inmutables
>>> def no_cambia_lista(lista):
...     lista = [0, 1, 2, 3]
...     print('Dentro de la funcion lista =', lista)
...
>>> lista = [10, 20, 30, 40]
>>> no_cambia_lista(lista)
Dentro de la funcion lista = [0, 1, 2, 3]
>>> lista
[10, 20, 30, 40]

#A continuación un ejemplo en el cual se modifica la variable recibida.
>>> def cambia_lista(lista):
...     for i in range(len(lista)):
...         lista[i] = lista[i] ** 3
...
>>> lista = [1, 2, 3, 4]
>>> cambia_lista(lista)
>>> lista
[1, 8, 27, 64]
#%% Repaso
# Resumen
#  Contrato (precondicion y poscondicion)
#  Documentacion
#  incluir contrato en documentacion
#  debe ser explicitado en la documentacion si una funcion modifica
#  un valor mutable que recibe por parametro
#  Los comentarios tiene como objetivo explicar como funciona el codigo
#  y por que se deció implementarlo de esa manera
#  Los invariantes de ciclo son condiciones que deben cumplirse al 
#  comienzo de cada iteracion
#%% EJERCICIOS
# Ejercicio 7.10: Funciones y documentación. Guardá estos códigos con tus modificaciones en el archivo documentacion.py
def valor_absoluto(n):
    if n >= 0:
        return n
    else:
        return -n
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res




