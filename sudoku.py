"""
Sudoku Game

This Python script implements a basic Sudoku game where the user can customize the board size
and make changes until they submit a potential solution. The game checks for valid solutions
and declares whether the user wins or not.

Functions:
- current_board(board): Display the current state of the Sudoku board.
- user_input(board, size): Allow the user to input values and update the board accordingly.
- re_start_board(size): Initialize and return a new Sudoku board with random values.
- check(board, size): Check if the current board configuration is a valid solution.

Main Function:
- main(): Execute the main logic of the Sudoku game, allowing the user to make changes,
  submit solutions, and exit the game.

Note:
This code serves as a practice project to demonstrate basic Python operations and may
benefit from improvements such as input validation, modularization, and enhanced user interface.
"""
import random
def current_board(board):
	print('Current Board\n: ')
	for i in board:
		print(i)
def user_input(board,size):
	current_board(board)
	row=int(input('Enter the row from where you want to change: '))
	col=int(input('Enter the column from where you want to change: '))
	value=int(input(f'Enter the new value(Enter a number in between 1 and {size}): '))
	board[row-1][col-1]=value
	current_board(board)
def re_start_board(size):
	board=[[0]* size  for i in range(size)]
	for i in range(0,size):
		for j in range(0,size):
			board[i][j]=random.randint(1,size)
	return board
def check(board,size):
	for i in range(size):
		for j in range(size):
			for k in range(size):
				if(j!=k and board[i][j] ==board[i][k]):
					return False
				if(i!=k and board[i][j] ==board[k][j]):
					return False
	return True
def main():
	print("""HEY ALL WELCOME TO CLASSIC SUDOKU...HERE YOU WILL BE GIVEN A CHANCE TO SELECT YOUR BOARD SIZE FROM 1 TO ANY VALUE OF YOU WISH.. THROUGH WHICH YOU CAN CUSTOMISE YOUR DIFFICULTY..IT CAN BE SIMPLE OR TOUGH.ITS YOUR LUCK ....!YOU WONT BE PROVIDED WITH THE SOLUTION..
	YOUR WIN AMD LOSS WILL BE DECLARED WHEN YOU SUBMIT YOUR SOLUTION...SO MOVEN ON...!!!""")
	size=int(input('\nEnter the size of your Sudoku board: '))
	board=re_start_board(size)
	current_board(board)
	while(1):
		print("""
		Type :
			1. To Make Changes
			2. To Submit
			3. To Exit""")
		submit=int(input('Enter your choice: '))
		print('\n')
		if(submit == 1):
			user_input(board,size)
		elif(submit==2):
			if(check(board,size)):
				print('You win')
				break
			else:
				print('This is not the solution\n')
				current_board(board)
		else:
			print('Thank You')
			break
main()
