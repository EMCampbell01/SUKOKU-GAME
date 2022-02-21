import random


def create_random_board():

    r1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    r9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    board = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

    for num in range(9):
        board[random.randrange(9)][random.randrange(9)] = num

    return board


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def fill_board(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        #print(find)

    for num in range(1, 10):

        #draw_board(board)

        if validate(board, row, col, num):
            board[row][col] = num

            if fill_board(board):
                return True

            board[row][col] = 0

    return False


def draw_board(board):
    print("A B C    D E F    G H I")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def validate(board, row, col, num):

    # Check row & col
    valid = True
    for x in range(9):
        if board[x][col] == num:
            valid = False
        for y in range(9):
            if board[row][y] == num:
                valid = False

    # Check box
    for i in range(9):
        if i//3 == row//3:
            ji = 0
            for j in board[i]:
                if ji//3 == col//3 and j == num:
                    valid = False
                ji += 1

    return valid


def set_board(board, num):

    for c in range(81 - num):

        while True:
            sqr = [random.randrange(9), random.randrange(9)]

            if board[sqr[0]][sqr[1]] != 0:
                break

        board[sqr[0]][sqr[1]] = 0

    return board
