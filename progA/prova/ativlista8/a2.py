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

def diagonal(mat):
  valor = False
  for i in range(len(mat)):
      if mat[i][i] == 0:
        valor = False
      else:
        valor = True
  if valor == True:
    print("OK")
  else:
    print("NOT OK")

n = int(input())

diagonal(lerMatriz(n))
        

      

