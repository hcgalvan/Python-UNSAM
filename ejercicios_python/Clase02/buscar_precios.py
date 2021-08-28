# -*- coding: utf-8 -*-
"""
Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author: Hugo César Galván
"""
#buscar precios

#%%
import csv
import re
def buscar_precio(frutas):
    f = open('../Data/precios.csv')
    rows = csv.reader(f)
    for line in rows:
        try:
            #row = line.split(',')
            fruta = line[:1]
            if len(line)>1: # con esta linea busca evitar el error del ultimo registro
                fruta = fruta[0]
                if fruta.lower() == frutas.lower(): #lo dejo todo en minuscula con el fin de comparar correctamente sin importar si mayuscula o minuscula
                    precio = line[1:]
                    precio = precio[0]
                    precio = re.sub(r'(\n)', r'', precio)
                    return print( 'El precio de un cajón de ',frutas,' es: ', precio)
                else:
                    continue
            else:
               return print(frutas,' no figura en el listado de precios.') # continue 
        except ValueError:
            return print(frutas,' no figura en el listado de precios.') # continue
    f.close()
#%%
print(buscar_precio('Frambuesa'))

"""
Salida :
El precio de un cajón de  Frambuesa  es:  34.35
"""