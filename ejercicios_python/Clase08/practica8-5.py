# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:12:39 2021

@author: User
"""

import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

#%%
df.columns
df.head() 
df[['altura_tot', 'diametro', 'inclinacio']].describe() # Categorizar las variables indicadas
df['nombre_com'].unique() # Valores unicos
df['nombre_com'] == 'Ombú' # busqueda solo del nombre elegido
(df['nombre_com'] == 'Ombú').sum() #sumar true, cuenta solo los nombres elegidos
cant_ejemplares = df['nombre_com'].value_counts() # cuenta los valores
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'] # Seleccionar todos los samples jacaranda

cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.describe()
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy() # crear una copia de los datos

df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot') #plotea los puntos

import seaborn as sns
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot') # lo entiende correctamente

# Filtros por índice y por posición
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.index  # es una serie (es como un DataFrame de una sola columna).
df.loc[165] #Para acceder con el índice usá loc[]
cant_ejemplares.loc['Eucalipto'] # Para acceder por número de posición usá iloc
cant_ejemplares.iloc[0:3] # acceder por rebanadas
df_jacarandas.iloc[-5:,2] # Esto nos devuelve los datos correspondientes a las últimas 5 filas y a la tercera columna ('inclinacio'). Fijate que siempre vienen acompañados del índice.

# Selección de una columna
df_jacarandas_diam = df_jacarandas['diametro']
type(df_jacarandas) # pandas.core.frame.DataFrame
type(df_jacarandas_diam) # pandas.core.series.Series

# Series temporales en Pandas
pd.date_range('20200923', periods = 7)
pd.date_range('20200923 14:00', periods = 7)
pd.date_range('20200923 14:00', periods = 6, freq = 'H')

#Luego, podés usar esos índices junto con datos para armar series temporales o DataFrames:
pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))

# Caminatas al azar
# Observá que estamos usando random del módulo numpy, no de random. 
# La función np.random.randint(-1,2,120) genera un array 
# de longitud 120 con valores -1, 0, 1 (no incluye extremo derecho del rango de valores).
import numpy as np
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

# O usar una media móvil (rolling mean) para suavizar los datos:
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

# Podés ver ambas curvas en un mismo gráfico para ver más claramente el efecto del suavizado:
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

# Ejemplo: 12 personas caminando 8 horas
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

# Los acumulamos con cumsum y los acomodamos en un DataFrame, 
# usando el índice generado antes y poniéndoles nombres adecuados a cada columna:
    
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

# Ahora suavizamos los datos, usando min_periods para no perder los datos
# de los extremos.
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()

# Guardando datos
df_walk_suav.to_csv('caminata_apostolica.csv')
#%%
# Incorporando el Arbolado lineal
# Ejercicio 8.7: Lectura y selección
import pandas as pd
import os
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_lineal  = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df_lineal[cols_sel]

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
print(df_lineal_seleccion)
# Grafica un bloxplot
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
#%%
import seaborn as sns
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
