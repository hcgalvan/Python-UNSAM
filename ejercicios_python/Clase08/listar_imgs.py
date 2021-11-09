# -*- coding: utf-8 -*-
"""
A partir de una entrada de carpeta, recorre archivos en subcarpetas,
y busca aquellos con extension png y los agrega a una lista

@author: hcgalvan
"""
import os

def archivos_png(directorio):

    lista = []
    actual = os.getcwd()
    os.chdir(directorio)
    for root, dirs, files in os.walk("."):
        for name in files:
          if name.endswith('.png'):
            lista.append(name)
    os.chdir(actual)

    return lista



def f_principal(parametros):
    if len(parametros) != 1:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ')
        archivos_png(parametros)
    return

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    