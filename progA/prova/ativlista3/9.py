tipo = input()
num1 = int(input())
num2 = int(input())
num3 = int(input())
def MediaA(num1, num2 , num3):
   return  (num1 + num2 + num3)/3
def MediaH(num1, num2 , num3):
   return 3/(1/num1 + 1/num2 + 1/num3)
def MediaG(num1, num2 , num3): 
    return (num1*num2*num3)**(1/3)
if tipo == "A":
    print(f'{MediaA(num1, num2, num3):.3f}')
if tipo == "H":
    print(f'{MediaH(num1, num2, num3):.3f}')
if tipo == "G":
    print(f'{MediaG(num1, num2, num3):.3f}')