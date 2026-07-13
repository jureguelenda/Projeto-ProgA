def ordenaBolha3(lst) :
  for i in range(len(lst)-1, 0, -1) :
    if not borbulharAte3(lst, i) :
      return

def borbulharAte3(lst, k) :
  houveTroca = False
  for i in range(0, k) :
    if lst[i] > lst[i+1] :
      lst[i], lst[i+1] = lst[i+1], lst[i]
      houveTroca = True
  return houveTroca

quantidade = int(input())
lista = []

for i in range(quantidade):
  numeros = [int(input())]
  lista.append(numeros)

ordenaBolha3(lista)
for elemento in lista:
    print(f"[{elemento}]", end="")
