def mypow(x, n):
    res=1
    while n>0:
        if n&1: res*=x
        x*=x
        n>>=1
    return res

def main():
    A,B,C=map(int,input().split())
    x=mypow(A,C)
    y=mypow(B,C)
    print("<" if x<y else ">" if x>y else "=")

if __name__ == "__main__":
    main()