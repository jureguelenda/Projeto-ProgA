notas = [float(x) for x in input().split()]
acima_da_media = len([nota for nota in notas if nota >= 5])
print(acima_da_media)