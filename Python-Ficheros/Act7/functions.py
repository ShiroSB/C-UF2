TEXTO1 = 'Introduce la fecha: '
TEXTO2 = 'Introduce el nombre: '
TEXTO3 = 'Introduce la localizacion: '
TEXTO4 = 'Introduce la especie: '
TEXTO5 = 'Introduce la medida: '
TEXTO6 = 'Introduce las caracteristicas: '
def read_file():

    file = open('bio.csv', 'r')

    print(file.read())

    file.close()


def write_file():

    frase = input(TEXTO1)
    frase2 = input(TEXTO2)
    frase3 = input(TEXTO3)
    frase4 = input(TEXTO4)
    frase5 = input(TEXTO5)
    frase6 = input(TEXTO6)
    file = open('bio.csv', 'a')

    file.write("\n"+frase+","+frase2+","+frase3+","+frase4+","+frase5+","+frase6)

    file.close()
