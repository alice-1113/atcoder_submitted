from itertools import combinations

N,K=map(int,input().split())
c=list(map(int,input().split()))
nc=[]
s=set()
while c:
    for k in range(K):
        try:
            s.add(c.pop())
        except:
            break
    nc.append(len(s))
print(max(nc))