#include <stdio.h>
#include "functions.h"

int main()
{
    
int i,x,aux,j;


    x = VLT();
    
    int vector[x];
    
    for(i = 0 ; i < x ; i++){
        
        printf("Introduce el valor : ");
        scanf("%d",&vector[i]);
        
    }
    
    printf("Desordenados : ");
    
    for(i = 0 ; i < x ; i++){
        
        printf("[%d]",vector[i]);
        
    }
    
    
    for(i = 0 ; i < x -1 ; i++){
        
        for( j = i + 1 ; j < x ; j++){
            
            if(vector[i] < vector[j]){
                
                aux = vector[i];
                
                vector[i] = vector[j];
                
                vector[j] = aux;
                
            }
            
        }
        
    }
    
    printf("\n");
    
    printf("Ordenados : ");
    
    for( i = 0 ; i < x ; i++){
        
        printf("[%d]",vector[i]);
        
    }
    
}
