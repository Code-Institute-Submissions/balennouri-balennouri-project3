import os
import shutil


# Globals Variables

# Center the print logs
columns = shutil.get_terminal_size().columns
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
    Create the board for Tic Tac Toe and the refernce board.
    """
    print("\nReference board: \n")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9| \n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    """
    Play game displays the board, handles the turns,
    flips the turn to the other player and check if the game has ended.
    Ask the users if they want to play again.
    """
    while True:
        display_board()
        while game_is_still_playing:
            handle_turn(current_player)
            check_if_game_over()
            flip_player()
            clear_reset_screen()
            display_board()
        # give the user who have won and if they want to play again.
        if winner == "X" or winner == "O":
            print(winner + " Has won the game.\n")
            print("Play Again?")
            print("'p' To play again")
            print("'q' To go back to the menu")
        elif winner is None:
            print("It was a draw!\n")
            print("Play Again?")
            print("'p' To play again")
            print("'q' To go back to the menu")
        play_again = input("Your Choice: \n")
        if play_again.lower().strip() == "p":
            clear_reset_screen()
            reset_game()
        elif play_again.lower().strip() == "q":
            clear_reset_screen()
            reset_game()
            main()
        else:
            print("Wrong input choose again!")
            play_again = input("Your Choise: \n")


def reset_game():
    """
    Reset the game variables to start a new game.
    """
    global board, game_is_still_playing, winner, current_player
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    game_is_still_playing = True
    winner = None
    current_player = "X"


def handle_turn(player):
    """
    Handles the turn and put the markers for each player.
    Tells the users who's turn it's.
    don't let the players use a invalid input.
    with while loop it checks the users input if it's
    inavlid or correct or it will loop
    to they choose a valid one.
    """
    print("Choose a position from 1-9\n")
    position = input("It is " + current_player + " turn to choose: \n").strip()

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "Invalid input please " + current_player + " choose again: \n"
            )
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("That position is already taken. Go again.\n")
    board[position] = player
    display_board()


def check_if_game_over():
    """
    Checks if the game is over.
    """
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
    choice_of_user = input("Your Choice?: \n")
    while True:
        if choice_of_user.lower().strip() == "p":
            clear_reset_screen()
            play_game()
        elif choice_of_user.lower().strip() == "q":
            clear_reset_screen()
            main()
        else:
            print("Wrong input. Press 'p to play or 'q' to quit the game!")
            choice_of_user = input("Choose Again: \n")


def clear_reset_screen(numlines=100):
    """
    Clears the console to simplify UX and clear visual clutter.
    numlines is an fallback backup. Code taken from
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    if os.name == "posix":
        # for OS => Unix / Linux / MacOS / BSD / etc
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):
        #  for OS => DOS / Windows
        os.system("CLS")
    else:
        # Fallback for other operating systems.
        print("\n" * numlines)


def main():
    """
    Main functon that shows the start menu and calls the start game.
    Give the user the multiplayer menu, for start the game or quit.
    """
    clear_reset_screen()
    print("--------------------------".center(columns))
    print("Welcome to the multiplayer".center(columns))
    print("--------------------------".center(columns))
    print("--------------------------".center(columns))
    print("        Tic-Tac-Toe       ".center(columns))
    print("--------------------------".center(columns))
    print("What's your names?\n".center(columns))
    while True:
        name = input("First Player: \n".center(columns))
        if name.strip() == "":
            print("You need to choose a name".center(columns))
        else:
            print("Welcome " + name + " to the game!".center(columns))
            print(name + " will play with the 'X'\n".center(columns))
            while True:
                name_2 = input("second Player: \n")
                if name_2.strip() == "":
                    print("You need to choose a name")
                else:
                    print("Welcome " + name_2 + " to the game!")
                    print(name_2 + " will play with the 'O'\n")
                    print("'p' to play the game")
                    print("'r' to read the rules")
                    print("'q' To quit the game")
                    print("--------------------")
                    user_choice = input("What's your choice: \n")
                    # Give the user option to play,read rules or quit.
                    while True:
                        if user_choice.lower().strip() == "r":
                            clear_reset_screen()
                            rules_for_game()
                        elif user_choice.lower().strip() == "p":
                            clear_reset_screen()
                            play_game()
                        else:
                            print(
                                "\nWrong input. Press 'p' to play or 'q' \
to quit the game."
                            )
                            user_choice = input("Choose Again: \n")


main()
