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
## La dificultad es cuando hace la lista inversa solo llega hasta el valor anterior al primero
# entonces falla en ese punto, el otro recorre bien
'''
def propagar(lista):
    r = len(lista)
    for n, e in enumerate(lista):
       if (r) > (n+1):
            if e == 1 and lista[n+1]== 0:
               lista[n+1] = 1
            else:
               continue
       else:
           continue
    for n, e in enumerate(lista): # Recorro la lista
        i = n # tomo el valor del indice
        i = len(lista)-i # acumulo el valor
        
        if (r) > (n+1) > 1:
    
            if lista[i]==1 and lista[i-1]==0:
               lista[i-1] = 1 
    
            else:
                continue
        else:
            continue
    return    print(lista)
       
           
       
        

#%%
propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])

#%%
propagar([ 0, 0, 0, 1, 0, 0]) #- devuele [ 1, 1, 1, 1, 1, 1]

