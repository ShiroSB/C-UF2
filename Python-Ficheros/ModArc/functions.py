TEXTO1 = 'Introduce el texto:  '

TEXTO2 = 'Introduce el nombre de tu archivo: '

TEXTO3 = 'Introduce la extension: '

OPCION1 = '1)Crear fichero'

OPCION2 = '2)Mostrar contenido de un fichero'

OPCION3 = '3)Modificar contenido de un fichero'

OPCION4 = '4)Salir'

def read_file(ruta):
    file = open('files/' + ruta, 'r')

    print(file.read())

    file.close()

def write_file(ruta):
    frase = input(TEXTO1)

    file = open('files/' + ruta, 'a')

    file.write(frase)

    print("Has introducido 1 registro")

    file.close()

def replace_file(ruta):

    x = int(input("Cuantos registros quieres introducir?"))

    for i in range(x):

        frase = input(TEXTO1)

        file = open('files/' + ruta, 'a+')

        file.write("\n" + frase)

    print("Has introducido " + str(x) + " registros")

    file.close

def def_ruta():
    x = input(TEXTO2)

    return x


def def_ext():
    x = input(TEXTO3)

    if x != 'txt':
        while x != 'txt':
            print('No es punto txt!')
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
