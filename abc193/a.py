N=int(input())
s=[]
sl=[]
for n in range(N):
    a,b=map(int,input().split())
    s.append((a,b))
    sl.append(a+b)
for i,m in enumerate(s):
    for j,l in enumerate(s):
        if i==j: continue
        sl.append(max(m[0], l[1]))
print(min(sl))