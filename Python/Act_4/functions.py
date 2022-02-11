def inp_num():
    
    x = int(input("Introduce un numero : "))
        
    while x < 1 or x > 10:
            
        x = int(input("Introduce un numero : "))
        
    return x
    
def rellenar_array():
    
    array = []
    
    for i in range(15):
        
        valor = inp_num()
        
        array.append(valor)
        
    return array
    
def mitjana_aprovats(array):
    
    aprobado = 0
    
    suma = 0
    
    mitjana = 0
    
    for i in range(15):
        
        if array[i] >= 5:
            
            suma = suma + array[i]
            
            aprobado = aprobado + 1
            
    mitjana = suma / aprobado
            
    return mitjana,aprobado
    
def mitjana_suspensos(array):
    
    suspensos = 0
    
    suma = 0
    
    mitjana = 0
    
    for i in range(15):
        
        if array[i] < 5:
            
            suma = suma + array[i]
            
            suspensos = suspensos + 1
            
    mitjana = suma / suspensos
            
    return mitjana,suspensos
