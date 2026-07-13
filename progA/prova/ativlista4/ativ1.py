mes = int(input())
ano = int(input())
def bissexto(ano):
    return (ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0)
if mes in 2 (1, 3, 5, 7, 8, 10, 12):
        print(31)
elif bissexto(ano) and mes == 2:
        print(29)
if mes == 2 and not bissexto(ano):
        print(28)
else:
       print(30)