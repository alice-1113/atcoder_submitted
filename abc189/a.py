from collections import Counter
C=[c for c in input()]
for _,v in Counter(C).items():
    if v == 3:
        print("Won")
        break
else:
    print("Lost")