# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:52:19 2021

@author: User
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')
# dos cosas: 
# * por un lado que use la columna 'Time' como índice (index_col = ['Time']) y 
# * por el otro que la interprete como un timestamp (parse_dates = True).
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

df.index
df['1-18-2014 9:00':'1-18-2014 18:00']
df['2-19-2014']
df['12-25-2014':]
df['12-25-2014':].plot()

df['10-15-2014':'12-15-2014'].plot()

dh = df['12-25-2014':].copy()

delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 0 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
# encontrar los valores delta
# valores_delta_t


# Levanto las dos series
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
# Me quedo con un fregmento
dh=df['10-01-2014':].copy()
# Selecciono los intervalos que voy a usar para desplazar SF
shifts = np.arange(-12,13)
# Genero un vector donde guardar los coeficientes de correlacion para cada deslpazamiento
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(shifts):
    #guardo el coeficiente de correlación r entre de SF desplazada con BA original.
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[12:-12],dh['H_BA'][12:-12])[0]
# ploteo los resultados   
plt.plot(shifts, corrs)

#Ejercicio 8.11: Interpolación
# Cada cuarto de hora
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
dh =df['10-01-2014':].copy() #ultimo trimestre
freq_horaria = 4 # 4 para 15min, 60 para 1min
cant_horas = 24
N = cant_horas * freq_horaria
#resampleo cada tantos minutos
dh = dh.resample(f'{int(60/freq_horaria)}T').mean()
#rellenos los NaNs suavemente
dh =dh.interpolate(method='quadratic')
# genero vector de desplazamientos (enteros)
ishifts = np.arange(-N,N+1)
# y su desplamiento horario asociado
shifts=ishifts/freq_horaria
# finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N:-N],dh['H_BA'][N:-N])[0]
# y grafico
plt.plot(shifts, corrs)