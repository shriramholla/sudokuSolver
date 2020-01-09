#Function that outputs a 9x9 2D array
def getGrid(arr):
    for i in range(9):
        print(*arr[i], sep=' ')

# Function that check for empty spots in the 2D array
def is_it_solved(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                return False
    return True

# Function that gets the row and column of an empty spot
def getEmptyCells(arr, l):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j

# Function that checks for repetition in the same line (horizontal or vertical)
def isvalid(arr, row, col, num):
    for i in range(9):
        if arr[row][i] == num or arr[i][col] == num:
            return False
    return True and sameBox(arr, row, col, num)

# Function that checks for repetition in the same 3x3 Box
def sameBox(arr, row, col, num):
    qRow = row // 3;
    qCol = col // 3;
    for i in range(3):
        for j in range(3):
            if arr[3 * qRow + i][3 * qCol + j] == num:
                return False
    return True

# Recursive and Backtracking step
def solve(arr):
    l = [0, 0]
    if is_it_solved(arr):
        return True
    getEmptyCells(arr, l)
    row = l[0]
    col = l[1]
    for i in range(1, 10):
        if isvalid(arr, row, col, i):
            arr[row][col] = i
            if solve(arr): # recurses here
                return True
            arr[row][col] = 0
    return False # Backtracks here

# Sample Test
grid = \
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 7, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 9, 0, 7, 3],
     [0, 0, 0, 0, 0, 2, 0, 0, 0],
     [2, 0, 0, 4, 1, 3, 0, 0, 0],
     [0, 0, 5, 0, 9, 0, 2, 6, 0],
     [7, 0, 8, 0, 0, 0, 0, 0, 0],
     [0, 4, 2, 0, 3, 0, 0, 0, 8],
     [0, 5, 0, 8, 0, 4, 0, 0, 0]]


if solve(grid):
    print("Solved!")
    getGrid(grid)
else:
    print("No Solution")
