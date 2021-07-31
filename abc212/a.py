p=print
A,B=map(int,input().split())

if 0<A and B==0:
    p("Gold")
elif A==0 and 0<B:
    p("Silver")
elif 0<A and 0<B:
    p("Alloy")