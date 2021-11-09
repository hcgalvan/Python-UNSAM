# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:53:45 2021

@author: User
"""
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __iter__(self):
        yield self.nombre
        yield self.cajones
        yield self.precio
    
    def __getitem__(self, index):
        return self.__getitem__(index)
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

    def __str__(self):
        return f'Lote de {self.cajones} cajones, de {self.nombre}, pagados a {self.precio} cada uno.'
    
    def costo(self):
        valor = self.cajones * self.precio
        return valor

    def vender(self, venta):
        self.cajones -= venta
        
