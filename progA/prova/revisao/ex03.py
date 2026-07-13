def achatar(lista):
    resultado = []
    for item in lista:
        if type(item) == list:
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado

def achatar_comp(lista):
    if type(lista) != list:
        return [lista]
    
    numeros = [x for x in lista if type(x) != list]
    sublistas = [n for x in lista if type(x) == list for n in achatar(x)]
    
    return numeros + sublistas