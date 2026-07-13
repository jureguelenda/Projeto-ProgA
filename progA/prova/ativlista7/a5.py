lista = []
nomes = input()

while nomes != "FIM":
   lista.append(nomes)
   nomes = input()

lista.sort()

for i in lista:
    print(i)

n = int(input())

while n != 0:
    print("-" * 50)
    for _ in range(n):
        novo_nome = input()
        lista.append(novo_nome)
        posicao = len(lista) - 1
        
        while posicao > 0 and lista[posicao] < lista[posicao - 1]:
            lista[posicao], lista[posicao - 1] = lista[posicao - 1], lista[posicao]
            posicao -= 1
        
    for i in lista:
     print(i) 
    
    n = int(input())