def inp_num():
    
    x = int(input("Introduce un numero : "))
        
    while x < 0:
            
        x = int(input("Introduce un numero : "))
    
    return x
   
def secuencia(x):
    
    suma = 0
    
    for i in range(x):
        
        if suma < x:
            
            suma = suma + i
            
            aux = i
            
            if suma <= x and suma != 0:
                
                print("[",i,"]" ,end="")
    
    if suma > x:
        
        suma = suma - aux
        
    print()
     
    return suma
