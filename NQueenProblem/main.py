import time

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = False

def n_queens(n):
    board = [[False] * n for _ in range(n)]
    solutions = []
    start_time = time.time()
    solve_n_queens(board, 0, n, solutions)
    end_time = time.time()
    
    for sol in solutions:
        print_board(sol)
    
    print(f"N = {n}, Total Solutions: {len(solutions)}, Execution Time: {end_time - start_time:.6f} seconds\n")
    return solutions


n_queens(5) # 5 row and columns
