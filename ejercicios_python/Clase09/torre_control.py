# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:54:13 2021

@author: User
"""

class  TorreDeControl:
    
    def __init__(self ):
        '''Crea una cola vacia.'''
        self.arribos = []    
        self.partida = []    
    
    def nuevo_arribo(self, arribo):
        ''' Agrega un nuevo arribo '''
        self.arribos.append(arribo)
        
    def nueva_partida(self, partida):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        self.partida.append(partida)
    
    def en_espera(self, valor):
        '''Devuelve el largo de la cola.'''
        return len(valor)
    
    
    def esta_vacia(self, valor):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.en_espera(valor) == 0 
    
    def asignar_pista(self):
        if self.esta_vacia(self.arribos):
            if self.esta_vacia(self.partida):
                return print('No hay vuelos en espera')
            return print(f'el vuelo {self.partida.pop(0)} despegó con éxito.')
        return print(f'el vuelo {self.arribos.pop(0)} aterrizó con éxito.')
         
    
    def proximo(self, valor):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        
        return valor[:]
    
    def ver_estado(self):
        arr = "<"
        arr += ", ".join(self.arribos)
        arr += ">"
        des = "<"
        des += ", ".join(self.partida)
        des += ">"
        
        if not self.esta_vacia(self.arribos):
            arr += "\n"
            arr += f"Vuelos esperando para aterrizar: {self.proximo(self.arribos)}"
        arr += "\n"

        if not self.esta_vacia(self.partida):
            des += "\n"
            des += f"Vuelos esperando para despegar: {self.proximo(self.partida)}"
        des += "\n"
        
        print(arr)
        print(des)
        
    