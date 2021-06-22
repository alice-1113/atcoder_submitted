N=int(input())
r=0
for i, d in enumerate(range(1, N+1), 1):
    r+=d
    if N <= r:
        break
print(i)