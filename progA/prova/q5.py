dic = dict()

frase = input()

for letra in frase:
    dic[letra] = dic.get(letra)

for letra in dic:
    print(letra)

