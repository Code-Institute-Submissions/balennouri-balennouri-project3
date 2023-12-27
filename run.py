#Globals Variables
# Game Board for tic tac toe
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# If the game is still playing
game_is_still_playing = True

# Who won? or tie?
winner = None

# Whos turn is it
current_player = "X"


def display_board():
    """
    Create the board for Tic Tac Toe, how it should look like. 
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    """
    Play game displays the board, handles the turns,
    flips the turn to the other player and check if the game has ended.
    """
    display_board()

    while game_is_still_playing:
     handle_turn(current_player)
     check_if_game_over()
     flip_player()

    if winner == "X" or winner == "O":
       print(winner + "Has won the game.\n")
    elif winner == None:
       print("Tie.\n")



def handle_turn(player):
    """
    Handles the turn and put the markers for each player.
    """
    position = input("Choose a position from 1-9\n")
    position = int(position) - 1

    board[position] = "X"
    display_board()

    
def check_if_game_over():
   check_if_win()
   check_if_tie()


def check_if_win():
   # check rows
   # check columns
   # check diagonals
   return

def check_if_tie():
   return
   

def flip_player():
   return
   


play_game()