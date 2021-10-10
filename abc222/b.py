N,P=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for p in a:
    if p < P:
        cnt+=1
print(cnt)