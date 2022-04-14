import random
from colorama import Fore, Style

'''
SUDOKU LOGIC, Euan Campbell, 27/03/2022

Contains functions for use in SudokuGame.py

Board = 9x9 integer matrix used to represent game board
Row = Y axis of Board
Col = X axis of Board
Sqr = Single cell within Board
'''


# Returns a 9x9 int matrix randomly populated with a single instance of numbers 1..9
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

    board = [r1, r2, r3, r4, r5, r6, r7, r8, r9]  # 9x9 grid that represents a board

    # Adding numbers 1..9 to board at random sqrs
    for num in range(9):
        board[random.randrange(9)][random.randrange(9)] = num

    return board


# Returns list of locations of all sqrs holding a non 0 num
def find_filled(board):
    filled = []
    r_index = 0
    c_index = 0

    for row in board:
        for sqr in row:
            if sqr != 0:
                filled.append([r_index, c_index])
            c_index += 1
        c_index = 0
        r_index += 1
        if r_index > 8:
            break
    return filled


# Iterates through all sqrs in board and returns the first empty sqr's location
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


# Iterates through all sqrs in board and adds a valid number to every empty square, creating a complete board
def fill_board(board):
    # identifies a empty sqr, if no empty sqr is found
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Adds valid number to all sqrs
    for num in range(1, 10):

        if validate(board, row, col, num):
            board[row][col] = num

            if fill_board(board):
                return True

            board[row][col] = 0

    return False


# Outputs the board to the console in a colour-coded grid format
# Requires a list of pre-set sqrs (squares that can not be changed by the player)
def draw_board(board, pre_set_sqrs):
    yaxis = ["J", "K", "L", "M", "N", "O", "P", "Q", "R"]

    print("\n")
    print(Fore.YELLOW + "  A B C    D E F    G H I" + Style.RESET_ALL)

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("  - - - - - - - - - - - - ")

        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 0:
                print(Fore.YELLOW + yaxis[i] + " ", end="" + Style.RESET_ALL)

            for sqr in pre_set_sqrs:
                if sqr[0] == i and sqr[1] == j:
                    print(Fore.CYAN, end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

            print(Style.RESET_ALL, end="")


# Returns True if num in position (row, col) in board is a valid sodoku placement, False if it is not
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

        if i // 3 == row // 3:
            ji = 0
            for j in board[i]:
                if ji // 3 == col // 3 and j == num:
                    valid = False
                ji += 1

    return valid


# Takes a completed suduko board and sets num quantity of squares to 0, returns board
def set_board(board, num):
    for c in range(81 - num):

        while True:
            sqr = [random.randrange(9), random.randrange(9)]

            if board[sqr[0]][sqr[1]] != 0:
                break

        board[sqr[0]][sqr[1]] = 0

    return board


# Adds a valid player input to board
def player_move(board, pre_set_sqrs):
    col_chars = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    row_chars = {"J": 0, "K": 1, "L": 2, "M": 3, "N": 4, "O": 5, "P": 6, "Q": 7, "R": 8}

    # Accept player input
    print("Input :")
    move = input()

    # End game on player input "STOP"
    if move == "STOP":
        return False

    # Check for valid input
    move = (move.split(" "))
    if len(move) == 3 and move[0] in col_chars and move[1] in row_chars:

        # Check input for num
        try:
            x = int(move[2])
        except ValueError:
            print(Fore.RED + "INVALID NUMBER INPUT! TRY AGAIN" + Style.RESET_ALL)
            return board

        # Check num is in range 1..9
        if int(move[2]) in range(0, 10):

            row = int(row_chars[move[1]])
            col = int(col_chars[move[0]])

            # Check input coordinates are not pre set squares
            for sqr in pre_set_sqrs:
                if int(sqr[0]) == row and int(sqr[1]) == col:
                    print(Fore.RED + "INVALID BOARD LOCATION! TRY AGAIN" + Style.RESET_ALL)
                    return board

            # if input is valid add input to board
            board[row][col] = int(move[2])
            return board

        else:
            print(Fore.RED + "INVALID NUMBER INPUT! TRY AGAIN" + Style.RESET_ALL)
            return board

    else:
        print(Fore.RED + "INVALID COORDINATE INPUT! TRY AGAIN" + Style.RESET_ALL)
        return board


# Checks sum of all rows cols and boxes == 45, is so the board is solved and returns true
def check_for_win(board):

    row_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    col_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    box_totals = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Sum all rows and cols
    row_index = 0
    for row in board:
        col_index = 0
        for sqr in row:
            row_totals[row_index] += sqr
            col_totals[col_index] += sqr
            col_index += 1
        row_index += 1

    # Sum all boxes
    row_index = 0
    for row in board:
        col_index = 0
        for sqr in row:
            box_totals[row_index//3][col_index//3] += sqr
            col_index += 1
        row_index += 1

    # Check sum of all rows and cols == 45
    for t1 in row_totals:
        if t1 == 45:
            for t2 in col_totals:
                if t2 == 45:
                    continue
                else:
                    return False
        else:
            return False

    # Check sum of all boxes == 45
    for b_row in box_totals:
        for b in b_row:
            if b == 45:
                continue
            else:
                return False

    return True


# Take player difficulty input and return corresponding int value
def select_difficulty():
    while True:

        print("SELECT DIFFICULTY (E/M/H) :")
        difficulty = input()

        if difficulty == "E" or difficulty == "M" or difficulty == "H":

            if difficulty == "E":
                difficulty = 40
            else:
                if difficulty == "M":
                    difficulty = 30
                else:
                    difficulty = 20

            return difficulty

        else:
            print("INVALID INPUT! TRY AGAIN")
            continue

