# Ejercicio 4.6: Propagación

#Funcion propagar()
def propagar(lista):
    lo = len(lista)
    #  -->  De izquierda a derecha
    for n, e in enumerate(lista):
        if e == 1:
            try:
                if lista[n+1] == 0:
                    lista[n+1] = 1
            except IndexError:
                continue
    
    #  De derecha a izquierda  <---
    p = lo - 1
    while p >= 0:
        if lista[p] == 1:
            if lista[p-1] == 0:
                lista[p-1] = 1  
        p -= 1
    return lista

# =============================================================================
# Ejemplos:
# d = propagar([ 0, 0, 0, 1, 0, 0])
# d = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# =============================================================================
#%%
print(propagar([ -1*((i% 6)//2-1) for i in range(60) ]))
#%%
print(propagar([ 0, 0, 0, 1, 0, 0]))
#%%
print(propagar([ 0, 0, 0, 0, 0, -1]))
#%%      
print(propagar([ 0, 0, 0, 0, 0, 1]))
#%%
print(propagar( [] ))
#%%      
print(propagar([ 0 for _ in range(1000) ] + [1]))
#%%      
print(propagar( [1] + [ 0 for _ in range(1000) ]))
#%%
print(propagar([ (i% 6)//2-1 for i in range(200) ]))
#%%
print(propagar( [ -1*((i% 6)//2-1) for i in range(60) ]))               