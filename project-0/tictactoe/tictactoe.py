"""
Tic Tac Toe Player
"""

import math
import copy

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
    nx = 0
    no = 0
    for row in board:
        for item in row:
            if item == X:
                nx += 1
            elif item == O:
                no += 1
    return O if nx > no else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return set(
        (i, j) for i in range(len(board)) for j in range(len(board[i]))
        if board[i][j] is None
    )


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or j < 0 or i >= 3 or j >= 3 or board[i][j] is not None:
        raise Exception('invalid action')
    new_board_state = copy.deepcopy(board)
    p = player(board)
    new_board_state[i][j] = p
    return new_board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not None and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    for j in range(3):
        if board[0][j] is not None and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all(item is not None for row in board for item in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return { X: 1, None: 0, O: -1 }[winner(board)]


def max_val(board, alpha, beta):
    """
    Maximizes the utility of board with alpha-beta pruning.
    """
    if terminal(board):
        return utility(board), None
    
    v = -2
    a = None

    for action in actions(board):
        nv, _ = min_val(result(board, action), alpha, beta)

        if nv >= v:
            v = nv
            a = action

        alpha = max(alpha, v)

        if alpha > beta:
            return v, a
        
    return v, a


def min_val(board, alpha, beta):
    """
    Minimizes the utility of board with alpha-beta pruning.
    """
    if terminal(board):
        return utility(board), None
    
    v = 2
    a = None

    for action in actions(board):
        nv, _ = max_val(result(board, action), alpha, beta)

        if nv <= v:
            v = nv
            a = action

        beta = min(beta, v)

        if alpha > beta:
            return v, a
        
    return v, a


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    if p == X:
        v, a = max_val(board, -2, 2)
    else:
        v, a = min_val(board, -2, 2)
    return a
    
