###################
# tic-tac-toe     #
# kółko i krzyżyk #
# X's and O's     #
###################
# console edition #
###################

gameboard = list(range(1, 10))
token_x = "X"
token_o = "0"
win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # win combinations

# creates graphic representation of the gameboard in the console
def draw_gameboard(board): 
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

# checks if cell number entered by a player is correct
def is_cell_number_correct(n):
    if 1 <= n <= 9:
        return True
    else:
        return False

# cheks if token can be placed in a cell
def is_cell_empty(n):
    if n == "X" or n == "0":
        return False
    else:
        return True
    

def has_win_combo(token_sequence):
    for i in range(0, len(token_sequence)-2): 
        temp = (((token_sequence[i])-1), ((token_sequence[i+1])-1), ((token_sequence[i+2])-1))
        if temp in win_coord:
            win = True
    return win
            

def player_input(token):
    valid = False
    x_token_seq, o_token_seq = [], []
    while valid == False:
        player_answer = int(input("where to put" +token+ ":"))
        if is_cell_number_correct(player_answer):
            gameboard[player_answer-1] = token
            if token == "X":
                x_token_seq.append(player_answer)
                x_token_seq.sort()
                valid = True
            elif token == "0":
                o_token_seq.append(player_answer) 
                o_token_seq.sort()
                valid = True
        else:
            print("Enter a number from the range 1-9")
    return x_token_seq, o_token_seq
    
    
def main(board):
    count = 0
    x, o = [], []
    while count < 9:
        if count%2 == 0:
            result = player_input(token_x)
            x.append(result[0])
            count += 1
        else:
            player_input(token_o)
            o.append(result[1])
            count += 1
        if count > 4:
            if has_win_combo(x):
                print("player X wins!")
            elif has_win_combo(o):
                print("player O wins!")
            elif counter == 9:
                print("DRAW")


draw_gameboard(gameboard)
print("##################\n# Start of input #\n##################")
main(gameboard)
print("##################\n#  End of input  #\n##################")
draw_gameboard(gameboard)
