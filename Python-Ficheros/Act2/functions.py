TEXTO1 = 'Introduce el texto:  '

TEXTO2 = 'text.txt'

def read_file(fname):
    
    file = open(fname,'r')
    
    print(file.read())
    
    file.close()
    
def write_file(fname):
    
    frase = input(TEXTO1)
    
    file = open(fname,'a')
    
    file.write(frase)
    
    file.close()
    
def def_ruta():
    
    x = TEXTO2
    
    return x
