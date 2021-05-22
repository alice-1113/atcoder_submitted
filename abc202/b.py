S=input()
conv=str.maketrans({"6":"9","9":"6"})
print(S[::-1].translate(conv))