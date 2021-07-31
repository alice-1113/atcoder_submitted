li = []

for _ in range(4):
    li.append(input())

an = {"H":0, "2B":0, "3B":0, "HR":0}

for l in li:
    if l in an:
        an[l] += 1

res = True

for a in an.values():
    if a < 1:
        res = False

if res:
    print("Yes")
else:
    print("No")