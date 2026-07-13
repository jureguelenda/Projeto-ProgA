def vantagem(candidato, concorrente, n):
    maior_p = 0.00
    
    for i in range(n):
        if candidato[i] > concorrente[i]:
            p_atual = candidato[i] - concorrente[i]
            if p_atual > maior_p:
                maior_p = p_atual
                
    return maior_p

n = int(input())
lista_candidato = list(map(float, input().split()))
lista_concorrente = list(map(float, input().split()))

k = vantagem(lista_candidato, lista_concorrente, n)

print(f"{k:.2f}")