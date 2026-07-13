def SomaFatorial(n):
    if n == 0:
        return 1
    else:
       return SomaFatorial(n - 1) * n

soma = 0

for i in range(5):
    n = int(input())
    if n % 3 == 0:
      soma += SomaFatorial(n)

print(soma)