N = int(input())
if N == 0:
    print("NULO")
elif N % 2 == 0 and N > 0:
    print("POSITIVO PAR")
elif N % 2 == 0 and N < 0:
    print("NEGATIVO PAR")
elif N % 2 != 0 and N > 0:
    print("POSITIVO IMPAR")
else:
    print("NEGATIVO IMPAR")