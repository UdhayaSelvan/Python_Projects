""" This is a python program to play Tic Tac Toe by using functions.
You need a friend to play this game, where you both can choose a marker ("X" or "O") and start playing.
Whoever matches three of their markers on the board (diagonally or vertically or horizontally) wins."""


# importing clear_output module from IPython.display
from IPython.display import clear_output


#a print function to print the welcome message
def welcome():
    print("Welcome to Tic Tac Toe!")


#structure of the board
def blue_print():
    elements = "         |         |         \n    1    |    2    |    3    \n_________|_________|_________\n         |         |         \n    4    |    5    |    6    \n_________|_________|_________\n         |         |         \n    7    |    8    |    9    \n         |         |         "
    return elements


#a function for both players to select a marker
def choose_marker(): # = marker
    coin = ''
    while coin not in ['X', 'O']:        
        coin = input("Player1 please choose your marker (X or O): ")
        if coin not in ['X', 'O']:
            print("Wrong choice!")
        else:
            print(f"\nplayer1's marker is {coin}")
            if coin == 'X':
                beats = 'O'
                print("player2's marker is O")
            else:
                beats = 'X'
                print("player2's marker is X")
    return coin, beats


#a function to get position of the marker
def valid_space(position,valid):
    valid = valid.replace(position, "#")
    return valid


#a function to check if the entered number (placeholder for marker) is valid or not
def choose_position(valid, player): # = position
    placement = ' '
    while placement not in valid:
        placement = input(f"{player} choose a number from 1 to 9 on the board!: ")
        if placement not in valid:
            print("Wrong choice!")
    return placement


#a function to place the marker on the board in the specific position (choosen number for the position)
def mark_embed(board, position, marker):
    bomb = board.replace(position, marker)
    return bomb


#a function to display the current board
def current_board(disp):
    for item in ['1','2','3','4','5','6','7','8','9']:
        disp = disp.replace(item, ' ')
    print(disp)


#a function to check if the game is draw
def check_draw(board, marker1, marker2):
    cynide = [34,44,54,124,134,144,214,224,234]
    condition = []
    for i in cynide:
        condition.append(board[i])
    if set(condition) == {marker1, marker2}:
        return True
    else:
        return False


#a function to check if anyone won already
def check_win(marker):
    if set((board[34],board[134],board[234])) == {marker} or set((board[54],board[134],board[214])) == {marker} or set((board[34],board[124],board[214])) == {marker} or set((board[44],board[134],board[224])) == {marker} or set((board[54],board[144],board[234])) == {marker} or set((board[34],board[44],board[54])) == {marker} or set((board[124],board[134],board[144])) == {marker} or set((board[214],board[224],board[234])) == {marker}:
        return True
    else:
        return False


#a function to ask player if they want to play again or not
def play_again():
    again = ''
    while again not in ['Y', 'N']:        
        again = input("Do you want to play again? (Y or N): ")
        if again not in ['Y', 'N']:
            print("Wrong choice!")
        elif again == 'Y':
            return True
        elif again == 'N':
            return False


welcome() #display the welcome message
marker1, marker2 = choose_marker() #player 1 choose a marker and the other player's marker is assigned automatically
board = blue_print() 
print(board) #display's the board
valid = "123456789" #valid positions from 1 to 9 only

#game play loop
while True:
    #player 1 starts always
    player = "Player 1"
    position = choose_position(valid, player) #player 1 will choose position
    valid = valid_space(position,valid) #check if the selected position is valid
    marker = marker1 #player1's marker
    disp = mark_embed(board, position, marker) #put the marker in the selected position
    clear_output() #clears the screen
    current_board(disp) #display the current board
    board = mark_embed(board, position, marker)
    if check_win(marker): #check for win on every round
        print(f"'{marker}' Won the Game!")
        if play_again():
            clear_output()
            welcome()
            board = blue_print()
            print(board)
            continue
        else:
            break
    if check_draw(board, marker1, marker2): #check for draw on every round
        print("The Game is DRAW!")
        if play_again():
            clear_output()
            welcome()
            board = blue_print()
            print(board)
            continue
        else:
            break
    player = "Player 2" #player 2's turn
    position = choose_position(valid, player)
    valid = valid_space(position,valid)
    marker = marker2
    disp = mark_embed(board, position, marker)
    clear_output()
    current_board(disp)
    board = disp
    if check_win(marker):
        print(f"'{marker}' Won the Game!")
        break
        
#End of the program
#You can use a python interpreter to run the code.
