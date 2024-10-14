#include <iostream>
#include <cmath> 
//fonction factorielle necessaire pour les termes du dl
double factorielle(int n){
    if (n==0){
        return 1;
    }else{
        return n*factorielle(n-1);
    }
}
//fonction pour calculer le dl de cosx
double cos(double x, int n){
    double result1= 1;
    double puissance= x*x;
    int signe= -1;
    for(int i=1; i<=n; i++ ){
        result1= signe*puissance/factorielle(2*i);
        signe =-1;
        puissance *= x*x;
    }
    return result1;
}
//fonction pour calculer le dl de sinx
double sin( double x, int n){
    double result2= 0;
    double puissance = x;
    int signe= 1;
    for(int i=1; i<=n; i++){
        result2=signe*puissance/factorielle(i);
        signe= -1;
        puissance *= x*x;
    }
    return result2;
}
int main(){ 
    double x;
    int n;
    std::cout<<"Entrez la valeur de l'angle:";
    std::cin>>x;
    //conversion en radian
    x=x*0.01745;
    std::cout<<"Entrez l ordre du developpement limite:";
    std::cin>>n;
    double result1= cos(x,n);
    double result2=sin(x,n);
    double result3=cos(x,n)/sin(x,n);
    std::cout<<"cos("<<x<<") ="<<result1;
    std::cout<<"sin("<<x<<")="<<result2;
    std::cout<<"tan("<<x<<")="<<result3;
    return 0;
}
