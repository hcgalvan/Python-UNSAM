# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 16:43:53 2021

@author: Hugo César Galván
"""
#%%
import gzip
with gzip.open('../Data/camion.csv.gz','rt') as f:
    for line in f:
        print(line, end ='')
