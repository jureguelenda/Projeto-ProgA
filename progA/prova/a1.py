def calcular_total(preco, qtd):
    total = preco * qtd
    if qtd >= 10:
        desconto = total * 0.20
    elif qtd >= 5:
        desconto = total * 0.10
    elif qtd >= 3:
        desconto = total * 0.05
    else:
        desconto = 0
    return total - desconto

n = int(input())
soma = 0
for i in range(n):
    nome = input()
    preco = float(input())
    qtd = int(input())
    calcular_total(preco, qtd)
    soma += calcular_total(preco, qtd)
    print(f'{nome}: {calcular_total(preco, qtd):.2f}')

print(f'TOTAL: {soma:.2f}')
    