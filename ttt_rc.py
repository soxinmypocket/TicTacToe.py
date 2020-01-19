#Tic Tac Toe
#Using Python 3.7

#Create board.
def tic_tac_toe_board():
    board = [None] + list(range(1, 10))


#Display board and define draw.
    def draw():
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print()


#Winning combinations & valid moves.
    winning_combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]


    def choose_number():
        while True:
            try:
                x = int(input())
                if x in board:
                    return x
                else:
                    print("\nInvalid move. Pick another number!")


#If invalid entry is chosen, prompt to pick a number instead.
            except ValueError:
                print("\nThat's not a number.\n Try again")


#Check wins to see if a player wins.
    def game_over():
        for x, y, z in winning_combinations:
            if board[x] == board[y] == board[z]:
                print("Player {0} wins!\n".format(board[x]))
                print("Congratulations! You won! \n")
                return True


#If no winning combination is drawn, game ends in a tie.
            if 9 == sum((tie == 'X' or tie == 'O') for tie in board):
                print("We have a tie! \n")
                return True


#Input moves, allows players to take turns & updates board.
    for player in 'XO' * 9:
        draw()
        if game_over():
            break
        print("Player {0} pick your move".format(player))
        board[choose_number()] = player
        print()
while True:
    tic_tac_toe_board()
    break
