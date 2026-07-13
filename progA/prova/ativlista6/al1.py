quant = int(input())
lista = []
lista2 = []
intercalar = []

for i in range(quant):
    lista.append(int(input()))

for i in range(quant):
    lista2.append(int(input()))

for i in range(quant):
    intercalar.append(lista[i])
    intercalar.append(lista2[i])

for it in intercalar:
    print(it)



