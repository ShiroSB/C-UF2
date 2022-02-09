def vlt_num():

    i = 0
    x = 0
    
    while x < 10 or x > 5000 and i != 3:
            
        x = int(input("Introduce un numero : "))
        
        i = i + 1
    
    return x
