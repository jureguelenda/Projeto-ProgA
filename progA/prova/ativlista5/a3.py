num = float(input())
total = num
meta = 0
i = 2
while i <= 7:
    valor = num
    num = float(input())

    total += num
    if num >= (valor + 0.50):
        meta += 1
    
    dia += 1

print(f"R$ {total:.2f}")
print(meta)