# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:23:40 2021

@author: User
"""
#herencia


#  Clase base, o superclase (tambien llamada Padre)
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
#%% Esta clase redefine el orginal        
class MiLote(Lote):
    def costo(self):
        return 1.25 * self.cajones * self.precio
#%% Redefinicion 
class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor

    def costo(self):
        return self.factor * super().costo()    