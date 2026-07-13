dia = int(input())
km = int(input())
diaria = dia * 90
km_dias = dia * 100
km_taxa = 0
if km > km_dias:
    km_extra = km - km_dias
    km_taxa = km_extra * 12
valor = diaria + km_taxa
print(f'{valor:.2f}')
       
   
    