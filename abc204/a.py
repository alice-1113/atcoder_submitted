x,y=map(int,input().split())
r=0
if x==y:
    r=x
else:
    r=list({0,1,2}-set([x,y]))[0]
print(r)