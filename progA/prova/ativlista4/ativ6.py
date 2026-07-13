A = int(input())
B = int(input())
C = int(input())
if A == B and A == C:
    print(1)
elif A != B and B != C and A != C:
    print(2)
else: 
    print(3)