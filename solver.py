def printBoard(board):
    for i in range(len(board)):
        print('[', end='')
        for j in range(len(board[i])):
            print(f' {board[i][j]}', end=' ')
            if (j+1) % 3 == 0:
                print(']', end='')
                if j < len(board[i]) - 1:
                    print('[', end='')
            elif j < len(board[i])-1:
                print('|', end='')

        print('')
        if (i+1) % 3 == 0:
            print('='*39)
        else:
            print('-'*39)


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return False


def getMiniGrid(board, square):  # Returns top left most square of the grid
    y, x = square
    return y//3 * 3, x//3 * 3


def isPossible(board, val, square):
    y, x = square

    # Look for repeat numbers in same column
    for row in range(len(board)):
        if board[row][x] == val:
            return False

    # Look for repeat numbers in same row
    for col in range(len(board)):
        if board[y][col] == val:
            return False

    # Look in same 3x3 grid
    gridY, gridX = getMiniGrid(board, square)
    for row in range(gridY, gridY+3):
        for col in range(gridX, gridX+3):
            if board[row][col] == val:
                return False

    return True


def solve(board, recurIter=0):
    emptySq = findEmpty(board)
    if not emptySq:
        return True
    else:
        empY, empX = emptySq

    for i in range(1, 10):
        if isPossible(board, i, emptySq):
            board[empY][empX] = i

            if solve(board, recurIter+1):
                return True

            board[empY][empX] = 0

    return False


board = [[1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

solve(board)
