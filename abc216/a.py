
x,y=map(float, input().split("."))
if 0 <= y <= 2:
    print(str(int(x))+"-")
elif 3 <= y <= 6:
    print(int(x))
elif 7 <= y <= 9:
    print(str(int(x))+"+")