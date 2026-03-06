"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_X = 0
    no_O = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == O:
                no_O += 1
            if board[i][j] == X:
                no_X += 1

    if no_X > no_O:
        return O
    if no_X == no_O:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []

    for i in range(len(board)):
        new_row = []
        for j in range(len(board[i])):
            new_row.append(board[i][j])
        new_board.append(new_row)

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    # check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not EMPTY:
        return True

    if len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    possible_actions = actions(board)
    is_max = True

    if player(board) == O:
        is_max = False

    current_value = 0

    for action in possible_actions:
        new_board = result(board, action)

        if winner(new_board) == X:
            return 1
        if winner(new_board) == O:
            return -1

        if terminal(new_board):
            return 0

        if is_max:
            current_value = max(current_value, minimax(new_board))
        else:
            current_value = min(current_value, minimax(new_board))

    return current_value
