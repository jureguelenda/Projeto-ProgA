def ordenarSelecao(lst, n):
   for i in range(0 , n):
       pos_menor = indiceDoMenorDesde(i, lst)
       lst[i], lst[pos_menor] = lst[pos_menor], lst[i]
       print(lst)

def indiceDoMenorDesde(inicio, lst):
   pos_menor = inicio
   for pos in range(pos_menor+1, len(lst)):
     if lst[pos] < lst[pos_menor]:
       pos_menor = pos
   return pos_menor

m, n = map(int, input().split())
lista = list(map(int, input().split()))
ordenarSelecao(lista, n)