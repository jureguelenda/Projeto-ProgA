A = int(input())
B = int(input())
C = int(input())
if A == B == C:
    print("*")
elif B != A and B != C and A == C:
    print("B")
elif A != C and B == C:
    print("A")
else:
    print("C")
