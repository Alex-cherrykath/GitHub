#include<stdio.h>
int main()
{
    int i;
    int n,f;
    printf("Entrer un nombre");
    scanf ("%d",&n);
    //verification de la nature du nombre
    if(n<0){
        printf( "Impossible");
        printf("Entrer un nombre positif./n");
        scanf("%d",&n);
    } else{
            f=1; 
        for(i=1; i<=n; i++){
            f*=i;
        }
        printf( "le factoriel est", "%d\n", f );     
    }
    return f;
}
