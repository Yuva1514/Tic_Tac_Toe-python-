# Game initializing and Board printing
import random

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Taing player input and handling
def playerInput(board, currentPlayer):
    while True:
        try:
            inp = int(input(f"Enter a number 1-9 for {currentPlayer}: "))
            if inp < 1 or inp > 9 or board[inp - 1] != "-":
                print("Oops! Invalid input or position already taken. Try again!")
            else:
                board[inp - 1] = currentPlayer
                break
        except ValueError:
            print("Oops! Invalid input. Please enter a number.")
    return board

# Check for Win
def checkHorizontal(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            return True
    return False

def checkVertical(board):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            return True
    return False

def checkDiagonal(board):
    if (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]) and board[4] != "-":
        return True
    return False

# Check for Tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        return True
    return False

# Check for Win or Tie
def checkWin(board, currentPlayer):
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {currentPlayer}")
        return True
    return False

# switching Player 

def switchPlayer(currentPlayer):
    return "O" if currentPlayer == "X" else "X"

# Computer's move
def computerMove(board, computerPlayer):
    while True:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = computerPlayer
            break
    return board

# Main game loop (play game)
def playGame(playerChoice):
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    
    currentPlayer = "X"
    computerPlayer = "O"
    if playerChoice == "O":
        currentPlayer = "O"
        computerPlayer = "X"
    
    gameRunning = True

    while gameRunning:
        printBoard(board)
        if currentPlayer == playerChoice:
            board = playerInput(board, currentPlayer)
        else:
            board = computerMove(board, computerPlayer)
        if checkWin(board, currentPlayer) or checkTie(board):
            gameRunning = False
        currentPlayer = switchPlayer(currentPlayer)

# main function 
def main():
    while True:
        playerChoice = input("Choose to play as X or O: ").upper()
        while playerChoice not in ["X", "O"]:
            playerChoice = input("Invalid choice. Choose only between X and O: ").upper()
        playGame(playerChoice)
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain != "yes":
            break

if __name__ == "__main__":
    main()
