N=int(input())
A=tuple(map(int, input().split()))
B=tuple(map(int, input().split()))
n=0
for a,b in zip(A,B):
    n+=a*b
if n==0:
    print("Yes")
else:
    print("No")