N,X=map(int,input().split())
A=list(map(int,input().split()))

for i in range(1, N, 2):
    A[i]=A[i]-1

if X < sum(A):
    print("No")
else:
    print("Yes")