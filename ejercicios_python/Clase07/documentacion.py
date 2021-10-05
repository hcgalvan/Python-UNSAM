# -*- coding: utf-8 -*-
"""
@author: hcgalvan

Precondiciones sobre las funciones definidas:
------------------------------------
a) def valor_absoluto recibe como parámetro un valor numérico tipo real
b) def suma_pares recibe como parámetro una lista con valores numéricos reales
c) def veces recibe como parámetros 2 valores numéricos a, b:
    donde el valor "a" es un valor tipo real o flotante
    donde el valor "b" es un valor natural incluyendo al cero
d) def collatz recibe como parámetro un solo valor numérico natural que no incluya el cero

Poscondiciones sobre variables de entrada de cada función definida:
------------------------------------
a) def valor_absoluto modifica el valor de entrada y devuelve la variable de entrada modificada
b) def suma_pares evalua la lista de entrada y realiza operaciones matemáticas sin modificar la lista para devolver un valor numérico
c) def veces evalua los valores de entrada sin modificarlas, realiza operaciones y devuelve un valor numérico
d) def collatz modifica el valor de entrada, realiza operaciones matemáticas y devuelve resultado de estas operaciones

"""


def valor_absoluto(n):
    'Devuelve el valor absoluto de un numero'
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    'Devuelve como resultado la suma de valores pares de una lista'
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    'Devuelve como resultado la suma de "b" veces del valor "a" '
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    'Devuelve la sucesión de un n (numero) natural ingresado'
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
