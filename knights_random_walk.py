# Knight's Random Walk Puzzle Solution
# Author: Thomas Scrace <tom@scrace.org>
# Date: 10/05/2012

'''
Start a knight at a corner square of an otherwise-empty chessboard. Move the knight at random by choosing uniformly from the legal knight-moves at each step. What is the mean number of moves until the knight returns to the starting square?

Source: http://www.johndcook.com/blog/2012/05/08/a-knights-random-walk/

The print_board routine isn't strictly necessary to solve the problem, but I include it anyway as a delightful bonus!
'''

import random

BOARD_SIZE = 8

def print_board(knight):
	'''
	Print out a representation of the current state of a chessboard with a single piece: a knight.
	'''
	knight = (knight[1], knight[0])
	for i in range(1, BOARD_SIZE + 1): print i,
	print
	for square in [(y, x) for y in range(BOARD_SIZE, 0, -1) for x in range(1, BOARD_SIZE + 1)]:
		if square[1] == 8:
			if square == knight:
				print 'k', square[0]
			else:
				print '_', square[0]
		else:
			if square == knight:
				print 'k',
			else:
				print '_',

def move_knight(start):
	'''
	Move a knight once, randomly. Return end location as a tuple of x, y values.
	'''
	moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
	while moves:
		move = moves[random.randint(0, len(moves) - 1)]
		end = (start[0] + move[0], start[1] + move[1])
		if end[0] in xrange(1, BOARD_SIZE + 1) and end[1] in xrange(1, BOARD_SIZE + 1):
			return end
		else:
			moves.remove(move)

def random_walk(start, verbose=False):
	'''
	Take a knight on a random walk starting at start and ending on return to start. Return the number /
	of moves.
	'''
	i = 0
	end = start
	while end != start or i == 0:
		if verbose: print_board(end)
		end = move_knight(end)
		i += 1
	if verbose: print_board(end)
	return i

def get_mean_walk_length(iterations=1000):
	'''
	Execute iterations random walks and return the mean walk length.
	'''
	corners = [(1, 1), (1, 8), (8, 8), (8, 1)]
	lengths = []
	while iterations:
		start = corners[random.randint(0, 3)]
		lengths.append(random_walk(start))
		iterations -= 1
	return sum(lengths) / len(lengths)

print get_mean_walk_length()