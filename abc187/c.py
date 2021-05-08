N = int(input())
S = {input() for s in range(N)}

for s in S:
    if s[0] == "!":
        if s.replace("!", "") in S:
            print(s.replace("!", ""))
            break
else:
    print("satisfiable")