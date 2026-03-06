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
    # count X & O if equal X, if not equal O
    no_X = 0
    no_O = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i, j] == O:
                no_O = no_O + 1
            if board[i, j] == X:
                no_X = no_X + 1

    if no_X > no_O:
       return O
    if no_X == no_O:
       return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i, j] == O:
                actions.add((i, j))

    return actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i, j] = board[i , j]

    new_board[action[0], action[1]] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = EMPTY
    for i in range(len(board)):
        for j in range(len(board[i])):
            if winner ==  EMPTY:
                winner = board[i,j]
            else:
                if winner != board[i,j]:
                    winner = EMPTY
                    continue
    if winner != EMPTY:
        return winner

    for j in range(len(board)):
        for i in range(len(board[i])):
            if winner ==  EMPTY:
                winner = board[i,j]
            else:
                if winner != board[i,j]:
                    winner = EMPTY
                    continue
    if winner != EMPTY:
        return winner

    for i in range(len(board)):
        for j in range(len(board[i])):
            if winner ==  EMPTY:
                winner = board[i,j]
            else:
                if winner != board[i,j]:
                    winner = EMPTY
                    continue
    if winner != EMPTY:
        return winner

    winner = board[1, 1]
    if winner == board[0, 0] and winner != board[2,2]:
        return winner

    if winner == board[0, 2] and winner != board[2,0]:
        return winner

    return EMPTY

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True

    if actions(board) != None:
        return True

    return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1

    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # start with current boardcheck50 ai50/projects/2024/x/tictactoe
    # get all new actions from current state
    # iterate through each action iteratively
    # when processing an action recusrsively call actions for that board
    # the recursive call should return the minmax or maxmin for that board state
    # depending on who is playing
    # if tis a leaf node there is no recursive call . instead we iterate over the
    # leaves to get the min max
    # similarly where the branches merge will be s iteration over the branches to
    # get min max


    actions = actions(board)
    max = True

    if player(board) == O:
        max = False
    current_value = 0;
    for action in actions:
        new_board = result(board, action)
        if winner(new_board) == X:
            return 1
        if winner(new_board) == O:
            return -1

        if terminal(new_board):
            return 0

        if max:
            current_value = max(current_value, minimax(new_board))
        else:
            current_value = min(current_value, minimax(new_board))

    return current_value

    raise NotImplementedError
