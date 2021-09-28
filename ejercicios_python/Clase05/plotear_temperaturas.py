
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:16:07 2021

@author: User
"""
import os
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    
    fn = os.path.join('..', 'Data', 'temperaturas.npy')
    temperaturas = np.load(fn)
    plt.hist(temperaturas,bins=25)
    plt.show() 
    
    return
