from collections import Counter

N=int(input())
n = {}

for _ in range(N):
    i = input()
    if i in n.keys():
        n[i] = 1
    else:
        n.setdefault(i, 0)

if 1 in list(n.values()):
    print("Yes")
else:
    print("No")