livros = int(input())
alunos = int(input())
analise = alunos / livros
if analise <= 8:
    print("A") 
elif analise <= 12:
    print("B")
elif analise <= 18:
    print("C")
else:
    print("D")
