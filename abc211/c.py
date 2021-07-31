from itertools import combinations

S=input()
m=10**9+7
c = 0
for i in combinations(S, 8):
    if "".join(i) == "chokudai":
        c+=1
print(c%m)