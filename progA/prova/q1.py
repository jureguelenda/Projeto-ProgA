N = int(input())
apostas = []
for i in range(N):
    apostas_feitas = set(input().split(','))
    apostas.append(apostas_feitas)

resultado = set(input().split())
vencedores = 0

for aposta in apostas:
    if resultado.issubset(aposta):
        vencedores += 1

print(f'Total de ganhadores: {vencedores}')


