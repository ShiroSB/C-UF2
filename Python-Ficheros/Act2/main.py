#Implementa un programa que demani un text a l’usuari i 
#l’afegeixi al fitxer creat en l’activitat anterior.

import functions

def main():
    
    ruta = functions.def_ruta()
    
    functions.write_file(ruta)
    
    functions.read_file(ruta)
    
if __name__ == '__main__':
    
    main()
