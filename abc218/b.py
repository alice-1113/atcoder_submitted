import string
P=map(int,input().split())

alph = string.ascii_lowercase

s = ""

for i in P:
    s += alph[i-1]

print(s)