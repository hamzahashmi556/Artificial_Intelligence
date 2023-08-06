# TO IMPLEMENT A PROGRAM TO SOLVE THE N_QUEEN PROBLEM
# N_Queens = int(input("Enter the No. of Queens : "))
# Solution = [0 for x in range(N_Queens)]
# Multiple_Solutions = []

solutionNumber = 1
def IsSafe(test_row, test_col):
    if test_row == 0:
        return True
    for row in range(0, test_row):
        if test_col == Solution[row]:
            return False
        if abs(test_row-row) == abs(test_col-Solution[row]):
            return False
    return True

def Place_Queen(row):
    global Multiple_Solutions, Solution, N_Queens
    for i in range(N_Queens):
        if not IsSafe(row, i):
            continue
        else:
            Solution[row] = i
            if row == N_Queens-1:
                Multiple_Solutions.append(Solution.copy())

            else:
                Place_Queen(row+1)


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row):
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1)
            board[row][col] = 0


def print_board(board):
    global solutionNumber
    print(f"Solution # {solutionNumber}")
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))
    solutionNumber += 1
    print()



if __name__ == "__main__":
    # Place_Queen(0)
    # print(len(Multiple_Solutions), "Solutions Found")
    # for i in Multiple_Solutions:
    #     print(i)
    n = 8
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(chessboard, 0)
