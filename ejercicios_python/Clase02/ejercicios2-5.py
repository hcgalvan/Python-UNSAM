# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:44:59 2021

@author: User
"""
#%% Contenedores
# usamos lista cuando el orden de los datos es importante.
# una lista puede contener cualquier objeto, ej: tuplas
camion = [
    ('pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.4)
    ]
print(camion[0])
#%%
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]
#%%
precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
#%% Podés verificar si una clave existe
if key in d:
    print('YES')
else:
    print('NO')
    
#%%
feriados = {
  (1, 1) : 'Año nuevo',
  (1, 5) : 'Día del trabajador',
  (13, 9) : "Día del programador",
}
#%%
print(feriados[(1,5)])
#%% CONJUNTOS
citricos = {'Naranja','Limon','Mandarina'}
print(citricos)
#%% CONJUNTOS UTILES PARA EVALUAR PERTENENCIA
#otra forma de escribir
citricos1 = set(['Naranja', 'Limon', 'Mandarina'])
print(citricos1)
print('Naranja' in citricos)
#%% CONJUNTO TAMBIEN SON UTILES PARA ELIMINAR DUPLICADOS
nombres = ['Naranja','Manzana','Pera','Naranja','Pera','Banana']
unicos = set(nombres)
print(unicos)
citricos.add('Banana')
citricos.remove('Limon')
#%%
print(citricos)
#%%
precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
