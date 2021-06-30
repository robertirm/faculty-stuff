#include <stdio.h>
#include <string.h>

int convertire(int n ,char sir[100]);

int main()
{
    //11. Se citeste de la tastatura un sir de mai multe numere in baza 2. 
    //Sa se afiseze aceste numere in baza 16.
    
    char sir[100];
    int n;
    printf("Sirul de numere in baza 2 : \n");
    fgets(sir, 100, stdin);
    sir[strlen(sir)-1] = 0;

    char *p;
    p = strtok(sir," ");
    while(p != NULL)
    {
        n = strlen(p);
        strrev(p);
        printf("%x ", convertire(n,p));
        p = strtok(NULL, " ");
    }

    return 0;
}
