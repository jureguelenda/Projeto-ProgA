kwh = int(input())
if kwh <= 99:
    tarifa = 1.35
    valor = kwh * tarifa

elif kwh <= 299:
    tarifa = 1.55
    valor = kwh * tarifa

elif kwh >= 300 and kwh <= 574:
    tarifa = 1.75
    valor = kwh * tarifa

else:
    tarifa = 2.15
    valor = kwh * tarifa
    
if kwh >= 300:
    valor *= 1.10  

if valor <= 35:
    valor = 35.00

print(f'{valor:.2f}')
print(f'{tarifa:.2f}')
