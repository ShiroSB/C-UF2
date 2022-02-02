#include <stdio.h>
#include "functions.h"

int VLT(){
    
    int x;
    
    do{
    
    printf("Tamaño vector : ");
    scanf("%d",&x);

    }while(x < 0 || x > 50);
    
    return x;
        
}
