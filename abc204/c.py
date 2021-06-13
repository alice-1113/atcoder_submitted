N,M=map(int,input().split())
w=[(n+1,n+1) for n in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    for m in range(M):
        if A<m+1:
            w.append((A, m+1))
    if not w.count((A,B)):
        w.append((A,B))
print(w,len(w))

# わからない
