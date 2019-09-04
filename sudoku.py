import time

#Build an is_safe function
def is_safe(n, r, c, matrix):
    for i in range(len(matrix[0])):
        if matrix[r][i] == n: return False
    for i in range(len(matrix[0])):
        if matrix[i][c] == n: return False
        
    row_start = (r / 3) * 3
    col_start = (c / 3) * 3
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if matrix[i][j] == n: return False
            
    return True
 
#Build a number_unassigned function
def number_unassigned(row, col, matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0: return [i, j, 1]
            
    return [-1, -1, 0]

#Build a solve_sudoku function
def solve_sudoku(matrix):
    row, col = 0, 0
    a = number_unassigned(row, col,  matrix)
    
    if a[2] == 0: return True
    
    row, col = a[0], a[1]
    
    for i in range(1, len(matrix[0]) + 1):
        if is_safe(i, row, col, matrix):
            matrix[row][col] = i
            if solve_sudoku(matrix): return True
            matrix[row][col] = 0
            
    return False
   
#Build a solve function
def solve(matrix):
    start = time.time()
    
    if solve_sudoku(matrix):
        for i in matrix:
            print i
    else:
        print 'No solution.'
        
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'
    
#Run the program
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

solve(matrix)
