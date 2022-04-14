import SudokuLogic

'''
SUDOKUGAME Euan Campbell 27/03/2022
This is the main file for SUDOKUGAME.py
functions from SUDOKULOGIC.py are used to create a sudoku console game.
'''

print("╭━━━╮╭╮ ╭╮╭━━━╮╭━━━╮╭╮╭━╮╭╮ ╭╮")
print("┃╭━╮┃┃┃ ┃┃╰╮╭╮┃┃╭━╮┃┃┃┃╭╯┃┃ ┃┃")
print("┃╰━━╮┃┃ ┃┃ ┃┃┃┃┃┃ ┃┃┃╰╯╯ ┃┃ ┃┃")
print("╰━━╮┃┃┃ ┃┃ ┃┃┃┃┃┃ ┃┃┃╭╮┃ ┃┃ ┃┃")
print("┃╰━╯┃┃╰━╯┃╭╯╰╯┃┃╰━╯┃┃┃┃╰╮┃╰━╯┃")
print("╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰╯╰━╯╰━━━╯")
print("BY EUAN CAMPBELL\n")

# Gameplay running loop
while True:

    # User selects difficulty
    difficulty = SudokuLogic.select_difficulty()

    # Creates new random board
    print("Creating Game...")
    board = SudokuLogic.create_random_board()
    SudokuLogic.fill_board(board)
    SudokuLogic.set_board(board, difficulty)
    print("Game Created!\n")

    print('INPUT MOVES AS THE FOLLOWING: "COL ROW NUM"')
    print('INPUT "STOP" TO END GAME\n')

    pre_set_sqrs = SudokuLogic.find_filled(board)  # list of unchangeable pre-set squares, output in blue

    # player inputs moves until the game is finished
    game_running = True
    while game_running:
        SudokuLogic.draw_board(board, pre_set_sqrs)
        if not SudokuLogic.player_move(board, pre_set_sqrs):
            break
        if SudokuLogic.check_for_win(board):
            game_running = False
            print("Puzzle Solved!")
            break

    # Option to play again
    print("\nWould you like to play again? (Y/N) : ")
    if input().capitalize() == "Y":
        continue
    else:
        break
