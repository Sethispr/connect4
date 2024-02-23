# Author: Sethispr
# Date: 02/22/24
# Python code for playing a board game called connect4 versus an AI. Can also be used to calulate the best move vs an opponent irl.
# The AI uses the minimax algorithm with alpha-beta pruning to make its moves. You can choose your moves by entering a column number when prompted.
# pip install -r requirements.txt if modules do not install themselves.

import numpy as np
from termcolor import colored

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def evaluate_window(window, piece):
    score = 0
    opponent_piece = 1
    if piece == 1:
        opponent_piece = 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    # Score center column
    center_array = [int(i) for i in list(board[:, 3])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(6):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(4):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Score Vertical
    for c in range(7):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negatively sloped diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, 100000000000000)
            elif winning_move(board, 1):
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, 2))
    if maximizingPlayer:
        value = -np.Inf
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:
        value = np.Inf
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def get_valid_locations(board):
    valid_locations = []
    for col in range(7):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def print_board(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == 0:
                print(colored(u'\u25A1', 'blue'), end=" ") # empty slot
            elif board[row][col] == 1:
                print(colored(u'\u25A0', 'red'), end=" ") # player 1's piece
            else:
                print(colored(u'\u25A0', 'yellow'), end=" ") # player 2's piece
        print()
    print(colored("0 1 2 3 4 5 6", 'yellow', attrs=['bold']))

def play_connect4():
    board = np.zeros((6, 7))
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        if turn == 0:
            try:
                col = int(input("\n" + colored("Player 1", 'red', attrs=['bold']) + " make your selection (0-6): "))
                print("\n")
                if col < 0 or col > 6:
                    raise ValueError("Invalid column!")
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    print_board(board)
                    print("\n" + "=" * 50)
                    print(colored("[Info]", 'green', attrs=['bold']), colored(f": {colored('Player 1', 'red', attrs=['bold'])} placed a piece in column {col}, row {chr(5 - row + ord('A'))}.", 'white', attrs=['bold']))
                    print("=" * 50 + "\n")

                    if winning_move(board, 1):
                        print("\n" + colored("[Info]", 'green', attrs=['bold']), colored(": Player 1 (You) wins!", 'white', attrs=['bold']))
                        game_over = True
                        break

                    turn = 1  # Switch to Player 2's turn
                else:
                    print("\n" + colored("[Warning]", 'yellow', attrs=['bold']), colored(": Column is full! Choose another column.", 'white', attrs=['bold']))
            except ValueError as ve:
                print("\n" + colored("[Error]", 'red', attrs=['bold']), colored(":", 'white', attrs=['bold']), ve)
        else:
            col, minimax_score = minimax(board, 5, -np.Inf, np.Inf, True)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                print_board(board)
                print("\n" + "=" * 50)
                print(colored("[Info]", 'green', attrs=['bold']), f": {colored('Player 2', 'yellow', attrs=['bold'])} placed a piece in column {col}, row {chr(5 - row + ord('A'))}.")
                print("=" * 50)

                if winning_move(board, 2):
                    print("\n" + colored("[Info]", 'green', attrs=['bold']), f": {colored('Player 2 (AI)', 'yellow', attrs=['bold'])} wins!")
                    game_over = True
                    break

                turn = 0  # Switch to Player 1's turn

            if is_terminal_node(board):
                print("\n" + colored("[Info]", 'green', attrs=['bold']), colored(": It's a tie!", 'white', attrs=['bold']))
                game_over = True

play_connect4()
