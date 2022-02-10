import random

import functions

def main():
    
    x = functions.pedir_numero()
    
    numero_aleatorio = [random.randint(15,200) for i in range(x)]
    
    n1 = functions.pedir_numero2()
    
    if n1 in numero_aleatorio:
        
        print("Esta en la lista")
        
    else:
        
        print("No esta")

    
if __name__ == '__main__':
    
    main()
