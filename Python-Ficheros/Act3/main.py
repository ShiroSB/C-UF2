#Implementa un programa que mostri un menú amb les següents opcions:
#crear un fitxer (demanant el nom del fitxer a l’usuari per teclat)
#mostrar el contingut d’un fitxer per pantalla (demanant el nom del fitxer a l’usuari per teclat)
#modificar el contingut d’un fitxer demanant el nom del fitxer a l’usuari per teclat)
#sortir


import functions

def main():
    
    opciones = functions.opciones()
    
    if(opciones == 1):
        
        opcion = functions.opcion1()
        
    elif(opciones == 2):
        
        opcion = functions.opcion2()
    
    elif(opciones == 3):
        
        opcion = functions.opcion3()
        
    elif(opciones == 4):
        
        print("Has decidido salir")
    
if __name__ == '__main__':
    
    main()
