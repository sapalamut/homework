# Global variables

#Game board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# If game still going
game_is_active = True

# Win or Tie?
winner = None

#Whos turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    
    
    display_board()
    
    while game_is_active:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
    
    #The Game has ended
    if winner == "X" or winner == "O":
        print(winner + " is the winner!")
    elif winner == None:
        print("It's a tie!")
    

def handle_turn(player):
    
    print(f"Now it's your turn {player}!")
    position = input("Choose a position from 1 to 9: ")
    
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")
        
        position = int(position) - 1
        
        if board[position] == "_":
            valid = True
        else:    
            print("Make another move!")   
    
    board[position] = player
    
    display_board()
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    
    global winner
    
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return



def check_rows():
    global game_is_active
    
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_is_active = False
    # Return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return


def check_columns():
    global game_is_active
    
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_is_active = False
    # Return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    
    return


def check_diagonals():
    global game_is_active
    
    diagonals_1 = board[0] == board[4] == board[8] != "_"
    diagonals_2 = board[6] == board[4] == board[2] != "_"
    if diagonals_1 or diagonals_2:
        game_is_active = False
    # Return the winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
      
    return


def check_if_tie():
    global game_is_active
    
    if "_" not in board:
        game_is_active = False
        
    return



def flip_player():
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()    

