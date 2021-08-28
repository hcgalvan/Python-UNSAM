# Adelantos.py
# Archivo de ejemplo
# Ejercicio de Adelantos en pagos de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
adelanto = 1000
mes = 0
total_pagado = 0.0
  
while saldo > 0:
    if mes < 12:
        saldo = saldo  * (1+tasa/12) - (pago_mensual + adelanto)
        total_pagado = total_pagado + (pago_mensual + adelanto)
        mes = mes + 1
    else:            
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes = mes + 1
    
print('Total pagado', round(total_pagado,2), 'en ', mes,' meses.')
