import csv

def main():

    with open('consumo_energia.csv') as projects_board:
        readCSV = csv.reader(projects_board,delimiter = ',')
        count = 0
        x = 0
        C_3_TOTAL = 0
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
                    C_3_TOTAL = C_3_TOTAL + 1
                    consumo = int(consumo) + y
        print(C_3_TOTAL)
        print(consumo)



if __name__ == "__main__":
    main()
