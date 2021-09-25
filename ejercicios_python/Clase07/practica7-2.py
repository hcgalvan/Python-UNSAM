# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:27:00 2021

@author: User
"""

# 7.2 Control de errores
# Formas en que los programas fallan

# Las funciones trabajarán sobre todo dato que sea compatible con las instrucciones dentro de la función.
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hola', 'mundo')    # 'Holamundo'
add('3', '4')           # '34'

#%%
# Si existen errores en una función, serán evidentes durante la ejecución de la función (en forma de una excepción).
def add(x, y):
    return x + y

#%% Excepciones
'''
Como ya dijimos, las excepciones son una forma de señalar 
errores en tiempo de ejecución. Acordate de que podés 
levantar una excepción usando la instrucción raise
'''
if nombre not in autorizados:
    raise RuntimeError(f'{nombre} no autorizado')
# Para atrapar una excepción, usá un bloque try-except
try:
    authenticate(nusuario)
except RuntimeError as e:
    print(e)

#%% Administración de excepciones

def grok():
    ...
    raise RuntimeError('Epa!')   # Levanta una excepción acá

def spam():
    grok()                        # Esta llamada va a levantar una excepción

def bar():
    try:
        spam()
    except RuntimeError as e:     # Acá atrapamos la excepción
        ...

def foo():
    try:
        bar()
    except RuntimeError as e:     # Por lo tanto la excepción no llega acá
        ...

foo()
#%%
'''
Cualquier instrucción hará que Python considere a la excepción como administrada, incluso un pass pero es pertinente realizar acciones relacionadas con la excepción específica a administrar.
'''
def grok(): ...
    raise RuntimeError('Epa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Excepción atrapada
        instrucciones           # Ejecuta estos comandos
        instrucciones
        ...

bar()
#%%
# Una vez atrapada la excepción, la ejecución continúa en la primera instrucción a continuación del try-except
def grok(): ...
    raise RuntimeError('Epa !')

def bar():
    try:
      grok()
    except RuntimeError as e:      # Excepción atrapada
        instrucciones
        instrucciones
        ...
    instrucciones                  # La ejecución del programa 
    instrucciones                  # continúa acá
    ...

bar()

#%% Excepciones integradas
 # La siguiente no es una lista completa.
ArithmeticError
AssertionError
EnvironmentError
EOFError
ImportError
IndexError
KeyboardInterrupt
KeyError
MemoryError
NameError
ReferenceError
RuntimeError
SyntaxError
SystemError
TypeError
ValueError
#%%
# Valores asociados a excepciones
raise RuntimeError('Nombre de usuario inválido')
# La instancia de la variable suministrada a except (en nuestros ejemplos e) lleva asociado este valor.
try:
    ...
except RuntimeError as e:   
    # `e` contiene la excepción lanzada con su mensaje específico
    ...

except RuntimeError as e:
    print('Fracasé. Motivo:', e)

    
#%% Podés atrapar múltiples excepciones
# Es posible atrapar diferentes tipos de excepciones en la misma porción de código, si incluís varios except en tu try:
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...

# Como alternativa, si las vas a procesar a todas de la misma manera, las podés agrupar:
try:
  ...
except (IOError, LookupError, RuntimeError) as e:
  ...
#%% Así NO se atrapan excepciones
try:
    hacer_algo()
except Exception:
    print('Hubo un error.')

#%% Así es un poco mejor.
try:
    hacer_algo()
except Exception as e:
    print('Hubo un error. Porque...', e)
    
# Sin embargo, por lo general es mejor atrapar errores específicos, y sólo aquellos que podés administrar.
#%% Re-lanzar una excepción
try:
    hacer_algo()
except Exception as e:
    print('Hubo un error. Porque...', e)
    raise
#%% Buenas prácticas al administrar excepciones
# La instrucción finally

lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # esto SIEMPRE se ejecuta. Haya o no haya excepciones.
# Una estructura como ésa resulta en un manejo seguro de los recursos disponibles (seguros, archivos, hardware, etc.)
#%% Ejercicios
# Ejercicio 7.1: Lancemos excepciones
#          Copiá el archivo fileparse.py al directorio de ejercicios de la clase actual
#          Modifcá tu código para que lance una excepción en caso que ambos parámetros select y has_headers = False sean pasados juntos.
# Ejercicio 7.2: Atrapemos excepciones
#        La función parse_csv() que escribiste está destinada a procesar un archivo completo. Pero en una situacion real, es posible que los archivos CSV de entrada estén "rotos", ausentes, o que su contenido no se adecúe al formato esperado. Probá esto:
#        >>> camion = parse_csv('../Data/missing.csv', types = [str, int, float])
# Ejercicio 7.3: Errores silenciados
#      Modificá parse_csv() de modo que le usuarie pueda silenciar los informes de errores en el parseo de los datos que agregaste antes, con un parámetro silence_errors
