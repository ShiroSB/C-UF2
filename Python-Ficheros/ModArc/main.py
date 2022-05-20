import functions

def main():
    opciones = functions.opciones()

    if (opciones == 1):

        opcion = functions.opcion1()

    if (opciones == 2):

        opcion = functions.opcion2()

    if (opciones == 3):

        opcion = functions.opcion3()

    if (opciones == 4):

        print("Has decidido salir")


if __name__ == '__main__':
    main()
