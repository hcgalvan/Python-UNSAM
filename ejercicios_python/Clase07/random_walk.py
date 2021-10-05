# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:36:04 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)
    return pasos.cumsum()

def graficas():
    N = 100000
    trayectoria = 11
    lis =[]
    mayor = 0
    dato2 = randomwalk(N)
    menor = sum(dato2)
    dato = []
    for i in range(trayectoria):
        v = randomwalk(N)
        valor1 = sum(v)
        if mayor > valor1:
            dato = v
            mayor = valor1
        else:
            if valor1 < menor:
                menor = valor1
                dato2 = v
                
        lis.append(dato)
        plt.subplot(2, 1, 1)
        plt.plot(v)
        
    plt.xticks([]), plt.yticks([]) # saca las marcas
    plt.xlabel('tiempo')
    plt.ylabel('distancia al origen')
    plt.title('12 Caminatas al azar', fontsize = 10)
    
    plt.subplot(2, 2, 3)
    plt.plot(dato)
    plt.title('La Caminata que mas se aleja', fontsize = 8)
    plt.xticks([])
    
    plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot(dato2)
    plt.xticks([])
    plt.title('La Caminata que menos se aleja', fontsize = 8)
    
        
    
    plt.show()

    return

def f_principal(parametros):
    if len(parametros) != 1:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ')
        graficas()
    return

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

