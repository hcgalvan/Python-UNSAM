def bbinaria_rec(lista, e):
    
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
            
        if lista[medio] > e:
            if lista[medio-1] == e:
                res = True     # elemento encontrado!
            else:
                der = medio - 1 # descarto mitad derecha
                return bbinaria_rec(lista[:der], e)
        else:
            if lista[medio] == e:
                 res = True     # elemento encontrado!
                 # if lista[medio] < x:
            else:
                 izq = medio + 1 # descarto mitad izquierda
                 return bbinaria_rec(lista[izq:], e)
       

    return res
