X = int(input())
Y = int(input())
soma = X + Y
def e_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if not e_primo(X):
    print(f'O numero {X} nao eh primo')
elif not e_primo(Y):
    print(f'O numero {Y} nao eh primo')
else:
    if e_primo(soma):
        print(f'A soma de {X} e {Y} eh um primo')
    else:
        print(f'A soma de {X} e {Y} nao eh um primo')

    


    
       