import os


# Globals Variables
# Game Board for tic tac toe
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# If the game is still playing
game_is_still_playing = True


# Who won? or tie?
winner = None


# Whos turn is it
current_player = 'X'


def start_menu():
   """
   This menu comes when user come in to the game.
   The user will have two options, to play singel player or multiplayer.
   User will notice that the singelplayer mode is not ready when user push on it,
   it will give a print message and inform the user.
   """
   clear_reset_screen()
   print("\nWelcome to the Tic Tac Toe game\n")
   print("You want to play singel player or multiplayer?\n")
   print("------------------------------------------------")
   print("------------------------------------------------\n")
   print("'s' To play singel player")
   print("'m' To play multiplayer")
   player_choice = input("What's your choice: ")
   while True:
      if player_choice == "m":
         clear_reset_screen()
         start_the_multiplayer()
      elif player_choice == "s":
         clear_reset_screen()
         start_the_singelplayer()
      else:
         print("\nWrong input. Press 's' to play singelplayer and 'm' to play mulitplayer.")
         player_choice = input("Choose Again: ")


def start_the_singelplayer():
   """
   Welcome the user to the singelplayer mode.
   """
   clear_reset_screen()
   print("\nWelcome to the singel player")
   print("\n----------------------------")
   print("------------------------------\n")
   print("We are sorry the singel player mode are not ready yet!")
   print("\n------------------------------------------------------")
   print("------------------------------------------------------\n")
   print("'r' to read the rules")
   print("'m' to play multiplayer")
   print("'q' to go back to the menu\n")
   choice = input("Your Choice: ")
   while True:
      if choice == "r":
         clear_reset_screen()
         rules_for_game()
      elif choice == "q":
         clear_reset_screen()
         start_menu()
      elif choice == "m":
         clear_reset_screen()
         start_the_multiplayer()
      else:
         print("Wrong input.")
         print("Press 'r' to read the rules")
         print("'m' to play multiplayer.")
         print("'q' to go back to the start menu.\n")
         print("---------------------------------")
         print("---------------------------------\n")
         choice = input("Choose Again: ")


def start_the_multiplayer():
   """
   Give the user the multiplayer menu, for start the game or quit.
   """
   clear_reset_screen()
   print("\nWelcome to the multiplayer")
   print("----------------------------")
   print("----------------------------\n")
   print("What's your names?\n")
   name = input("First Player: ")
   print("Welcome " + name + " to the game!")
   print(name + " will play with the 'X'\n")
   name_2 = input("second Player: ")
   print("Welcome " + name_2 + " to the game!")
   print(name_2 + " will play with the 'O'\n")
   print("'p' to play the game")
   print("'r' to read the rules")
   print("'q' To quit the game")
   print("--------------------")
   user_choice = input("What's your choice: ")
   while True:
      if user_choice == "r":
         clear_reset_screen()
         rules_for_game()
      elif user_choice == "p":
         clear_reset_screen()
         play_game()
      elif user_choice == "q":
         clear_reset_screen()
         start_menu()
      else:
         print("\nWrong input. Press 'p to play or 'q' to quit the game!")
         user_choice = input("Choose Again: ")

 
def display_board():
    """
    Create the board for Tic Tac Toe and the refernce board. 
    """
    print("\nReference board: \n")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9| \n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def rules_for_game():
    """
    Explain the game and the rules.
    """
    print("")
    print("Tic-tac-toe is a game in which two players take turns in drawing")
    print("either an 'O' or an 'X' in one square of a grid")
    print("consisting of nine squares.")
    print("The winner is the first player to get three of the same symbols")
    print("in a row, vertically, horizontally or diagonally.")
    print("")
    print("Now press 'p' to play or 'q' to quit the game!")
    choice_of_user = input("Your Choice?: ")
    while True:
      if choice_of_user == "p":
         clear_reset_screen()
         play_game()
      elif choice_of_user == "q":
         clear_reset_screen()
         start_menu()
      else:
         print("Wrong input. Press 'p to play or 'q' to quit the game!")
         choice_of_user = input("Choose Again: ")

       
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
       print(winner + " Has won the game.\n")
    elif winner == None:
       print("It was a draw!\n")


def handle_turn(player):
    """
    Handles the turn and put the markers for each player.
    Tells the users who's turn it's.
    don't let the players use a invalid input.
    with while loop it checks the users input if it inavlid or correct or it will loop
    to they choose a valid one.
    """
    print("Choose a position from 1-9\n")
    position = input("It is " + current_player + " turn to choose: ")
    
    valid = False
    while not valid:

      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input please " + current_player + " choose again: ")

      position = int(position) - 1

      if board[position] == "-":
        valid = True
      else:
        print("That position is already taken. Go again.\n")

    board[position] = player

    display_board()

    
def check_if_game_over():
   check_for_win()
   check_if_tie()


def check_for_win():
   """
   Check for possible wins.
   """
   global winner
   row_winner = check_rows()
   columns_winner = check_columns()
   diagonals_winner = check_diagonals()
   if row_winner:
      winner = row_winner
   elif columns_winner:
      winner = columns_winner
   elif diagonals_winner:
      winner = diagonals_winner
   else:
      winner = None
   return
      

def check_rows():
   """
   This checks if any of the rows have all the same value of X or O.
   If it have the same it will return the winner.
   """
   global game_is_still_playing
   row_1 = board[0] == board[1] == board[2] != "-"
   row_2 = board[3] == board[4] == board[5] != "-"
   row_3 = board[6] == board[7] == board[8] != "-"
   if row_1 or row_2 or row_3:
      game_is_still_playing = False
   if row_1:
      return board[0]
   elif row_2:
      return board[3]
   elif row_3:
      return board[6]
   return
   
   
def check_columns():
   """
   This checks if any of the columns have all the same value of X or O.
   If it have the same it will return the winner.
   """
   global game_is_still_playing
   columns_1 = board[0] == board[3] == board[6] != "-"
   columns_2 = board[1] == board[4] == board[7] != "-"
   columns_3 = board[2] == board[5] == board[8] != "-"
   if columns_1 or columns_2 or columns_3:
      game_is_still_playing = False
   if columns_1:
      return board[0]
   elif columns_2:
      return board[1]
   elif columns_3:
      return board[2]
   return

       
def check_diagonals():
   """
   This checks if any of the diagonals have all the same value of X or O.
   If it have the same it will return the winner.
   """
   global game_is_still_playing
   diagonals_1 = board[0] == board[4] == board[8] != "-"
   diagonals_2 = board[6] == board[4] == board[2] != "-"
   if diagonals_1 or diagonals_2:
      game_is_still_playing = False
   if diagonals_1:
      return board[0]
   elif diagonals_2:
      return board[6]
   return


def check_if_tie():
   global game_is_still_playing
   if "-" not in board:
      game_is_still_playing = False
   return


def flip_player():
   """
   Change the players if current player is X
   then change it to O.
   """
   global current_player
   if current_player == "X":
      current_player = "O"
   elif current_player == "O":
      current_player = "X"
   return


def clear_reset_screen(numlines=100):
    """
    Clears the console to simplify UX and clear visual clutter.
    numlines is an fallback backup.
    """
    if os.name == "posix":
        # for OS => Unix / Linux / MacOS / BSD / etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        #  for OS => DOS / Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)
   

def main():
   """
   Main functon tat shows the start menu and calls the start game.
   """
   start_menu()
   display_board()
   play_game()


main()