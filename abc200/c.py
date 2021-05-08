import sys
input=sys.stdin.readline
from itertools import combinations

N=int(input())
A=list(map(int,input().split()))
ans=0

for a,b in combinations(A,2):
    if (a-b)%200 == 0:
        ans += 1
print(ans)

# 速度が足りない?? Pypy3 -> 120ms, Python -> 30ms
