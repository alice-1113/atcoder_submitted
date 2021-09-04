S1=input()
S2=input()
S3=input()

s = {
    "ABC": 0,
    "ARC": 0,
    "AGC": 0,
    "AHC": 0
}

s[S1] += 1
s[S2] += 1
s[S3] += 1


for k, v in s.items():
    if v == 0:
        print(k)