from io import SEEK_END


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

def isValid(board):
    # Look in same 3x3 grid
    mini_grids = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
    for grid in mini_grids:
        seen_before = []
        for i in range(3):
            for j in range(3):
                sq = board[grid[0] + i][grid[1]+j]
                if sq in seen_before:
                    return False
                if sq != 0:
                    seen_before.append(sq)
            
    # Look in row and column
    for row in range(len(board)):
        seen_before_row = []
        seen_before_col = []
        for col in range(len(board)):
            sq1 = board[row][col]
            sq2 = board[col][row]
            if sq1 in seen_before_row or sq2 in seen_before_col:
                return False
            if sq1 != 0:
                seen_before_row.append(sq1)
            if sq2 != 0:
                seen_before_col.append(sq2)

    return True

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


def solve(board):
    isval = isValid(board)
    
    if isval:
        emptySq = findEmpty(board)
        if not emptySq:
            return True
        
        else:
            empY, empX = emptySq

        for i in range(1, 10):
            if isPossible(board, i, emptySq):
                board[empY][empX] = i

                if solve(board):
                    return True

                board[empY][empX] = 0

    else:
        return False
