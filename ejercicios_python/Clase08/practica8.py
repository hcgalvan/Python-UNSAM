# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:45:48 2021

@author: User
"""

import zipfile.Zipfile('../Data/ordenar.zip','r') as zip_ref:
    zip_ref.extractall('../Data/ordenar')
