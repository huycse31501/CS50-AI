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

def num(board):
    res = copy.deepcopy(board)
    for x in range(3):
        for y in range(3):
            if board[x][y] == X:
                res[x][y] = 1
            if board[x][y] == O:
                res[x][y] = -1
            if board[x][y] == EMPTY:
                res[x][y] = 0
    return res

def revnum(board):
    res = copy.deepcopy(board)
    for x in range(3):
        for y in range(3):
            if board[x][y] == 1:
                res[x][y] = X
            if board[x][y] == -1:
                res[x][y] = O
            else:
                res[x][y] = EMPTY

def checkempty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                return False
    return True

def sumdiag(board,pos):
    if pos == 0:
        sum1 = 0
        for i in range(3):
            sum1 += board[i][i]
        return sum1
    if pos == 1:
        sum1 = 0
        for i in range(3):
            sum1 += board[i][2 - i]
        return sum1


def sumcolumn(board,pos):
    sum1 = 0
    for i in range(3):
        sum1 += board[i][pos]
    return sum1

def player(board):
    res = num(board)
    sum1 = 0
    for i in range(3):
        sum1 += sum(res[i])
    if sum1 == 0:
        return X
    return O
    """
    Returns player who has the next turn on a board.
    """


def actions(board):
    res = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                a = (i,j)
                res.append(a)
    return set(res)
    """
    Returns set of all possible actions (i, j) available on the board.
    """


def result(board, action):
    numboard = num(board)
    a = action[0]
    b = action[1]
    if numboard[a][b] == 1 or numboard[a][b] == -1:
        raise NameError('Move not available')
    deepboard = copy.deepcopy(board)
    if player(board) == X:
        deepboard[a][b] = X
    else:
        deepboard[a][b] = O
    return deepboard
    """
    Returns the board that results from making move (i, j) on the board.
    """


def winner(board):
    board = num(board)
    for i in range(3):
        if sum(board[i]) == 3:
            return X
        if sum(board[i]) == -3:
            return O
        if sumcolumn(board,i) == 3:
            return X
        if sumcolumn(board,i) == -3:
            return O
    for i in range(2):
        if sumdiag(board,i) == 3:
            return X
        if sumdiag(board,i) == -3:
            return O
    return None
    """
    Returns the winner of the game, if there is one.
    """


def terminal(board):
    if winner(board) == X or winner(board) == O:
        return True
    board = num(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True
    """
    Returns True if game is over, False otherwise.
    """


def utility(board):
    if terminal(board) == True and winner(board) == X:
        return 1
    if terminal(board) == True and winner(board) == O:
        return -1
    if terminal(board) == True and winner(board) == None:
        return 0
            
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


def minimax(board):
    if terminal(board) == True:
        return None
    if checkempty(board) == True:
        return (1,1)
    c = ()
    if player(board) == X:
        deepboard = copy.deepcopy(board)
        for action in actions(board):
            deepboard = copy.deepcopy(board)
            deepboard = result(deepboard,action)
            if winner(deepboard) == X:
                return action
        for action in actions(board):
            deepboard = copy.deepcopy(board)
            a = action[0]
            b = action[1]
            deepboard[a][b] = O
            if winner(deepboard) == O:
                return action
            c = action
    if player(board) == O:
        deepboard = copy.deepcopy(board)
        for action in actions(board):
            deepboard = copy.deepcopy(board)
            deepboard = result(deepboard,action)
            if winner(deepboard) == O:
                return action
        for action in actions(board):
            deepboard = copy.deepcopy(board)
            a = action[0]
            b = action[1]
            deepboard[a][b] = X
            if winner(deepboard) == X:
                return action
            c = action
    return c 
    
            
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
