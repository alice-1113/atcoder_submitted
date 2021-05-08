N,S,D=map(int,input().split())
XY=[tuple(map(int,input().split())) for _ in range(N)]
ans=["No","Yes"]
r=False
for i in range(N):
    if XY[i][0] < S and XY[i][1] > D:
        r=True
print(ans[r])