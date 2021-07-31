N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
m=float("inf")
for a in range(N):
    for b in range(M):
        d = abs(A[a]-B[b])
        if m > d:
            m = d
print(m)
