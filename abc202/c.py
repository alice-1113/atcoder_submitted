from itertools import product
from sys import stdin

def main():
    input=stdin.readline
    n=int(input())
    A=tuple(map(int,input().split()))
    B=tuple(map(int,input().split()))
    C=tuple(map(int,input().split()))
    s=(A[i]==B[C[j]-1] for i,j in product(range(n), repeat=2))
    print(s.count(True))

if __name__ == "__main__":
    main()