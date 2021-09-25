# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:56:41 2021

@author: User
"""

# 7.3 El módulo principal
# Python no tiene una función o método principal. 
# En su lugar existe un módulo principal y éste será el archivo 
# con código fuente que se ejecuta primero.
#        bash % python3 prog.py 
#%% Chequear __main__
# Es una práctica estándar usar la siguiente convención en módulos que son ejecutados como scripts principales:
# prog.py
...
if __name__ == '__main__':
    # Soy el programa principal ...
    comandos
    ...
# Los comandos dentro del if constituyen el programa principal
#%% Módulo principal vs. módulo importado
# Cualquier archivo .py puede ejecutarse ya sea como el programa principal o como un módulo importado:
bash % python3 prog.py # Corriendo como principal
import prog   # Corriendo como módulo importado
''' 
La variable __name__ es el nombre del módulo. 
Sin embargo, esta variable __name__ valdrá __main__ si ese módulo
 está siendo ejecutado como el script principal.
'''
if __name__ == '__main__':
    # Esto no se ejecuta en un módulo importado ...
#%% Modelo de programa
# Éste es un modelo usual para escribir un programa en Python:
# prog.py
# Comandos import (bibliotecas o módulos)
import modules

# Funciones
def spam():
    ...

def blah():
    ...

# Función principal
def f_principal():
    ...

if __name__ == '__main__':
    f_principal()    

#%% Herramientas para la consola
bash % python3 informe_final.py ../Data/camion.csv ../Data/precios.csv
# Esto permite que los scripts sean ejecutados desde la terminal para correr ciertos procesos automáticos, ejecutar tareas en segundo plano, etc.
#%% Argumentos en la línea de comandos
bash % python3 informe_final.py ../Data/camion.csv ../Data/precios.csv
bash % python3 -i informe_final.py ../Data/camion.csv ../Data/precios.csv

#  Te permite usar tu script para generar el informe con archivos de diferentes camiones o precios, pasados como parámetros por la línea de comandos:
import sys

if len(sys.argv) != 3:
    raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
camion = sys.argv[1]
precios = sys.argv[2]
...
# podés mirar el módulo argparse de Python

#%% Standard I/O  están definidos por el sistema operativo.
sys.stdout # (usualmente la pantalla)
sys.stderr # (usualmente el teclado)
sys.stdin # recapitulación de errores, usualmente, la pantalla otra vez

# Esta sintaxis se llama "piping" o redireccionamiento
bash % python3 prog.py > resultados.txt
# o si no
bash % cmd1 | python3 prog.py | cmd2


#%% Terminación del programa
# La terminación y salida del programa se administran a través de excepciones.
raise SystemExit
raise SystemExit(codigo_salida)
raise SystemExit('Mensaje informativo')
# O, alternativamente:
import sys
sys.exit(codigo_salida) # Es estándar que un codigo de salida de 0 indica que no hubo problemas y otro valor, que los hubo.

#%% El comando #! en Linux/Unix permite autoejecutarse el archivo desde comandos
# Por ejemplo, si agregás la siguiente línea al comienzo de tu script podés ejecutar directamente el script (sin invocar manualmente a Python en la misma línea). 

#!/usr/bin/env python3
# prog.py
...

# asignar derecho de ejecutable
bash % chmod +x prog.py
# Ahora lo podés ejecutar
bash % ./prog.py
... salida ...

# En windows que sucede
# Al iniciar un script Python en Windows, se lee la línea que comienza con #! dentro del script para saber qué versión del intérprete invocar.
#%% Modelo de script con parámetros
#!/usr/bin/env python3
# prog.py

# Import (bibliotecas)
import modules

# Funciones
def spam():
    ...

def blah():
    ...

# Funcion principal
def f_principal(parametros):
    # Analizar la línea de comandos, 
    # usando la variable parámetros en lugar 
    # de sys.argv, donde corresponda
    ...

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    
'''
Observación: Este modelo es flexible en el sentido que 
te permite escribir programas que podés llamar desde la terminal
 pasándole parámetros o ejecutar directamente dentro de 
 un intérprete usando import y llamando a su función main 
 como veremos en los siguientes ejercicios.
'''

#%% EJERCICIOS
# Ejercicio 7.4: Función principal
# Ejercicio 7.5: Hacer un script

