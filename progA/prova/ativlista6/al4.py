def acima (notas,media):
   p = media * 1.1
   k = 0
   for i in notas:
      if i > p:
         k += 1
   return k
def abaixo (notas,media):
   p = media * 0.9
   k = 0
   for i in notas:
      if p > i:
         k += 1
   return k
n = int(input())

notas = []

for i in range (n):
   valor = float(input())
   notas.append(valor)
soma = sum(notas)
media = soma/n
print(f'{media:.2f}')
print(acima(notas,media))
print(abaixo(notas,media))