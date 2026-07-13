def diasAteInicioDoMes(mes):
    if mes == 1 :
        return 0
    elif mes == 2 :
        return 31
    elif mes == 3 :
        return 59
    elif mes == 4 :
        return 90
    elif mes == 5 :
        return 120 
    elif mes == 6 :
        return 151
    elif mes == 7 :
        return 181
    elif mes == 8 :
        return 212
    elif mes == 9 :
        return 243
    elif mes == 10 :
        return 273
    elif mes == 11 :
        return 304
    else : # mes == 12 
        return 334
dia = int(input())
mes = int(input())
ano = int(input())
saoj = diasAteInicioDoMes(6) + 24
diaA = diasAteInicioDoMes(mes) + dia
def bissexto(ano):
    return (ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0)
def ajustarbissexto (ano, mes, dia):
    return ((mes == 1 or (mes == 2 and dia <= 28)) and bissexto(ano)) or (
        ((mes == 6 and dia >= 25) or mes > 6) and bissexto(ano + 1))
if saoj == diaA:
    print("Viva Sao Joao")
else:
    if saoj > diaA:
        diasate = saoj - diaA
    else: 
        diasate = 365 - diaA + saoj   
    if ajustarbissexto(ano, mes, dia):
        diasate += 1
    print(f"Faltam {diasate} dias para o Sao Joao chegar")
