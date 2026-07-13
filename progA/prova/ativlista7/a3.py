def ordenaBolha3(lst, n):
     for i in range(len(lst)-1, len(lst)-1-n, -1) :
      borbulharAte3(lst, i)
      print(lista)

def borbulharAte3(lst, k):
   houveTroca = False
   for i in range(0, k):
      if lst[i] > lst[i+1]:
         lst[i], lst[i+1] = lst[i+1], lst[i]
         houveTroca = True
   return houveTroca

m, n = map(int, input().split())
lista = list(map(int,input().split()))
ordenaBolha3(lista, n)

