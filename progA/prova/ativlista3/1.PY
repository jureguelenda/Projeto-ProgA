num1 = float(input())
num2 = float(input())
num3 = float(input())
media = (num1 + num2 + num3)/3
valor = 0
if num1 > media: 
    valor = valor + 1
if num2 > media:
    valor = valor + 1
if num3> media:
    valor = valor + 1
print(valor)
