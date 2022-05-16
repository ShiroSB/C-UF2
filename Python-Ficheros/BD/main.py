import functions
import frases as fr
def main():

    functions.factura_total()
    print("1)Ingresar dato y cargarlos a BD")
    print("2)Mostrar datos tabulados")
    print("3)Mostrar total de datos csv")
    i = int(input("Introduce una opción: "))

    if i == 1:
        x = int(input(fr.FRASE6))
        functions.pedir_datos(x)
    if i == 2:
        functions.print_panda()
    if i == 3:
        functions.count_lines()


if __name__ == "__main__":
    main()

