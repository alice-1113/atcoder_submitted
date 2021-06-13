N,Q=map(int,input().split())
A=set(map(int,input().split()))
A_n={i for i in range(N)}
X=list(A_n-A)
K=[]
for _ in range(Q+1):
    K.append(int(input()))
for k in K:
    print(X[k])