# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:44:55 2021

@author: User
"""
#Ejercicio 6.1: Propagar por vecinos
'''
El siguiente código propaga el fuego de cáda fósforo 
encendido a sus vecinos inmediatos (si son fósforos 
nuevos) a lo largo de toda la lista. Y repite esta 
operación mientras sea necesario. ¿Te animás a estimar..
 cuántas operaciones puede tener que hacer, 
 en el peor caso?
'''
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m
'''
Preguntas: 
    1. ¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no causan un IndexError en los bordes de la lista? 
    2. ¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas perfectamente simétricas, no generan la misma cantidad de repeticiones de llamadas a la función propagar_al_vecino? 
    3. Sobre la complejidad. Si te sale, calculá: 
        * ¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n? 
        * ¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n? 
    * Entonces, 
    ¿cuántas operaciones hace como máximo esta versión de propagar en una lista de largo n? 
    ¿Es un algoritmo de complejidad lineal o cuadrática?
'''
#%%
propagar([0,0,0,0,1])
propagar([0,0,1,0,0])
propagar([1,0,0,0,0])
#%%
# Ejercicio 6.2: Propagar por como el auto fantástico
'''
El siguiente código propaga el fuego inspirado en 
las luces del auto fantástico.
'''
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp
'''
Preguntas: 
    1. ¿Por qué se modificó la lista original? 
    2. ¿Por qué no quedó igual al estado propagado? 
    3. Corregí el código para que no cambie la lista de entrada. 
    4. ¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n? 
    5. Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de operaciones 
    en la longitud de la lista ¿Cuántas operaciones hace como máximo propagar en una lista de largo n?
'''
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#%%
# Ejercicio 6.3: Propagar con cadenas
'''
Esta versión usa métodos de cadenas para resolver 
el problema separando los fósforos en grupos sin fósforos
 quemados y analizando cada grupo. Sin embargo algo falla...
'''
def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

'''
Preguntas: 
    1. ¿Porqué se acorta la lista? 
    2. ¿Podés corregir el error agregando un solo caracter al código? 
    3. ¿Te parece que este algoritmo es cuadrático como el Ejercicio 6.1 o lineal como el Ejercicio 6.2?
'''
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)
#%% EJERCICIOS REALIZADOS
# Ejercicio 6.1: Propagar por vecinos
# Ejercicio 6.2: Propagar por como el auto fantástico
# Ejercicio 6.3: Propagar con cadenas