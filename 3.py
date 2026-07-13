def texto(n):
    if len(n) == 0 or len(n) == 1:
        return n
    if n[0] == n[1]:
        return texto(n[1:])
    else:
        return n[0] + texto(n[1:])

while True:
    s = input()
    if s == "*":
        break
    print(texto(s))