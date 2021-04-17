def show_GameBoard(matrix):
    for row in matrix:
        print(row)


def number_of_collisions(matrix, row, column):
    collisions = 0
    for i in range(0, len(matrix)):
        if matrix[row][i] == 1:
            collisions += 1
        if matrix[i][column] == 1:
            collisions += 1

    for i, j in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    for i, j in zip(range(row, len(matrix), 1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    return collisions


def number_of_collisions_full(matrix, row, column):
    collisions = 0
    for i in range(0, len(matrix)):
        if matrix[row][i] == 1:
            collisions += 1
        if matrix[i][column] == 1:
            collisions += 1

    for i, j in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    for i, j in zip(range(row, len(matrix), 1),
                    range(column, -1, -1)):
        if matrix[i][j] == 1:
            collisions += 1

    for i, j in zip(range(row, -1, 1),
                    range(column, -1, 1)):
        if matrix[i][j] == 1:
            collisions += 1

    for i, j in zip(range(row, len(matrix), -1),
                    range(column, -1, 1)):
        if matrix[i][j] == 1:
            collisions += 1

    return collisions


def numberOfFreePositions(board, column):
    free_pos = 0
    for i in range(0, len(board)):
        if number_of_collisions(board, i, column) == 0:
            free_pos += 1
    return free_pos


def colMinFree(board, list_of_cols):
    min_free = len(board)
    min_free_col = None
    for item in list_of_cols:
        free_pos = numberOfFreePositions(board, item)
        if free_pos <= min_free:
            min_free = free_pos
            min_free_col = item
    return min_free_col, min_free


def backtrackSolver(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if number_of_collisions(board, i, col) == 0:
            board[i][col] = 1
            if backtrackSolver(board, col + 1):
                return True
            board[i][col] = 0
    return False


def backtrackMRVSolver(board, col, col_list):

    for i in range(len(board)):
        if number_of_collisions_full(board, i, col) == 0:
            board[i][col] = 1
            col_list.remove(col)
            if not col_list:
                return True

            col, min_free_pos = colMinFree(board, col_list.copy())
            if min_free_pos == 0:
                board[i][col] = 0
                return False

            if backtrackMRVSolver(board, col, col_list.copy()):
                return True
            board[i][col] = 0
    return False


# Initializing The Board
n = int(input("Please Enter the size of Game board you wanna have: "))
game_board = [[0 for _ in range(n)] for _ in range(n)]

# Simple bactrack
if not backtrackSolver(game_board, 0):
    print("Could not find any possible solution!")
else:
    show_GameBoard(game_board)
print('----------------------')

game_board = [[0 for _ in range(n)] for _ in range(n)]

# MRV-backtrack
if not backtrackMRVSolver(game_board, 0, [i for i in range(len(game_board))]):
    print("Could not find any possible solution!")
else:
    show_GameBoard(game_board)
