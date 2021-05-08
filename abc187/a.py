def S(N):
    return int(N[0])+int(N[1])+int(N[2])

a, b = input().split()
if S(a) > S(b):
    print(S(a))
else:
    print(S(b))