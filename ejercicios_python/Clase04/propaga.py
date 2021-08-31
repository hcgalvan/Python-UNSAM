# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:46:23 2021

@author: User
"""

###############################################
# Ejercicio 4.6: Propagación
#  en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado)
###############################################
'''
def propagar(lista):
    propagado = []
    conta = 0
    #conta = 
    #v1 = ''
    conta3 = 0
    while conta < len(lista): # Recorro la lista y voy guardando el mayor
        #v1 = lista[conta] #Capturo el primer valor lista
        conta2 = conta + 1
        if conta2 < len(lista): # verifico que estoy dentro de los indices de lista
            if lista[conta3] == 1:
                propagado.append(lista[conta3])
                if lista[conta3] > lista[conta2]: # lo comparo
                    propagado.append(lista[conta3])
                else:
                    propagado.append(lista[conta2])
                    conta3 = conta2
            else:
                propagado.append(lista[conta])
                conta3 = conta
            conta += 1     
        else:
            conta = conta2
            
       
    
    return print(propagado)
'''
def propagar(lista):
   for e in lista:
       if e == 1:
           dat = lista.index(e)
           
       
        

#%%
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
propagar([ 0, 0, 0, 1, 0, 0]) - devuele [ 1, 1, 1, 1, 1, 1]

