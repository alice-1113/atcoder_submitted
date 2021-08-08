N=int(input())
A=list(map(int,input().split()))
B=sorted(A.copy())[-2]
print(A.index(B)+1)