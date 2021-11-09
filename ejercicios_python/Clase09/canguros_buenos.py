# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:40:50 2021

@author: User
"""

# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        elems = []
        self.nombre = nombre
        # El bug es que reutilizaba sin importar las llamadas posteriores.
        # Esto sucede porque ya asignamos al principio el vector
        # Para evitar reutilización debemos asegurarnos de inicializarlas dentro del código.
        for c in contenido: 
            elems.append(c)
        self.contenido_marsupio = elems
               

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def  meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
#%%
print(cangurito)

