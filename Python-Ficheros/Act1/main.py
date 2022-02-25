#Implementa un programa que demani un text a l’usuari i el guardi
#en un fitxer anomenat “text.txt”.

import functions

def main():
    
    ruta = functions.def_ruta()
    
    functions.write_file(ruta)
    
    functions.read_file(ruta)
    
if __name__ == '__main__':
    
    main()
