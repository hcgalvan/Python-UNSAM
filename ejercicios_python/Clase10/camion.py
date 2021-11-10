# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:55:38 2021

@author: User
"""
import lote
class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()
    
    def __getitem__(self, index):
        return self.lotes.__getitem__(index)
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])
    
    def __len__(self):
        return self.lotes.__len__()
    
    def __repr__(self):
        return f'Camion({self.lotes})'
    
    def __str__(self): 
                
        line = [' Camion con',str(len(self.lotes)),' lotes: \n ']
        for obj in self.lotes:
            t = '   '+ lote.Lote.__str__(obj)
            line.append(t)
        return '\n'.join(line)        
       
    
    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total

    