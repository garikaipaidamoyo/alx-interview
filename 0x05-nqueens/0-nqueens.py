#!/usr/bin/python3
import sys


def is_safe(board, row, col, queens):
    for prev_row in range(row):
        prev_col = queens[prev_row]
        if (prev_col == col or prev_col - prev_row == col - row
                or prev_col + prev_row == col + row):
            return False
    return True


def solve_nqueens(N):

    def solve(row, queens, solutions):
        if row == N:
            solutions.append(queens[:])
            return

        for col in range(N):
            if is_safe(board, row, col, queens):
                queens.append(col)
                solve(row + 1, queens, solutions)
                queens.pop()

    solutions = []
    board = [-1] * N
    solve(0, [], solutions)
    return solutions


def print_solution(solution):
    for row in solution:
        queens = [-1] * len(solution)
        queens[row] = solution[row]
        print(queens)


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
