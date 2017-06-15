''' Note, this game is not smart enough to see errors in turns, or 
see a winner, just showing how to define and use a dictionary '''

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}# Defines Dictionary

def printBoard(board): # Defines the board the user sees
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'  # Initializes 'X' or 'O'
for i in range(9):
	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X': 	# Alternates 'X' and 'O' each turn
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)
