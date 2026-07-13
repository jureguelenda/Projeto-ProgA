valor = float(input())
garantia = int(input())
if garantia == 0:
    print(f'{valor:.2f}')
elif garantia == 1:
    taxa = valor * 1.03
    print(f'{taxa:.2f}')
elif garantia == 2:
    taxa = valor * 1.05
    print(f'{taxa:.2f}')