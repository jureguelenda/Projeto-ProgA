n = int(input())

lista_cpf = []
while len(lista_cpf) < n:
    cpf = int(input())
    lista_cpf.append(cpf)


lista_notas = []
while len(lista_notas) < n:
    notas = int(input())
    lista_notas.append(notas)


m = int(input())
for i in range(m):
    consulta_cpf = int(input())
    achou = False
    for posicao in range(n):
        if lista_cpf[posicao] == consulta_cpf:
            print(lista_notas[posicao])
            achou = True
            break
    if not achou:
        print('NAO SE APRESENTOU')

   
       
         