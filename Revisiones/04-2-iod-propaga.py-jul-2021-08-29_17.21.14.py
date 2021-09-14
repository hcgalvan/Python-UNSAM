def propaga(lista):
    
    buffer_1 = []
    buffer_0 = []

    for index,i in enumerate(lista):
        if i==1:
            buffer_1.append(index)
        elif i==0:
            buffer_0.append(index)
        else:
            continue
    
    for i in buffer_1:
        if (i+1) in buffer_0:
            buffer_1.append(i+1)
            buffer_0.remove(i+1)
        if (i-1) in buffer_0:
            buffer_1.append(i-1)
            buffer_0.remove(i-1)
    
    for i in buffer_1:
        lista[i]=1

    return lista

print ([0,-1,1,0,0,0,0,-1,0])
print (propaga([0,-1,1,0,0,0,0,-1,0]))
#%%
print(propaga([ -1*((i% 6)//2-1) for i in range(60) ]))
#%%
print(propaga([ 0, 0, 0, 1, 0, 0]))
#%%
print(propaga([ 0, 0, 0, 0, 0, -1]))
#%%      
print(propaga([ 0, 0, 0, 0, 0, 1]))
#%%
print(propaga( [] ))
#%%      
print(propaga([ 0 for _ in range(1000) ] + [1]))
#%%      
print(propaga( [1] + [ 0 for _ in range(1000) ]))
#%%
print(propaga([ (i% 6)//2-1 for i in range(200) ]))
#%%
print(propaga( [ -1*((i% 6)//2-1) for i in range(60) ]))