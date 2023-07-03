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
win_coord = ([0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]) # win combinations

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
    win = False
    for i in range(len(token_sequence)-1, 1, -1): 
        temp = [token_sequence[i], token_sequence[i-1], token_sequence[i-2]]
        tmp = sorted(temp)
        if tmp in win_coord:
            win = True
            break
    return win
            

def player_input(token):
    valid = False
    while valid == False:
        player_answer = int(input("where to put " +token+ ": "))
        if is_cell_number_correct(player_answer):
            cn = player_answer-1 # cell number
            gameboard[cn] = token
            valid = True
        else:
            print("Enter a number from the range 1-9")
    return cn

    
def main(board):
    count = 0
    x, o = [], []
    while count < 9:
        if count%2 == 0:
            result = player_input(token_x)
            x.append(result)
            count += 1
            if count > 4:
                if has_win_combo(x):
                    print("player X wins!")
                    break
        elif count%2 == 1:
            player_input(token_o)
            o.append(result)                
            count += 1
            if count > 5:
                if has_win_combo(o):
                    print("player O wins!")
                    break
        elif count == 9:
            print("DRAW")


draw_gameboard(gameboard)
print("##################\n# Start of input #\n##################")
main(gameboard)
print("##################\n#  End of input  #\n##################")
draw_gameboard(gameboard)
