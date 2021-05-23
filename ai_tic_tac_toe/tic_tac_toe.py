"""This is the main module of the tic-tac-toe game."""
import logging
from random import choice
import numpy as np

logging.basicConfig(filename="tic_tac_toe.log", \
    level=logging.INFO, format="%(message)s - %(asctime)s", datefmt='%d-%b-%y %H:%M:%S')


class TicTacToe:
    """This is a class of the main functions of the game"""
    def __init__(self, name_1, name_2):
        """Initialization of fields. Players are stored as a list of players names.
        stroke is a variable of the stroke, there is 0 specified,
        then the move is X, if 1, then the move is O.
        field - field of the game, consisting of 0; if X is placed, cell = 1, if O, then -1.
        win - equal to 0 or 1 depending on the winning player, in case of a tie = None.
        count - the game score, depending on the winning player, it is incremented"""
        self.players = [name_1, name_2]
        self.stroke = 0
        self.field = np.array([[0] * 3 for i in range(3)])
        self.win = None
        self.count = [0, 0]

    def restart(self):
        """When you restart the game for the same players, you need to reset the game field,
        set again the first move X, "zero" the winner"""
        self.stroke = 0
        self.field = np.array([[0] * 3 for i in range(3)])
        self.win = None

    @staticmethod
    def cell_validity(row, col):
        """Row and column indices must be between 0 and 2"""
        if row not in list(range(3)):
            raise ValueError("Неверное значение строки")
        if col not in list(range(3)):
            raise ValueError("Неверное значение столбца")

    def cell_busy_validity(self, row, col):
        """The cell must be empty to make a move"""
        TicTacToe.cell_validity(row, col)
        if self.cell_is_busy(row, col):
            raise Exception("Ячейка занята")

    @staticmethod
    def player_validity(player):
        """Players in the whole program = 0 or 1"""
        if player not in [0, 1]:
            raise ValueError("Неверное значение игрока")

    def check_win(self, player):
        """A check to see if one of the players wins.
        Since, if there is X in a cell, in field this cell = 1,
        if it is O, then -1, then it is enough to check that at least one sum of numbers
        field by row, column, or diagonal was 3 or -3 depending on
        the player (playing for X or O), for whom the check is carried out"""
        TicTacToe.player_validity(player)

        flag = -3 if player else 3
        return any(self.field.sum(axis = 1) == flag) or \
        any(self.field.sum(axis = 0) == flag) or \
        np.diagonal(self.field).sum() == flag or \
        np.diagonal(np.fliplr(self.field)).sum() == flag

    @property
    def check_standoff(self):
        """Draw check function. If none of the players won,
        and the field is filled, then True will return - a draw"""
        return not self.check_win(0) and \
        not self.check_win(1) and \
        self.field_is_filled

    @property
    def field_is_filled(self):
        """Checking if the field is full. If you bring field (which consists of
        0 - if the cell is empty, 1 - if there is X, -1 - if there is O) to absolute values,
        then the filled cells will be equal to 1, empty - 0. As a result, True will be returned if
        all elements of the list will be equal to 1 - the field is filled"""
        return np.all(np.abs(self.field))

    @property
    def game_done(self):
        """The game will end if there is a draw (then win = None),
        if one of the players wins (check for each player's winnings,
        we write it to the winners (win = player) and change the game score (change_count (player)).
        The corresponding logs are written to the file."""
        if self.check_standoff:
            self.win = None
            logging.info("Партия между %s и %s закончилась ничьей. Счет %s:%s",
                *self.players, *self.count)
            return True
        for player in [0,1]:
            if self.check_win(player):
                self.win = player
                self.change_count(player)
                logging.info("Партия между %s и %s закончилась победой %s. Счет %s:%s",
                    *self.players, self.players[self.win], *self.count)
                return True
        return False

    def cell_is_busy(self, row, col):
        """Check if the cell is occupied. Will return the absolute value of the cell
        (for 1 (for X) and -1 (for O) = 1, for 0 = 0)"""
        TicTacToe.cell_validity(row, col)
        return bool(np.abs(self.field[row][col]))

    def do_stroke(self, player, row, col, clean_cell = None):
        """The function of making a move. Depending on the player, we put either 1 or -1
        to the specified cell. 1 corresponds to X, -1 corresponds to O.
        And we pass the move to the second player (stroke = not player).
        For minimax, the jail needs to be cleared, so if a flag is passed to a function,
        which indicates that the cell needs to be cleaned and not filled with X / O,
        a move is made with the establishment of 0 in the square of the field"""
        if clean_cell is not None:
            flag = 0
        else:
            TicTacToe.player_validity(player)
            self.cell_busy_validity(row, col)
            flag = -1 if player else 1
        self.field[row][col] = flag
        self.stroke = not player


    def change_count(self, player):
        """Account change function. For the corresponding player, increment the value in count"""
        TicTacToe.player_validity(player)
        self.count[player] += 1

    @property
    def empty_cell(self):
        """Function returning an array of indices of empty cells of the field"""
        empty = []
        for row in range(len(self.field)):
            for col in range(len(self.field[0])):
                if not self.field[row][col]:
                    empty.append([row, col])
        return empty

    @property
    def minimax(self):
        """AI function of the game XO, returns the score and the best move in an array of moves
        (random among the best). He must choose the move with the most points,
        when the AI plays for X, and the move with the lowest score when a person plays for X."""
        if self.check_win(1):
            return -10, [None, None]
        if self.check_standoff:
            return 0, [None, None]
        if self.check_win(0):
            return 10, [None, None]

        scores, moves = [], []
        best = 10 if self.stroke else -10

        for row, col in self.empty_cell:
            self.do_stroke(self.stroke, row, col)
            val, _ = self.minimax
            scores.append(val)
            moves.append([row, col])
            self.do_stroke(self.stroke, row, col, "clean")
            if self.stroke:
                best = min(scores)
            else:
                best = max(scores)

        return best, choice([mv for mv, sc in zip(moves, scores) if sc == best])
