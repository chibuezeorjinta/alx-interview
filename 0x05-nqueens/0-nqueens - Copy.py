#!/usr/bin/python3
"""Solve the n queens problem"""

# for a row, check if a queen can be placed
# in a cell from data provided from
# the above rows

# go through the queens pos list
# at each row
import sys

def nextRow(n: int, queen_pos):
	row = len(queen_pos)
	arr = [0 for i in range(n)]
	if row == n:
		return None
	for pos in queen_pos:
		queen_row = 0
		arr[pos] = 1
		pdiag = (row - queen_row) + pos
		ndiag = (row - queen_row) - pos
		if pdiag < n:
			arr[pdiag] = 1
		if ndiag >= 0:
			arr[ndiag] = 1
	return arr


def create_board(n: int):
	board = [
	[0 for i in range(n)]
	]
	return board

def change_board(queeen_pos: list=[0], board:list[list]=None, n=4):
	if board is None:
		board = create_board(n)
	if len(queeen_pos) == n:
		return queeen_pos
	elif len(board) == len(queeen_pos) and len(queeen_pos) < n:
		board.append(nextRow(n, queeen_pos))
		next_action = check_row(board[-1], n)
		if next_action:
			queeen_pos.append(next_action)
			return change_board(queeen_pos, board, n)
		else:
			if len(queeen_pos) == 0:
				board.pop()
				queeen_pos.pop()
			return change_board(queeen_pos, board)
	elif len(board) > len(queeen_pos):
		next_action = check_row(board[-1], n)
		if next_action:
			queeen_pos.append(next_action)
			return change_board(queeen_pos, board, n)
		else:
			if len(queeen_pos) == 0:
				board.pop()
				queeen_pos.pop()
			return change_board(queeen_pos, board)

def check_row(row, n):
    for i in range(n):
        if row[i] == 0:
            row[i] = n
            return i
        else:
            temp = row[i]
            row[i] = 1
            if check_row(row, n) is not False:
                return i
            row[i] = temp
    return False

if __name__ == '__main__':
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

	out_list = []
	formatted_board = []
	formatted_points: list[list] = []
	for i in range(num):
		out_list.append(change_board(n=num))

	formatted_board = [[index, value] for points in out_list for index, value in enumerate(points)]
	print(formatted_board)
		
