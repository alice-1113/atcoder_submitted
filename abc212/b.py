X=input()
c1 = len(set(X)) <= 1
c2 = "1234", "2345", "3456", "4567", "5678", "6789", "7890", "8901", "9012", "0123"
if c1 or (X in c2): print("Weak")
else: print("Strong")