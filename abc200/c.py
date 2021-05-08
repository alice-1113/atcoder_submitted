import sys
input=sys.stdin.readline
from itertools import combinations

N=int(input())
A=list(map(int,input().split()))
d = {i:0 for i in range(200)}
for a,b in combinations(A,2):
    d[(a-b)%200]+=1
print(d[0])

# Python -> 30ms
# ? TLE
