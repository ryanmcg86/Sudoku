import time

def is_safe(n, r, c, size, matrix):
    for i in range(size):
        if matrix[r][i] == n: return False
    for i in range(size):
        if matrix[i][c] == n: return False
        
    row_start = (r / 3) * 3
    col_start = (c / 3) * 3
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if matrix[i][j] == n: return False
            
    return True
    
def number_unassigned(row, col, size, matrix):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0: return [i, j, 1]
            
    return [-1, -1, 0]

def solve_sudoku(size, matrix):
    row, col = 0, 0
    a = number_unassigned(row, col, size, matrix)
    
    if a[2] == 0: return True
    
    row, col = a[0], a[1]
    
    for i in range(1, size + 1):
        if is_safe(i, row, col, size, matrix):
            matrix[row][col] = i
            if solve_sudoku(size, matrix): return True
            matrix[row][col] = 0
            
    return False
    
def solve(size, matrix):
    start = time.time()
    
    if solve_sudoku(size, matrix):
        for i in matrix:
            print i
    else:
        print 'No solution.'
        
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
size = 9
matrix = [
[0, 0, 0, 3, 7, 0, 0, 2, 0],
[0, 9, 0, 0, 8, 5, 7, 0, 0],
[3, 0, 0, 9, 0, 0, 0, 0, 5],
[1, 0, 0, 0, 0, 0, 0, 8, 0],
[0, 0, 0, 0, 0, 0, 3, 0, 0],
[0, 0, 0, 0, 9, 0, 0, 0, 7],
[2, 0, 0, 6, 0, 0, 0, 0, 1],
[0, 4, 8, 0, 0, 0, 6, 0, 0],
[0, 3, 0, 0, 0, 0, 0, 4, 0]]

solve(size, matrix)
