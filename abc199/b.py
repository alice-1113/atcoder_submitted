N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ANS=[set(range(A[i],B[i]+1)) for i in range(N)]
res=ANS[0]
for ans in ANS[1:]:
    res=set(res)&ans
print(len(res))