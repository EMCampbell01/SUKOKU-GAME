import Game

print("╭━━━╮╭━━━╮╭━━━╮╭━━━╮╭╮╭━╮╭╮ ╭╮")
print("┃╭━╮┃┃╭━╮┃╰╮╭╮┃┃╭━╮┃┃┃┃╭╯┃┃ ┃┃")
print("┃╰━━╮┃┃ ┃┃ ┃┃┃┃┃┃ ┃┃┃╰╯╯ ┃┃ ┃┃")
print("╰━━╮┃┃┃ ┃┃ ┃┃┃┃┃┃ ┃┃┃╭╮┃ ┃┃ ┃┃")
print("┃╰━╯┃┃╰━╯┃╭╯╰╯┃┃╰━╯┃┃┃┃╰╮┃╰━╯┃")
print("╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰╯╰━╯╰━━━╯")
print("BY EUAN CAMPBELL\n")


selecting_difficulty = True
while selecting_difficulty:

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

        selecting_difficulty = False

    else:
        print("INVALID INPUT! TRY AGAIN")
        continue

print("Creating Game...")

board = Game.create_random_board()
Game.fill_board(board)
Game.set_board(board, difficulty)

Game.draw_board(board)
