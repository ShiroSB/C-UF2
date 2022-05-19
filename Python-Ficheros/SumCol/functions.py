import csv

def print_datos():
    with open('consumo_energia.csv') as projects_board:
        readCSV = csv.reader(projects_board,delimiter = ',')
        for row in readCSV:
            print(row[5],row[6])


def consumo_total():
    with open('consumo_energia.csv') as projects_board:
        readCSV = csv.reader(projects_board,delimiter = ',')
        count = 0
        x = 0
        y = 0
        consumo = 0
        for row in readCSV:
            count = count + 1
            if count >= 2:
                if row[7] == '':
                    row[7] = '0'
                x = int(row[5])
                y = int(row[7])
                if x == 3:
                    consumo = int(consumo) + y
        print("Consumo total del sector 3  : " + str(consumo))
