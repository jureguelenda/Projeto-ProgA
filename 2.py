def pares(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
          print(n)
        pares(n - 1)
    

pares(int(input()))

    

    