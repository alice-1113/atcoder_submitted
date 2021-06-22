from math import factorial

def cc(n, r):
    return int(factorial(n)/factorial(r)/ factorial(n-r))

def main():
    N=int(input())
    A=tuple(map(int,input().split()))
    r=0
    i,j=0,0
    for _ in range(cc(N, 2)):
        pass
    print(r)

if __name__ == "__main__":
    main()