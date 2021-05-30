N,K=map(int, input().split())
s= []

for i in range(1, N+1):
    for j in range(1, K+1):
        n = "{}0{}".format(i,j)
        s.append(int(n))
print(sum(s))