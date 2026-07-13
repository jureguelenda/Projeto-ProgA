N = int(input())
i = 1
soma = 0
while i <= N:
   numerador = i
   denominador = i * 3
   termo = numerador / denominador
   soma += termo
   if i < N:
      print(f"{numerador}/{denominador}", end=" + ")
   else:
      print(f"{numerador}/{denominador}")
   i += 1
print(f"{soma:.2f}")