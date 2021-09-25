# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:18:21 2021

@author: User
"""

# 7.6 Estilos de codeo
# PEP 8 - La guía de estilo para Python
# La comunidad de usuaries de Python ha adoptado una guía de estilo que facilita la lectura del código y la consistencia entre programas de distintos usuaries
'''
 Indentación : Utilizar siempre 4 espacios y nunca mezclar tabuladores y espacios.
 Tamaño máximo de línea: Las líneas deben limitarse a un máximo de 79 caracteres.
 Líneas en blanco: Separar las definiciones de las clases y funciones con dos líneas en blanco. Los métodos dentro de clases se separan con una línea en blanco
 Imports: Los imports de distintos módulos deben estar en líneas diferentes
  Sí se pueden poner en una línea los elementos que se importan de un mismo módulo
  from subprocess import Popen, PIPE
  Los imports deben ponerse siempre al principio del archivo, justo después de los comentarios y de la documentación del archivo y antes de la definición de las variables globales y las constantes.
    Los imports deben agruparse en el siguiente orden:
    
    bibliotecas o módulos estándar.
    bibliotecas o módulos de terceros.
    bibliotecas o módulos locales o propios.
    
    Cada grupo de imports debe estar separado por una línea en blanco.
 Espacios en blanco en expresiones: Evitar espacios en blanco extra en: 
     Dentro de paréntesis, corchetes o llaves.
    # Sí: 
    spam(ham[1], {eggs: 2})
    # No:  
    spam( ham[ 1 ], { eggs: 2 })

    Antes de una coma.
    
    # Sí: 
    if x == 4: print x, y; x, y = y, x 
    # No: 
    if x == 4 : print x , y ; x , y = y , x

    # Sí: 
    spam(1)
    # No, ese espacio es espantoso
    spam (1)

    Antes del corchete de un índice o clave.
    
    # Sí: 
    dict['key'] = list[index]
    # No, ese espacio es igual de espantoso que el anterior
    dict ['key'] = list [index]

    Siempre separá los operadores binarios con un espacio simple a ambos lados: asignación (=), asignación aumentada (+=, -= , etc.), comparación (==, <, >, !=, <>, <=, >=, in, not in, is, is not), booleanos (and, or, not).
    Usá espacios alrededor de operadores artiméticos:
    
    # Sí:
    i = i + 1
    submitted += 1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)
    # No:
    i=i+1
    submitted +=1
    x = x*2 - 1 #no es recomendado pero a veces lo usamos
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

 Convenciones de nombres: algunas de las recomendaciones actuales sobre nombres.
 Estilos de nombres: 
  Éstos son algunos estilos:
    b (una sola letra, en minúscula)
    B (una sola letra, en mayúscula)
    minusculas
    minusculas_con_guiones_bajos
    MAYUSCULAS
    MAYUSCULAS_CON_GUIONES_BAJOS
    PalabrasConMayusculas (también llamado estilo camello por las jorobas)
    mixedCase (difiere del camello en la inicial)
    Con_Mayusculas_Y_Guiones_Bajos (horrible!)
    no usar acentos ni caracteres especiales
    
 El código no es solo leído: el código de percibe: 
     un código en Python no solo lee el código sino que percibe su diseño en el espacio, el uso de bloques y espacios, de indentaciones y mayúsculas. 

##################
El PEP 20 (PEP viene de Python Enhancement Proposals), también conocido como el Zen de Python

AL ESCRIBIR EN INTERPRETE DE COMANDOS: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

######### EN ESPAÑOL ##############
Zen de Pyhton

Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Espaciado es mejor que denso.
La legibilidad es importante.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Sin embargo la practicidad le gana a la pureza.
Los errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitá la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
A pesar de que esa manera no sea obvia a menos que seas Holandés.
Ahora es mejor que nunca.
A pesar de que nunca es muchas veces mejor que justo ahora.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea, ¡hagamos más de ellos!


'''