s=input()

for i, a in enumerate(s, 1):
    if i%2==0:
        if not a.isupper():
            print("No")
            break
    else:
        if not a.islower():
            print("No")
            break
else:
    print("Yes")