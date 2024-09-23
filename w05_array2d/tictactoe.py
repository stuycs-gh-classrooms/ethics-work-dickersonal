board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

def drawBoard():
    print("\n")
    for i in range(len(board)):
        print("|".join(board[i]))
        if i < len(board)-1:
            print("-----")

def findWinner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[0][2] == board[1][1] == board[2][0] != " "):
        return board[1][1]
    return None

def isDraw():
    for row in board:
        for cell in row:
            if cell == " " :
                return False
    return True

def runGame():
    currentPlayer = "X"
    while True:
        drawBoard()
        print("It's "+currentPlayer+"'s turn.")
        try:
            row = int(input("Select a row, (0, 1, 2): "))
            col = int(input("Select a column, (0, 1, 2): "))
        except ValueError:
            print("Input must be an integer: 0, 1, or 2")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Input is outside the board. Please try again.")
        elif not (board[row][col] == " "):
            print("This spot is already filled with an "+ board[row][col])
        else:
            board[row][col] = currentPlayer
            
            winner = findWinner()
            if winner:
                drawBoard()
                print(winner+" wins!")
                break

            if isDraw():
                drawBoard()
                print("It's a draw!")
                break
            
            if currentPlayer == 'X':
                currentPlayer = 'O'
            elif currentPlayer == 'O':
                currentPlayer = 'X'

runGame()
