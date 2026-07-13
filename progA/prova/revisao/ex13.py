matriz = [[int(x) for x in linha.split()] for linha in input().split(",")]
pares = [num for linha in matriz for num in linha if num % 2 == 0]
print(pares)