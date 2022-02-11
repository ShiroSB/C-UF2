import functions

def main():
    
    x = functions.inp_num()
    
    array = functions.rellenar_array(x)
    
    res = functions.array_print(array)
    
    mitjana = functions.mitjana_array(array,x)
    
    val_max = functions.valor_maximo(array,x)
    
    val_min = functions.valor_minimo(array,x)
    
    array_ordenado = functions.ordenar_array(array,x)
    
    print("Media : ",mitjana)
    
    print("Valor maximo : ",val_max)
    
    print("Valor minimo : ",val_min)
    
    print("Valores ordenados : ","[",array,"]")
    
if __name__ == '__main__':
    main()
