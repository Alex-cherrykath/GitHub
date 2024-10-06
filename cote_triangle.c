#include <stdio.h>
#include <math.h>
int main() {
    float cote1, cote2, cote3;
    char typtriangle;
    char reponse;
    printf("Entrez la longueur du premier cote:");
    scanf("%f", &cote1);
    printf("Entrez la longueur du deuxieme cote:");
    scanf("%f", &cote2);
    printf("Entrez la nature du triangle, e,i,r respectivement pour equilatera,isocele,rectangle:");
    scanf("%c", &typtriangle);
    switch(typtriangle) {
        case'e':
            cote3=cote1;
            break;
        case 'i':
            printf("Indiquez si le troisieme cote est egale au premier (o) ou non (n):");
            scanf("%c", &reponse);
            if(reponse=='o'){
                cote3=cote1;
            } else{
                cote3=cote2;
            }
            break;
        case 'r':
            //supposont que cote1 et cote2 sont les deux cotes formant l'angle droit
            cote3= sqrt(cote1*cote1 + cote2*cote2);
            break;
        default:
        printf("Type de triangle invalide");
    }
    printf("Le troisieme cote mesure:%f\n",cote3);
    return 0;
}
