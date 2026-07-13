def borbulharAte3(lst, k) :
  houveTroca = False
  for i in range(0, k) :
    if lst[i] > lst[i+1] :
      lst[i], lst[i+1] = lst[i+1], lst[i]
      houveTroca = True
  return houveTroca

def borbulharAte3decrescente(lst, k) :
  houveTroca = False
  for i in range(0, k) :
    if lst[i] < lst[i+1] :
      lst[i], lst[i+1] = lst[i+1], lst[i]
      houveTroca = True
  return houveTroca

def ordenaBolha3(lst) :
  i = len(lst)-1
  while borbulharAte3(lst, i) :
    i -= 1

def ordenaBolha3decrescente(lst) :
  i = len(lst)-1
  while borbulharAte3decrescente(lst, i) :
    i -= 1
num1 = int(input())
num2 = int(input())
num3 = int(input())
numeros = [num1, num2, num3]

if num1 < 0 or num2 < 0 or num3 < 0:
  print("Ordenacao cancelada.")

elif num1 % 2 == 0:
  ordenaBolha3decrescente(numeros)
  for elemento in numeros:
    print(elemento)


else:
  ordenaBolha3(numeros)
  for elemento in numeros:
    print(elemento)
