def paraInteiro(ss) :
  for i in range(len(ss)) :
    ss[i] = int(ss[i])

def lerMatriz(n) :
  matriz = []
  for _ in range(n) :
    fila = input().split()
    paraInteiro(fila)
    matriz.append(fila)
  return matriz

def somaAcima(mat):
  soma = 0
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if j > i :
        soma += mat[i][j]
  return soma

def somaAbaixo(mat):
  soma = 0
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if j < i :
        soma += mat[i][j]
  return soma


lado = input()
limiar = int(input())
m = int(input())

if lado == "acima":
  if somaAcima(lerMatriz(m)) > limiar:
    print(True)
  else:
    print(False)

if lado == "abaixo":
  if somaAbaixo(lerMatriz(m)) > limiar:
    print(True)
  else:
    print(False)