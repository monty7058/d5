import time
prev = -1

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, n, r, c):
    global prev
    if row == n:
        return True
    
    if row == r:
        board[r][c] = 0
        if is_safe(board, r, c, n):
            board[r][c] = 1
            if solve_n_queens_util(board, r + 1, n, r, c):
                return True
            else:
                print("Backtracking")
                return False
    
    print(*board, sep="\n", end="\n\n")
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n, r, c):
                return True
            board[row][col] = 0
            print("Backtracking")
    
    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    r = int(input("Enter row of the first queen: "))
    c = int(input("Enter col of the first queen: "))
    board[r][c] = 1
    if solve_n_queens_util(board, 0, n, r, c):
        return board
    else:
        return None

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

def main():
    n = int(input("Enter the value of N: "))
    start_time = time.time()
    solution = solve_n_queens(n)
    end_time = time.time()
    
    if solution:
        print("Solution exists:")
        print_solution(solution)
    else:
        print("No solution exists.")
    
    print(f"\nTime taken: {(end_time - start_time):.6f} seconds\n")

if __name__ == "__main__":
    main()