s=input()
a = int(s[:2])
b = int(s[2:])

yymm, mmyy = False, False

if 1 <= b <= 12: yymm = True
if 1 <= a <= 12: mmyy = True

if yymm and mmyy: print("AMBIGUOUS")
elif yymm: print("YYMM")
elif mmyy: print("MMYY")
else: print("NA")