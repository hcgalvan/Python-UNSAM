# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:32:35 2021

@author: User
"""
import random
def generar_punto():
    
    x = random.random()
    y = random.random()
    return x,y

def medir_temp(n):

    for i in range(n):
        print(f'{random.normalvariate(0,0.2):.2f}', end=', ')
        
    return
        

#%%
for i in range(6):
        print(f'{random.normalvariate(0,1):.2f}', end=', ')
#%%
medir_temp(10)
        