#!/usr/bin/env python3
"""
Tic Tac Toe game with three difficulty levels: easy, medium, and hard.
Easy: random moves.
Medium: tries to win or block, otherwise random.
Hard: minimax algorithm for an optimal play.
"""

import random

PLAYER = 'X'
AI = 'O'
EMPTY = ' '
WIN_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def display_board(board):
    """Print the current Tic Tac Toe board."""
    print('\n')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('\n')


def get_available_moves(board):
    """Return the list of empty positions on the board."""
    return [index for index, value in enumerate(board) if value == EMPTY]


def check_winner(board):
    """Check the board and return 'X', 'O', 'Tie', or None."""
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]

    if EMPTY not in board:
        return 'Tie'

    return None


def make_move(board, position, marker):
    """Place a marker on the board at the given position."""
    board[position] = marker


def best_move(board, marker):
    """Return a winning or blocking move for the given marker if available."""
    for position in get_available_moves(board):
        board[position] = marker
        if check_winner(board) == marker:
            board[position] = EMPTY
            return position
        board[position] = EMPTY
    return None


def easy_ai(board):
    """Easy AI chooses a random available move."""
    return random.choice(get_available_moves(board))


def medium_ai(board):
    """Medium AI tries to win or block the player, otherwise chooses randomly."""
    win_move = best_move(board, AI)
    if win_move is not None:
        return win_move

    block_move = best_move(board, PLAYER)
    if block_move is not None:
        return block_move

    return easy_ai(board)


def minimax(board, depth, is_maximizing):
    """Minimax algorithm returning the score for the current board state."""
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    if winner == PLAYER:
        return depth - 10
    if winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = PLAYER
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def hard_ai(board):
    """Hard AI chooses the optimal minimax move."""
    best_score = -float('inf')
    chosen_move = None
    for move in get_available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            chosen_move = move
    return chosen_move


def get_ai_move(board, difficulty):
    """Select an AI move based on the difficulty level."""
    if difficulty == 'easy':
        return easy_ai(board)
    if difficulty == 'medium':
        return medium_ai(board)
    return hard_ai(board)


def get_user_move(board):
    """Prompt the user for a valid move."""
    available = get_available_moves(board)
    while True:
        user_input = input('Choose a position (1-9): ').strip()
        if user_input.isdigit():
            position = int(user_input) - 1
            if position in available:
                return position

        print('Invalid move. Try again.')


def choose_difficulty():
    """Let the user choose the AI difficulty."""
    options = {'1': 'easy', '2': 'medium', '3': 'hard'}
    print('Select difficulty:')
    print('1 - Easy')
    print('2 - Medium')
    print('3 - Hard')

    while True:
        choice = input('Enter 1, 2, or 3: ').strip()
        if choice in options:
            return options[choice]
        print('Please enter a valid choice.')


def choose_first_player():
    """Ask whether the player or AI should go first."""
    while True:
        choice = input('Do you want to go first? (y/n): ').strip().lower()
        if choice in ('y', 'yes'):
            return PLAYER
        if choice in ('n', 'no'):
            return AI
        print('Enter y or n.')


def play_game():
    """Run one Tic Tac Toe game."""
    board = [EMPTY] * 9
    difficulty = choose_difficulty()
    current_player = choose_first_player()

    print(f'You are {PLAYER}. AI is {AI}. Difficulty: {difficulty.title()}')

    while True:
        display_board(board)
        winner = check_winner(board)
        if winner is not None:
            break

        if current_player == PLAYER:
            position = get_user_move(board)
            make_move(board, position, PLAYER)
            current_player = AI
        else:
            print('AI is thinking...')
            position = get_ai_move(board, difficulty)
            make_move(board, position, AI)
            current_player = PLAYER

    display_board(board)
    if winner == 'Tie':
        print('It is a tie!')
    else:
        print(f'{winner} wins!')


def main():
    print('=== Tic Tac Toe ===')
    while True:
        play_game()
        answer = input('Play again? (y/n): ').strip().lower()
        if answer not in ('y', 'yes'):
            print('Thanks for playing!')
            break


if __name__ == '__main__':
    main()
