def g1(x):
    return "".join(sorted([y for y in str(x)], reverse=True))

def g2(x):
    return "".join(sorted([y for y in str(x)]))

def f(x):
    return int(g1(x)) - int(g2(x))

N,K=map(int,input().split())
for i in range(K):
    N=f(N)
print(N)