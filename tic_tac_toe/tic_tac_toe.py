"""Это основной модуль игры крестики-нолики"""
import logging
import numpy as np

logging.basicConfig(filename="tic_tac_toe.log", \
    level=logging.INFO, format="%(message)s - %(asctime)s", datefmt='%d-%b-%y %H:%M:%S')


class TicTacToe:
    """Это класс основных функций игры"""
    def __init__(self, name_1, name_2):
        """Инициализация полей. Игроки хранятся в виде списка имен players.
        stroke - переменная хода, есть указан 0, то ход Х, если 1, то ход О.
        field - поле игры, состоящее из 0; если ставится Х, ячейка = 1, если О, то -1.
        win - равна 0 или 1 в зависимости от игрока-победителя, в случае ничьи = None.
        count - счет игры, в зависимости от игрока-победителя икрементируется"""
        self.players = [name_1, name_2]
        self.stroke = 0
        self.field = np.array([[0] * 3 for i in range(3)])
        self.win = None
        self.count = [0, 0]

    def restart(self):
        """При повторном запуске игры для тех же игроков нужно обнулить поле игры,
        установить снова первый ход Х, "обнулить" победителя"""
        self.stroke = 0
        self.field = np.array([[0] * 3 for i in range(3)])
        self.win = None

    @staticmethod
    def cell_validity(row, col):
        """Индексы строки и столбца должны быть от 0 до 2"""
        if row not in list(range(3)):
            raise ValueError("Неверное значение строки")
        if col not in list(range(3)):
            raise ValueError("Неверное значение столбца")

    def cell_busy_validity(self, row, col):
        """Ячейка должна быть пуста для осуществления хода"""
        TicTacToe.cell_validity(row, col)
        if self.cell_is_busy(row, col):
            raise Exception("Ячейка занята")

    @staticmethod
    def player_validity(player):
        """Игроки во всей программе = 0 или 1"""
        if player not in [0, 1]:
            raise ValueError("Неверное значение игрока")

    def check_win(self, player):
        """Проверка на победу одного из игроков.
        Поскольку, если в ячейке стоит Х, в field эта ячейка = 1,
        если стоит О, то -1, то достаточно проверить, чтоб хотя бы одна сумма чисел
        field по строкам, столбцам или диагоналям была равна 3 или -3 в зависимости от
        игрока (играющего за Х или О), для которого осуществляется проверка"""
        TicTacToe.player_validity(player)

        flag = -3 if player else 3
        return any(self.field.sum(axis = 1) == flag) or \
        any(self.field.sum(axis = 0) == flag) or \
        np.diagonal(self.field).sum() == flag or \
        np.diagonal(np.fliplr(self.field)).sum() == flag

    @property
    def check_standoff(self):
        """Функция проверки на ничью. Если ни один из игроков не выиграл,
        и поле заполнено, то вернется True - ничья"""
        return not self.check_win(0) and \
        not self.check_win(1) and \
        self.field_is_filled

    @property
    def field_is_filled(self):
        """Проверка на заполненность поля. Если привести field (что состоит из
        0 - если ячейка пустая, 1 - если стоит Х, -1 - если стоит О) к абсолютным значениям,
        тогда заполненные клетки будут равны 1, пустые - 0. В итоге вернется True, если
        все элементы списка будут равны 1 - поле заполнено"""
        return np.all(np.abs(self.field))

    @property
    def game_done(self):
        """Игра завершится, если будет ничья (тогда win = None),
        если один из игроков выиграет (проверяем на выигрыш каждого игрока,
        записываем его в победители (win = player) и меняем счет игры (change_count(player)).
        В файл записываются соответствующие логи."""
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
        """Проверка на занятость клетки. Вернется абсотлютное значение ячейки
        (при 1(для Х) и -1(для О) = 1, при 0 = 0)"""
        TicTacToe.cell_validity(row, col)
        return bool(np.abs(self.field[row][col]))

    def do_stroke(self, player, row, col):
        """Функция осуществления хода. В зависимости от игрока, ставим либо 1, либо -1
        в указанную ячейку. 1 соответствует Х, -1 соответствует О.
        И передаем ход второму игроку (stroke = not player)"""
        TicTacToe.player_validity(player)
        self.cell_busy_validity(row, col)

        flag = -1 if player else 1
        self.field[row][col] = flag
        self.stroke = not player

    def change_count(self, player):
        """Функция смены счета. Для соответствующего игрока инкрементируем значение в count"""
        TicTacToe.player_validity(player)
        self.count[player] += 1
