n = int(input())
primos = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primos)