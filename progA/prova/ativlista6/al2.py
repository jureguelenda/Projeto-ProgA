n = int(input())
lista = []
lista = list(map(int, input().split()))
menor = min(lista)
p = lista.index(menor)
print(f'Menor valor: {menor}')
print(f'Posicao: {p}')

   