import functions

def main():
    
    
    array = functions.rellenar_array()
    
    mit_ap,aprovats= functions.mitjana_aprovats(array)
    
    mit_sus,suspensos= functions.mitjana_suspensos(array)
    
    print("Media aprobados : ","[",mit_ap,"]")
    
    print("Aprobados totales : ","[",aprovats,"]")
    
    print("Media suspensos : ","[",mit_sus,"]")
    
    print("suspensos totales : ","[",suspensos,"]")
    
    
if __name__ == '__main__':
    main()
