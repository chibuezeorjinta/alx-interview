#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (num >= 4):
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """NQueens Attenpt"""
    col = set()
    pos_diag = set()
    negative_diag = set()

    result = []

    board = [[] for n in range(n)]

    def backtrack(row):
        """Impliment backtracking"""
        if row == n:
            copy = board.copy()
            result.append(copy)
            return
        for c in range(n):
            if c in col or (row + c) in pos_diag or (row - c) in negative_diag:
                continue
            col.add(c)
            pos_diag.add(row + c)
            negative_diag.add(row - c)
            board[row] = [row, c]
            backtrack(row + 1)
            col.remove(c)
            pos_diag.remove(row + c)
            negative_diag.remove(row - c)
            board[row] = []

    backtrack(0)

    return result


if __name__ == "__main__":
    """main function"""
    boards = solveNQueens(num)
    for board in boards:
        print(board)
