import csv
import  pandas as pd
import frases as fr
import dbfunctions

def pedir_datos(x):

    write_header()
    for i in range(x):
        identificador = int(input(fr.FRASE1))
        while identificador <= 0:
            identificador = int(input(fr.FRASE1))
        nombre = input(fr.FRASE2)
        autor = input(fr.FRASE3)
        dia = int(input(fr.DIA))
        while dia < 0 or dia > 31:
            dia = int(input(fr.DIA))
        mes = int(input(fr.MES))
        while mes < 1 or mes > 12:
            mes = int(input(fr.MES))
        año = int(input(fr.YEAR))
        while año < 1900 or año > 2022:
            año = int(input(fr.YEAR))
        fecha = str(dia) + "/" + str(mes) + "/" + str(año)
        idioma = input(fr.FRASE5)
        dbfunctions.create_table()
        dbfunctions.insert_data(identificador, nombre, autor, fecha, idioma)

        libros = {
            "identificador":identificador,
            "nombre":nombre,
            "autor":autor,
            "fecha":fecha,
            "idioma":idioma
        }
        write_CSV(libros)

def count_lines():

    with open('libros.csv') as projects_board:
        total_lines = sum(1 for line in projects_board)
        total_lines = total_lines - 1
        print(fr.FRASE7 + str(total_lines))

def factura_total():
    with open('libros.csv') as projects_board:
        readCSV = csv.reader(projects_board, delimiter=',')
        x = 0
        count = 0
        for row in readCSV:
                count = count + 1
                if count >= 2:
                    x = x + int(row[0])
        print(x)

def print_panda():
    df = pd.read_csv("libros.csv")
    print(df)

def read_CSV():
    with open('libros.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)

def write_CSV(std):
    with open('libros.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['identificador', 'nombre', 'autor', 'fecha', 'idioma']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writerow(std)

def write_header():

    with open('libros.csv') as projects_board:
        total_lines = sum(1 for line in projects_board)
        total_lines = total_lines - 1


    if total_lines == 0:
        with open('libros.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = [ 'Identificador','Nombre del libro', 'Autor', 'Fecha', 'Idioma']
            write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            write_csv.writeheader()
