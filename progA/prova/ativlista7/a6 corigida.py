n = int(input())

lista_cpf = []
while len(lista_cpf) < n:
    cpf = int(input())
    lista_cpf.append(cpf)

lista_notas = []
contador = 0
while contador < n:
    notas = int(input())
    cpf_do_aluno = lista_cpf[contador]
    
    while len(lista_notas) <= cpf_do_aluno:
        lista_notas.append(-1)
        
    lista_notas[cpf_do_aluno] = notas  
    contador += 1

m = int(input())
for i in range(m):
    consulta_cpf = int(input())
    
    if consulta_cpf >= len(lista_notas) or lista_notas[consulta_cpf] == -1:
        print('NAO SE APRESENTOU')
    else:
        print(lista_notas[consulta_cpf])