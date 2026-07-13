array1 = set()

for i in range(20):
    array1.add(int(input()))

array2 = set()

for i in range(20):
    array2.add(int(input()))

inter = array1 & array2

if not inter:
    print('VAZIO')
else:
    for k in inter:
        print(k)