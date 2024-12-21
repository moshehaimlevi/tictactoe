import random

def print_board(board):
    for i in range(3):
        print(' | '.join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print('_' * 10)

def check_winner(board, symbol):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if all(board[i] == symbol for i in pattern):
            return True
    return False

def is_full(board):
    return all(cell != ' ' for cell in board)

def player_turn(board, player_name, symbol):
    while True:
        try:
            move = int(input(f"{player_name}'s turn ({symbol}). Enter a number from 1 to 9: ")) - 1
            if move < 0 or move > 8:
                raise ValueError("Invalid input, Choose between 1 and 9.")
            if board[move] != ' ':
                print("Try again.")
            else:
                board[move] = symbol
                break
        except ValueError as e:
            print(e)

def main():
    print("Welcome to Tic Tac Toe!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1_symbol = input(f"{player1_name}, choose your symbol (X or O): ").upper()
    if player1_symbol not in ['X', 'O']:
        player1_symbol = random.choice(['X', 'O'])
        print(f"{player1_name} didn't choose a valid symbol, so {player1_symbol} is randomly assigned.")

    player2_symbol = 'O' if player1_symbol == 'X' else 'X'
    print(f"{player2_name}'s symbol is {player2_symbol}.")

    board = [' '] * 9
    turn = 0

    while True:
        current_player = player1_name if turn % 2 == 0 else player2_name
        current_symbol = player1_symbol if turn % 2 == 0 else player2_symbol

        print_board(board)

        player_turn(board, current_player, current_symbol)

        if check_winner(board, current_symbol):
            print_board(board)
            print(f"Congratulations {current_player}, you win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1



