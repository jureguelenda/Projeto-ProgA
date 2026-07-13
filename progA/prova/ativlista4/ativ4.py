A = int(input())
B = int(input())
C = int(input())
if A == B and B == C:
    print("equilatero")
elif A != B and B != C and A != C:
    print("escaleno")
else:
    print("isosceles")
