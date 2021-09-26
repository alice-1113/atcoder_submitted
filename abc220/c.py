N=int(input())
A=list(map(int, input().split()))
X=int(input())
x=0
k=0
i=1
while X>x:
    x+=A[i%N]
    i+=1
print(i-1)