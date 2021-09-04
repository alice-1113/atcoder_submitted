S,T = input().split()

s = sorted([S, T])[0] == S
if s is True:
    print("Yes")
else:
    print("No")
