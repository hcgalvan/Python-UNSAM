import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        camion = []
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                camion.append({"nombre": row[0],"cajones": int(row[1]),"precio": float(row[2])})
        except:
            print('Datos incompletos!')
    return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precios = {}
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            if len(row) >= 3:
                print('Datos incompletos!')
    return precios

def calcular_balance(csv_camion, csv_precios):
    costo_camion = 0
    precios_venta = 0
    resultado = 0
    for producto in leer_camion(csv_camion):
        for precio, v in leer_precios(csv_precios).items():
            if producto['nombre'] == precio:
                precios_venta += (float(v)*producto['cajones'])
                costo_camion += (producto['precio']*producto['cajones']) # agregando los cajones
    balance = precios_venta - costo_camion
    if balance > 0:
        resultado = f'Hubo una ganancia de ${round(balance, 2)}'
    else:
        resultado = f'Hubo una perdida de ${round(balance, 2)}'

    print(f"El costo total fue de ${round(costo_camion, 2)} y la recaudacion fue de ${round(precios_venta, 2)}. {resultado} ")

#%%

calcular_balance('../Data/camion.csv','../Data/precios.csv') #corregir la ruta relativa

"""
Salida :
    
fruta: Lima Costo: 3220.00 Venta: 4022.00 Ganancia: 802.00
fruta: Naranja Costo: 4555.00 Venta: 5314.00 Ganancia: 759.00
fruta: Caqui Costo: 15516.00 Venta: 15819.00 Ganancia: 303.00
fruta: Mandarina Costo: 10246.00 Venta: 16178.00 Ganancia: 5932.00
fruta: Durazno Costo: 3835.15 Venta: 6980.60 Ganancia: 3145.45
fruta: Mandarina Costo: 3255.00 Venta: 4044.50 Ganancia: 789.50
fruta: Naranja Costo: 7044.00 Venta: 10628.00 Ganancia: 3584.00
Costo Total: 47671.15 Vta Total: 62986.10 Ganancia: 15314.95
"""