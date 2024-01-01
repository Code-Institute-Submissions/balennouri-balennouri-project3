
# Function to print Tic Tac Toe
def print_tic_tac_toe(BOARD):
	"""
	Create the board for Tic Tac Toe and the refernce board.
	"""
	print("\nReference board: \n")
	print("|1|2|3|")
	print("|4|5|6|")
	print("|7|8|9| \n")
	
	print("\n")
	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(BOARD[0], BOARD[1], BOARD[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(BOARD[3], BOARD[4], BOARD[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")

	print("\t  {}  |  {}  |  {}".format(BOARD[6], BOARD[7], BOARD[8]))
	print("\t     |     |")
	print("\n")


# Function to print the score-board
def scoreboard_print(score_board):
	"""
	Print the scoreboard for the game.
   """
	print("\t--------------------------------")
	print("\t       	   SCOREBOARD       ")
	print("\t--------------------------------")

	players = list(score_board.keys())
	print("\t   ", players[0], "\t    ", score_board[players[0]])
	print("\t   ", players[1], "\t    ", score_board[players[1]])

	print("\t--------------------------------\n")

# Function to check if any player has won
def check_win(player_position, current_player):

	# All possible winning combinations
	soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

	# Loop to check if any winning combination is satisfied
	for x in soln:
		if all(y in player_position[current_player] for y in x):

			# Return True if any winning combination satisfies
			return True
	# Return False if no combination is satisfied		
	return False		

# Function to check if the game is drawn
def check_draw(player_position):
	if len(player_position['X']) + len(player_position['O']) == 9:
		return True
	return False		

# Function for a single game of Tic Tac Toe
def single_game(current_player):

	# Represents the Tic Tac Toe
	BOARD = [' ' for x in range(9)]
	
	# Stores the positions occupied by X and O
	player_position = {'X':[], 'O':[]}
	
	# Game Loop for a single game of Tic Tac Toe
	while True:
		print_tic_tac_toe(BOARD)
		
		# Try exception block for MOVE input
		try:
			print("Player ", current_player, " turn. Which box? : ", end="")
			move = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again")
			continue

		# Sanity check for MOVE inout
		if move < 1 or move > 9:
			print("Wrong Input!!! Try Again")
			continue

		# Check if the box is not occupied already
		if BOARD[move-1] != ' ':
			print("Place already filled. Try again!!")
			continue

		# Update game information

		# Updating grid status 
		BOARD[move-1] = current_player

		# Updating player positions
		player_position[current_player].append(move)

		# Function call for checking win
		if check_win(player_position, current_player):
			print_tic_tac_toe(BOARD)
			print("Player ", current_player, " has won the game!!")		
			print("\n")
			return current_player

		# Function call for checking draw game
		if check_draw(player_position):
			print_tic_tac_toe(BOARD)
			print("Game Drawn")
			print("\n")
			return 'D'

		# Switch player moves
		if current_player == 'X':
			current_player = 'O'
		else:
			current_player = 'X'

if __name__ == "__main__":

	print("Player 1")
	player1 = input("Enter the name : ")
	print("\n")

	print("Player 2")
	player2 = input("Enter the name : ")
	print("\n")
	
	# Stores the player who chooses X and O
	current_player = player1

	# Stores the choice of players
	player_choice = {'X' : "", 'O' : ""}

	# Stores the options
	options = ['X', 'O']

	# Stores the scoreboard
	score_board = {player1: 0, player2: 0}
	scoreboard_print(score_board)

	# Game Loop for a series of Tic Tac Toe
	# The loop runs until the players quit 
	while True:

		# Player choice Menu
		print("Turn to choose for", current_player)
		print("Enter 1 for X")
		print("Enter 2 for O")
		print("Enter 3 to Quit")

		# Try exception for CHOICE input
		try:
			choice = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again\n")
			continue

		# Conditions for player choice	
		if choice == 1:
			player_choice['X'] = current_player
			if current_player == player1:
				player_choice['O'] = player2
			else:
				player_choice['O'] = player1

		elif choice == 2:
			player_choice['O'] = current_player
			if current_player == player1:
				player_choice['X'] = player2
			else:
				player_choice['X'] = player1
		
		elif choice == 3:
			print("Final Scores")
			scoreboard_print(score_board)
			break	

		else:
			print("Wrong Choice!!!! Try Again\n")

		# Stores the winner in a single game of Tic Tac Toe
		winner = single_game(options[choice-1])
		
		# Edits the scoreboard according to the winner
		if winner != 'D' :
			player_won = player_choice[winner]
			score_board[player_won] = score_board[player_won] + 1

		scoreboard_print(score_board)
		# Switch player who chooses X or O
		if current_player == player1:
			current_player = player2
		else:
			current_player = player1