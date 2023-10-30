#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve(row):
        if row == N:
            solutions.append([row[:] for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions


def print_solution(solution):
    for row in solution:
        print(row)
    print()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_nqueens(N)
        for solution in solutions:
            print_solution(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main":
    main()
