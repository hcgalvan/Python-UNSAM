# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:23:56 2021

@author: User
"""

# Metodos especiales
class Lote(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
#%% 
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Con `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Con `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
#%% Métodos matemáticos especiales
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    def __add__(self, b):
        return Punto(self.x + b.x, self.y + b.y)

#%% Métodos especiales para acceder a elementos
class Secuencia:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...


  