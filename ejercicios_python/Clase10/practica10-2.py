# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:31:48 2021

@author: User
"""

class Camion:
    def __init__(self):
        self.lotes = []

    def __iter__(self):
        return self.lotes.__iter__()
    
#%%
camion = Camion()
for c in camion:
    print(c)
#%%
a = [1, 9, 4, 25, 16]
i = a.__iter__()
i.__next__()

#%%
f = open('../Data/camion.csv')
f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
#<_io.TextIOWrapper name='../Data/camion.csv' mode='r' encoding='UTF-8'>
next(f)
'nombre,cajones,precio\n'
next(f)
'Lima,100,32.20\n'
next(f)
'Naranja,50,91.10\n'
#%% Ejerciicio 10.2
