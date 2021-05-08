from itertools import combinations
N=int(input())
s=(tuple(map(int, input().split())) for _ in range(N))
c,t=combinations(s, 2),0
for v in c:
    if -1 <= ((v[1][1]-v[0][1])/(v[1][0]-v[0][0])) <= 1:
        t+=1
print(t)