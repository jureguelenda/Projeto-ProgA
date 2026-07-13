def matriz(n, f):
    matriz = []
    for i in range(n):
        linhas = []
        for i in range(f):
            numeros = int(input())
            linhas.append(numeros)
        matriz.append(linhas)
    return matriz

def produto(mat):
    valor = 0
    for i in range(mat):
     valor += sum(mat[i])
    
def filial(mat,f,n):
   for j in range(len(f)):
      valor = 0
      for i in range(len(n)):
         valor += mat[i][j]
   return valor
      
n, f = map(int, input().split())
minha_matriz = matriz(n,f)
print(filial(minha_matriz,f,n))
print(produto(minha_matriz))
print(minha_matriz)
