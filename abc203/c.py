N,K=map(int,input().split())  # 友達, 所持金
AB=[0]*N
c=0
f=0
for i in range(N):
    AB[i]=list(map(int,input().split()))  # i人目の友達Ai, Biを太郎君にA
AB.sort(key=lambda x: x[0])
while K:
    while AB[f][0] == c:
        K += AB[f][1]
        if f+1 < N:
            f += 1
    c+=1
    K-=1
print(c)

# エラーがある.
