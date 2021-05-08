from math import log
N=int(input())
A=tuple(map(int, input().split()))
B=A[:]
while len(A)>2:
    n=[]
    for i in range(0, 2**N, 2):
        if A[i]>A[i+1]:
            n.append(A[i])
        else:
            n.append(A[i+1])
    N=int(log(len(n),2))
    A=n
print(B.index(min(A))+1)