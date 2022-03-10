def read_file():

    file = open('projects_board.csv', 'r')
    print(file.read())
    file.close()

def count_lines():

    with open('projects_board.csv') as projects_board:
        total_lines = sum(1 for line in projects_board)
        print(total_lines)
