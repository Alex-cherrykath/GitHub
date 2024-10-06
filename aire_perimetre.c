#include<stdio.h>
#include<math.h>
const int PI=3.14;
int main() 
{
	//comme c'est plusieurs formes,on doit stocker le choix de l'user
    int choix;
    float c,l,L,r,b,t,h;
    float perimetre, aire;
    printf("De qu'elle figure veux-tu les parametres?:\n");
    printf("1. Carre\n");
    printf("2. Rectangle\n");
    printf("3. Triangle\n");
    printf("4. Cercle");
    scanf("%d", choix);
    // Utilisons la structure switch pour que le programe execute les calculs exacts en fonction du choix
    switch(choix){
    	if (choix=1){
        case 1:
            printf("Entrez donc la longueur positive du carre");
            scanf("%f",&c);
            	perimetre= c*4;
            	aire= c*c;
            printf("perimetre:", "%f\n", perimetre);
            printf("aire:", "%f\n",aire);
		}
           break;
            // break est fondamentale sinon le code va continuer a s'executer
            if (choix=2){
        case 2:
            printf("Entrez donc la longueur positive du rectangle");
            scanf("%f",&L);
            printf("Entrez donc la largeur positive du rectangle");
            scanf("%f",&l);
            	perimetre= (L+l)*2;
				aire= L*l;
            printf("perimetre:", "%f\n", perimetre);
            printf("aire:", "%f\n", aire);
			}
            break;
            if (choix=3){
        case 3:
            printf("Entrez donc la hauteur positive du triangle");
            scanf("%f",&h);
            printf("Entrez  la base positive du triangle");
            scanf("%f",&b);
            printf("Entrez le troisieme cote positif du triangle");
            scanf("%f",&t);
            	perimetre= b+h+t;
            	aire= (h*b)*0.5;
            printf("perimetre:", "%f\n",perimetre );
            printf("aire:", "%f\n", aire);
			}
            break;
            if (choix=4){
        case 4:
            printf("Entrez donc le rayon du cercle");
            scanf("%f",&r);
            	perimetre= 2*(PI*r);
            	aire= (PI*r*r);
            printf("perimetre:", "%f\n", perimetre);
            printf("aire:", "%f\n",aire);
			}
            break;
            // l'instruction default s'est au cas ou on entre une valeur de choix non defini
        default:
            printf("choix non valide.\n");
    }
    return 0;
    
    
}