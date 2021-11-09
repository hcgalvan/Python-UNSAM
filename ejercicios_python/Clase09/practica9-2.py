# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:22:49 2021

@author: User
"""

# Un objeto de tipo Jugador tiene como atributos x, y y salud. Sus métodos son mover() y lastimar().

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts

        