A,B,C,D=map(int,input().split())
c1=A # 水色
c2=0 # 赤色
count=0
for n in range(10**5*10):
    c1=A+B*n
    c2=C*n
    if c1<=c2*D:
        break
    count+=1
else:
    count=-1
print(count)
