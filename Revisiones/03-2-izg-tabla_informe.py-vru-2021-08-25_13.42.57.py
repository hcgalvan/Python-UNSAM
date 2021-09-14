# informe.py 
#3.9: La función zip()

import csv

#%% Precio pagado al conductor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        cabeceras = next(f).split(',')
        camion = []
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(cabeceras, fila))
            try:
               camion.append({'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio\n'])})

            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return camion

#%% Precio de venta
def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        diccionario = {}
        for i,linea in enumerate(filas):
            try:
                diccionario[linea[0]] = float(linea[1])
            except IndexError:
                print(f'Faltan datos en la línea {i+1}.')
                return diccionario

#%%

def hacer_informe(nombre_archivo1,nombre_archivo2):
	camion = leer_camion(nombre_archivo1)
	precios = leer_precios(nombre_archivo2)
	cabeceras = ('Nombre', 'Cajones', 'Precio', 'Cambio')
	sep = ('----------')
	print(f'{cabeceras[0]:>10s} {cabeceras[1]:>10s} {cabeceras[2]:>10s} {cabeceras[3]:>10s}')
	print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
	lista = []
	for s in camion:
		lista = ((s['nombre'],s['cajones'],'$'+str(s['precio']),precios[s['nombre']]-s['precio']))
		print('%10s %10d %10s %10.2f' % lista)

#hacer_informe('Data/camion.csv','Data/precios.csv')
hacer_informe('../Data/fecha_camion.csv','../Data/precios.csv')