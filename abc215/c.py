from itertools import permutations

s,k = input().split()
k = int(k)
coms = list(permutations(list(s), len(s)))
coms = sorted(list(set(coms)))

print("".join(coms[k-1]))