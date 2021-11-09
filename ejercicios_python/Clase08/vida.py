# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:51:12 2021

@author: User
"""
from datetime import datetime

def vida_en_segundos(fecha_nac):
    t1 = datetime.strptime(fecha_nac, '%d/%m/%Y')
    t2 = datetime.now()
    
    t3 = t2 - t1
    t4 = t3.total_seconds()
          
    return t4

