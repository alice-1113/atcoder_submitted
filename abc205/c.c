#include <stdio.h>

long int mypow(long x, int n){
    long int res=1;
    while(n>0){
        if(n&1) res*=x;
        x*=x;
        n>>=1;
    }
    return res;
}

int main(void){
    long int A,B,C,x,y;
    scanf("%ld %ld %ld", &A, &B, &C);
    x=mypow(A,C);
    y=mypow(B,C);
    if (x<y) printf("<\n");
    else if(x>y) printf(">\n");
    else if(x==y) printf("=\n");
}