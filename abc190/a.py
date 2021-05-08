A,B,C=map(int,input().split())
for _ in range(A+B+1):
    if C%2==0:
        if A==0:
            print("Aoki")
            break
        A-=1
    else:
        if B==0:
            print("Takahashi")
            break
        B-=1
    C+=1