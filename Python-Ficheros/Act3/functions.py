TEXTO1 = 'Introduce el texto:  '

TEXTO2 = 'Introduce el nombre de tu archivo: '

TEXTO3 = 'Introduce la extension: '

OPCION1 = '1)Crear fichero'

OPCION2 = '2)Mostrar contenido de un fichero'

OPCION3 = '3)Modificar contenido de un fichero'

OPCION4 = '4)Salir'

def read_file(ruta):
    
    file = open(ruta,'r')
    
    print(file.read())
    
    file.close()
    
def write_file(ruta):
    
    frase = input(TEXTO1)
    
    file = open(ruta,'a')
    
    file.write(frase)
    
    file.close()
    
def replace_file(ruta):
    
    frase = input(TEXTO1)
    
    file = open(ruta,'w')
    
    file.write(frase)
    
    file.close
    
def def_ruta():
    
    x = input(TEXTO2)
    
    return x
    
def def_ext():
    
    x = input(TEXTO3)
    
    return x
    
def opciones():

    print(OPCION1)
    
    print(OPCION2)
    
    print(OPCION3)
    
    print(OPCION4)
    
    x = int(input("Introduce una opcion: "))
    
    return x
    
def opcion1():
    
    ruta = def_ruta()
        
    ext = def_ext()
        
    ruta = ruta + '.' + ext
        
    write_file(ruta)
    
def opcion2():
    
    ruta = def_ruta()
        
    ext = def_ext()
        
    ruta = ruta + '.' + ext
        
    read_file(ruta)
    
def opcion3():
            
    ruta = def_ruta()
        
    ext = def_ext()
        
    ruta = ruta + '.' + ext
        
    replace_file(ruta)
