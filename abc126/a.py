n,k=map(int,input().split())
s=input()
ns = ""
for i,a in enumerate(s):
    if k-1 == i:
        ns+=a.lower()
    else:
        ns+=a
print(ns)