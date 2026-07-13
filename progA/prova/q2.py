N = int(input())
presentes = set()
quantidade_presentes = 0
for i in range(N):
    lista = set(input().split())
    presentes.update(lista)

for x in presentes:
    quantidade_presentes += 1

print(quantidade_presentes)