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


def draw_gameboard(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def is_cell_number_correct(n):
    if 1 <= n <= 9:
        return True
    else:
        return False


def is_cell_empty(n):
    if n == "X" or n == "0":
        return False
    else:
        return True
    

def has_win_combo(token_sequence):
    for i in range(0, len(token_sequence)-2): 
        temp = ((token_sequence[i]-1), (token_sequence[i+1]-1), (token_sequence[i+2]-1))
        if temp in win_coord:
            win = True
    return win
            
def main(gameboard):
    count = 0
    win = False
    


draw_gameboard(gameboard)

# ci = 0  # counts users' inputs
# while ci < 9:
#     ci += 1
#     temp = int(input("Please enter cell number(1-9) for X:"))
#     gameboard[temp-1] = player_x_token
#     ci += 1
#     draw_gameboard(gameboard)
#     temp = int(input("Please enter cell number(1-9) for 0:"))
#     gameboard[temp-1] = player_0_token
#     draw_gameboard(gameboard)

print("##################\n# Start of input #\n##################")

print("##################\n#  End of input  #\n##################")
