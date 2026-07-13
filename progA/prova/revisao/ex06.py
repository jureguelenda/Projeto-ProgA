texto = input()
print(len([letra for letra in texto.lower() if letra in 'aeiou']))