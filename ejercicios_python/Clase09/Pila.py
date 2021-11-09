# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:42:34 2021

@author: User
"""

class Pila:
    def __init__(self):
        '''Crea una cola vacia.'''
        self.pila = []
        
    def esta_vacia(self):
        if len(self.pila) == 0:
            return True
        else:
            return False
        return
    
    def apilar(self, item):
        self.pila.append(item)      
        return
    
    def desapilar(self):
        
        self.pila.pop(-1)
        return

def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")

#%%
pila_de_llamadas = Pila()
#%%
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}

#%%
mostrar_x_del_estado(estado)

#%%
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)

#%%
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#%%
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)
