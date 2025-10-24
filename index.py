# Crossword Generator and Solver using Backtracking
# Mini Project

N = 10  # Grid size (10x10 crossword)

def canPlaceHorizontally(board, word, row, col):
    if col + len(word) > N:
        return False
    for i in range(len(word)):
        if board[row][col + i] not in ['-', word[i]]:
            return False
    return True


def placeHorizontally(board, word, row, col):
    placed = []
    for i in range(len(word)):
        if board[row][col + i] == '-':
            board[row][col + i] = word[i]
            placed.append((row, col + i))
    return placed

def canPlaceVertically(board, word, row, col):
    if row + len(word) > N:
        return False
    for i in range(len(word)):
        if board[row + i][col] not in ['-', word[i]]:
            return False
    return True


def placeVertically(board, word, row, col):
    placed = []
    for i in range(len(word)):
        if board[row + i][col] == '-':
            board[row + i][col] = word[i]
            placed.append((row + i, col))
    return placed

def removeWord(board, placed):
    for (r, c) in placed:
        board[r][c] = '-'

# Backtracking 
def solveCrossword(board, words, index):
    if index == len(words):
        return True  

    word = words[index]

    for row in range(N):
        for col in range(N):
            if canPlaceHorizontally(board, word, row, col):
                placed = placeHorizontally(board, word, row, col)
                if solveCrossword(board, words, index + 1):
                    return True
                removeWord(board, placed)

            if canPlaceVertically(board, word, row, col):
                placed = placeVertically(board, word, row, col)
                if solveCrossword(board, words, index + 1):
                    return True
                removeWord(board, placed)

    return False

def printBoard(board):
    for row in board:
        print(' '.join(row))
    print()

if __name__ == "__main__":
    board = [['-' for _ in range(N)] for _ in range(N)]
    words = ["HELLO", "WORLD", "PYTHON", "DATA", "CODE","TRY","OCEAN",]

    if solveCrossword(board, words, 0):
        print("Crossword Generated Successfully!\n")
        printBoard(board)
    else:
        print("Cannot generate crossword with given words")
        
