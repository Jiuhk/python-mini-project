import random

playerNum = 1
size = 3  # Board size, different gameplay should be ok
chess1 = 'X'
chess2 = 'O'
play = 1


def engChess(chess):
    if chess == -1:
        return " "
    elif chess == 1:
        return chess1
    elif chess == 0:
        return chess2
    else:
        return chess


def printBoard(board):
    pos = 0
    for line in range(0, 2 * size + 1):
        if line == 0 or line == 2 * size:
            for i in range(0, 2 * size + 1):
                print("-", end="")
            print("")
        elif line % 2 == 0:
            for i in range(0, size):
                print("|-", end="")
            print("|")
        else:
            for i in range(0, size):
                if type(board[pos]) == type(1):
                    print("|", engChess(board[pos]), sep="", end="")
                else:
                    print("|", board[pos], sep="", end="")

                pos += 1
            print("|")


# Gamemode setting
error = 1
while error == 1:
    playerNum = int(input("Player number (1 for PVC, 2 for PVP): "))
    if playerNum == 1 or playerNum == 2:
        error = 0
    else:
        print("Wrong input!")

# Introduction to the game
introBoard = []
for i in range(1, size * size + 1):
    introBoard.append(str(i))
printBoard(introBoard)
print("Introduction")
print("")

while play:
    # Initialization
    chessboard = []
    freeSlot = []
    playerTurn = 0
    win = 0
    for i in range(0, size * size):
        chessboard.append(-1)
        freeSlot.append(i)

    # Gameplay
    while win == 0 and len(freeSlot) > 0:
        playerTurn += 1
        printBoard(chessboard)
        print("Player ", playerTurn)
        playerTurn %= 2

        if playerNum == 2 or playerTurn % 2 == 1:  # Player's turn
            error = 1
            while error == 1:
                move = int(input("Your move (1-" + str(size * size) + "): ")) - 1
                if move < 0 or move > size * size - 1:
                    print("Wrong input!")
                elif chessboard[move] != -1:
                    print("Occupied!")
                else:
                    error = 0
        else:  # Computer's turn
            move = random.choice(freeSlot)
        chessboard[move] = playerTurn % 2
        freeSlot.remove(move)

        # Win condition
        same = 1
        for i in range(0, size):

            same = 1  # Horizontal
            for j in range(0, size):
                if chessboard[size * i + j] != playerTurn:
                    same = 0
            if same:
                win = 1

            same = 1  # Vertical
            for j in range(0, size):
                if chessboard[i + size * j] != playerTurn:
                    same = 0
            if same:
                win = 1

        same = 1  # Positive diagonal
        for i in range(0, size):
            if chessboard[0 + i * (size + 1)] != playerTurn:
                same = 0
        if same:
            win = 1

        same = 1  # Negative diagonal
        for i in range(0, size):
            if chessboard[size - 1 + i * (size - 1)] != playerTurn:
                same = 0
        if same:
            win = 1
    printBoard(chessboard)
    if win:
        if playerTurn == 0:
            playerTurn += 2
        print("Player " + str(playerTurn) + " win!")
    else:
        print("Draw!")

    play = int(input("Continue? (1 or 0): "))
