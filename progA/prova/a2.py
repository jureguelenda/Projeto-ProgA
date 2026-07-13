valor = float(input())
maior = valor
total = 0
qtd = 0
while valor != 0:
    if valor > maior:
        maior = valor
    total += valor
    qtd += 1
    valor = float(input())
print(f'QUANTIDADE: {qtd}')
print(f'TOTAL: {total:.2f}')
print(f'MAIOR: {maior:.2f}')