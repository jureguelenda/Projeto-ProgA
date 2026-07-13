N = int(input())
desejos = {}
for i in range(N):
    lista_pessoas = input().split()
    desejos.update({lista_pessoas[0]: lista_pessoas[1:]})

palpites = input()


while palpites != 'FIM':
    lista_palpites = palpites.split()
    nome = lista_palpites[0]
    desejo = lista_palpites[1:]
    if nome in desejos:
        if desejo[0] in desejos[nome]:
             print('Uhul! Seu amigo secreto vai adorar')
        else:
             print('Tente Novamente!')
    else:
        print('Tente Novamente!')
    
    palpites = input()
