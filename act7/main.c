#include <stdio.h>
#include "functions.h"

int VLT(){
    
    int i = 0;
    
    int arr[i];
    
    do{
    
    printf("Introduce los datos : ");
        
    scanf("%d",&arr[i]);

    }while(arr[i] < 0 || arr[i] > 10);
    
    return arr[i];
        
}

int VLTTMN(){
    
    int x;
    
    do{
    
    printf("Tamaño del array : ");
    
    scanf("%d",&x);
    
    }while(x < 1 || x > 50);
    
    return x;
}
