def paraInteiro(ss):
    for i in range(len(ss)):
        ss[i] = int(ss[i])

def lerMatriz(n):
    matriz = []
    for _ in range(n):
        fila = input().split()
        paraInteiro(fila)
        matriz.append(fila)
    return matriz

n, m = map(int, input().split())
matriz_maior = lerMatriz(n)

r, s = map(int, input().split())
matriz_menor = lerMatriz(r)

soma = 0

for i in range(n - r + 1):
    for j in range(m - s + 1):
        casamento = True
        for k in range(r):
            for l in range(s):
                if matriz_maior[i + k][j + l] != matriz_menor[k][l]:
                    casamento = False
                    break
            if not casamento:
                break
        if casamento:
            soma += 1

print(soma)

 
