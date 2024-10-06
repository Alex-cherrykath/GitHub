#include <stdio.h>
#include <math.h>
int main() {
    float cote1, cote2, cote3;
    int typtriangle;
    int reponse;
    printf("Entrez la longueur du premier cote:");
    scanf("%f", &cote1);
    printf("Entrez la longueur du deuxieme cote:");
    scanf("%f", &cote2);
    printf("Entrez la nature du triangle, 1,2,3 respectivement pour equilatera,isocele,rectangle:");
    scanf("%d", &typtriangle);
    switch(typtriangle) {
        case 1:
            cote3=cote1;
            break;
        case 2:
            printf("Indiquez si le troisieme cote est egale au premier (1) ou non (0):");
            scanf("%d", &reponse);
            if(reponse==0){
                cote3=cote1;
            } else{
                cote3=cote2;
            }
            break;
        case 3:
            //supposons que cote1 et cote2 sont les deux cotes formant l'angle droit
            cote3= sqrt(cote1*cote1 + cote2*cote2);
            break;
        default:
        printf("Type de triangle invalide");
    }
    printf("Le troisieme cote mesure:%f\n",cote3);
    return 0;
}	
