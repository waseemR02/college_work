def solve_sudoku(board):
    # Find the first empty cell in the board
    empty_cell = find_empty_cell(board)
    
    # If there are no empty cells, the puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try filling in a digit from 1 to 9
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # If the move is valid, set the cell to the chosen number
            board[row][col] = num
            
            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True
            
            # If the puzzle cannot be solved with this choice, backtrack
            board[row][col] = 0
    
    # If no valid number can be placed, backtrack to the previous cell
    return False

def find_empty_cell(board):
    # Find the first empty cell in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(board, row, col, num):
    # Check if the chosen number is valid for the given cell
    return (
        not used_in_row(board, row, num) and
        not used_in_col(board, col, num) and
        not used_in_box(board, row - row % 3, col - col % 3, num)
    )

def used_in_row(board, row, num):
    # Check if the number is used in the same row
    return num in board[row]

def used_in_col(board, col, num):
    # Check if the number is used in the same column
    return num in [board[i][col] for i in range(9)]

def used_in_box(board, box_start_row, box_start_col, num):
    # Check if the number is used in the 3x3 box
    for i in range(3):
        for j in range(3):
            if board[i + box_start_row][j + box_start_col] == num:
                return True
    return False

# Example Sudoku board
sudoku_board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
