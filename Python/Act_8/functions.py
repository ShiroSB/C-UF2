def inp_num():
    
    x = int(input("Introduce un numero : "))
        
    while x < 0:
            
        x = int(input("Introduce un numero : "))
    
    return x
   
def elev(x,i):
    
    aux = x
    
    count = 1
    
    if i == 0:
        
        return 1
        
    else:
        
        while count < i:
                
            count = count + 1
                
            x = x * aux
        
    return x
