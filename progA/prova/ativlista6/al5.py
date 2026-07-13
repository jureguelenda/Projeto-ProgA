ns = []
ns = list(map(int, input().split()))
k = 0
for i in ns:
  if i == ns[9]:
   k += 1
print(f'O numero {ns[9]} apareceu {k} vezes')