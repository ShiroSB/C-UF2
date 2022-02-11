def inp_num():
    
    x = int(input("Introduce el tamaño del array entre 1 y 50 : "))
        
    while x < 0 or x > 50:
            
        x = int(input("Introduce el tamaño del array entre 1 y 50 : "))
    
    return x
    
def inp_num2():
    
    x = int(input("Introduce un numero : "))
        
    while x < 1 or x > 10:
            
        x = int(input("Introduce un numero : "))
        
    return x
   
def rellenar_array(x):
    
    array = []
    
    for i in range(x):
        
        valor = inp_num2()
        
        array.append(valor)
        
    return array
    
def array_print(array):
    
        print(array)
        
def mitjana_array(array,x):
    
    suma = 0
    
    mitjana = 0
    
    for i in range(x):
        
        suma = suma + array[i]
        
    mitjana = suma / x
    
    return mitjana
    
def valor_maximo(array,x):
    
    maximo = 0
    
    for i in range(x):
        
        if maximo < array[i]:
            
            maximo = array[i]
            
    return maximo
    
def valor_minimo(array,x):
    
    minimo = 10
    
    for i in range(x):
        
        if minimo > array[i]:
            
            minimo = array[i]
            
    return minimo

def ordenar_array(array,x):

    aux = 0

    for i in range(x):
            
        for j in range(x):
                
            if array[i] < array[j]:
                
                aux = array[i]
                
                array[i] = array[j]
                
                array[j] = aux
        
    return(array)
    
        
