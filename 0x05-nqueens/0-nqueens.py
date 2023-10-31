#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[
                i] + i == col + row:
            return False
    return True


def solve_nqueens(N):

    def solve(row, board):
        if row == N:
            return [board[:]]
        solutions = []
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solutions += solve(row + 1, board)
                board[row] = -1
        return solutions

    board = [-1] * N
    return solve(0, board)


def print_solution(solution):
    for row in solution:
        print([row[i] for i in range(len(row))])


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
            print()

    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main":
    main()
