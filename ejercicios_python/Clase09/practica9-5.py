# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:24:11 2021

@author: User
"""
# Objetos, pilas y colas
class Rectangulo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def base(self):
        return
    
    def altura(self):
        return
    
    def area(self):
        return
    
    def desplazar(self, desplazamiento):
        return
    
    def rotar(self, x):
        return
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):   
        return 

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
