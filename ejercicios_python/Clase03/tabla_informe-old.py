"""
Este programa funciona si estas ubicado en "..\Ejercicio\Clase02\"

@author:  Hugo César Galván


"""
#informe.py
"""
Realiza el balance de las operaciones en frutería en base a los
precios y el valor de cada fruta por cajón

Usa técnica para elegir las columnas a partir de sus encabezados.
"""
import csv
# Armamos un diccionario con cada tipo de 
def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    encabezados = next(rows)
    # next(rows)
    camion = []
    lote = {}
    for n_fila, fila in enumerate(rows, start=1):
        record = dict(zip(encabezados, fila))
        lote ['nombre'] = record['nombre']
        lote ['cajones'] = int(record['cajones'])
        lote ['precio'] = float(record['precio'])
        camion.append(lote)      
        lote = {}
    f.close()
    return camion


def leer_precios(nombre_archivo):
    dic_precio = {}
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    for row in rows:
        if len(row)>1:
            dic_precio[row[0]] = float(row[1])
        else:
            continue
    return dic_precio
    f.close()   


def hacer_informe(camion, precios):
   # from collections import Counter
    camion = leer_camion(camion)
    precios = leer_precios(precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    #fruta = []
    #cajon = []
    #preciof = []
    #fruteria = []
    frutavta = []
    #frutas = {}
    #informe = Counter()
    for s in camion:
        for k, v in precios.items():
            if (s['nombre'])== k:
                fruta1 = ( s['nombre'], s['cajones'], s['precio'], float(v)-float(s['precio']) )
                frutavta.append(fruta1)
                #frutavta.append(s['nombre'], s['cajones'], s['precio'], float(v)-float(s['precio']) )
            #frutas.(s['nombre'],s['cajones'],s['precio']))
        #fruta.append(s['nombre'])
        #cajon.append(s['cajones'])
        #preciof.append(s['precio'])
        #print(fruta)
        #fruta = list(dict(s['nombre'].values))
    #for s, v in precios.items():
        #frutavta.append(s)
        
    #print(fruta,cajon,preciof,frutavta)
    #print(frutavta)

    '''
    #cambio = 0
    for s in camion:
        for k, v in precios.items():
            if s['nombre'] == k:
                #fruteria[s['nombre']] = s['nombre']
                #frutas['nombre'] = s['nombre']
                #frutas['cajones'] = s['cajones']
                #frutas['precio'] =  s['precio']
                #frutas['cambio'] = (float(v)-float(s['precio']))
                lista=list(zip(frutas.values(),frutas.keys()))
                fruteria.append(lista)
    #print(fruteria)
    #for nombre, cajones, precio, cambio in fruteria:
        #informe[nombre] += cajones
        
        #print(tenencias_camion)
        #print(ventas_fruta)
    
    '''
    
    
    print('%10s %10s %10s %10s' % headers) #print(fruta)
    print('---------- ---------- ---------- ----------')
    for r in frutavta:
        print('%10s %10d %10.2f %10.2f' % r) #print(fruta)
    return 
    
def balance (camion, precios):
    camion = leer_camion(camion)
    costo_total = 0
    precios = leer_precios(precios)
    venta = 0
    costo_unit = 0
    vta_unit = 0
    ganancia = 0
    gcia_total = 0
    for row in camion:
        #print (row['nombre'],row['precio'])
        for k, v in precios.items():
            if row['nombre'] == k:
                costo_unit = (int(row['cajones'])*float(row['precio']))
                vta_unit = int(row['cajones'])*float(v)
                ganancia = vta_unit - costo_unit
                costo_total += costo_unit
                venta += vta_unit
                gcia_total += ganancia
                print (f'fruta: {k} Costo: {costo_unit:0.2f} Venta: {vta_unit:0.2f} Ganancia: {ganancia:0.2f}')
            else:
                continue
    return print(f'Costo Total: {costo_total:0.2f} Vta Total: {venta:0.2f} Ganancia: {gcia_total:0.2f}')
#%%
print ( balance('../Data/camion.csv', '../Data/precios.csv'))
#%%
informes = hacer_informe('../Data/camion.csv', '../Data/precios.csv')
#print(informes[0])

