X=list(map(int, input().split()))
if max(X)<min(X)+3:
    print("Yes")
else:
    print("No")