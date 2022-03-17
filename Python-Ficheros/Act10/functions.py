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
        cantante = input(fr.FRASE2)
        cancion = input(fr.FRASE3)
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
        visualizaciones = int(input(fr.FRASE5))
        dbfunctions.create_table()
        dbfunctions.insert_data(identificador, cantante, cancion, fecha, visualizaciones)

        musica = {
            "identificador":identificador,
            "cantante":cantante,
            "cancion":cancion,
            "fecha":fecha,
            "visualizaciones":visualizaciones
        }
        write_CSV(musica)
        print_panda([musica])

def print_panda(musica):
    panda = pd.DataFrame(musica)
    print(panda)

def read_CSV():
    with open('music.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)

def write_CSV(std):
    with open('music.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['identificador', 'cantante', 'cancion', 'fecha', 'visualizaciones']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writerow(std)

def write_header():
    with open('music.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['identificador', 'cantante', 'cancions', 'fecha', 'visualizaciones']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        write_csv.writeheader()
