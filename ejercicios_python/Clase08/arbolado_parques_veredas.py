# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:51:41 2021

@author: User
"""
import pandas as pd
import os
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
archivo1 = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
fname1 = os.path.join(directorio,archivo1)
df_veredas = pd.read_csv(fname)
df_parques = pd.read_csv(fname1)
col = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
col1= ['nombre_cie', 'diametro', 'altura_tot']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][col].copy()
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][col1].copy()

d = {'nombre_cientifico': 'nombre_cie','diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura_tot'}
df_tipas_veredas.rename(columns=d, inplace=True)
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro',by = 'ambiente')

df_tipas.boxplot('altura_tot',by = 'ambiente')


