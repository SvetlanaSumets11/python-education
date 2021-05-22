"""This module for the tic-tac-toe game console interface"""
import sys
from texttable import Texttable
import numpy as np
import tic_tac_toe as T

mask = {0: ' ', 1: 'X', -1: 'O'}
player = {0: 'X', 1: 'O'}


def mask_field(field):
    """We put a mask on the field of the game, all 0s will become empty lines,
    all cells with 1 become X, all cells with -1 become O"""
    return np.array([[mask[cell] for cell in row] for row in field])


def draw_field(field):
    """Draw the game field"""
    new_field = mask_field(field)
    for i, row in enumerate(new_field):
        for j, item in enumerate(row):
            if item == " ":
                new_field[i][j] = i * 3 + j + 1
    table = Texttable()
    for item in range(3):
        table.add_row(new_field[item])
    print(table.draw())


def coor(num):
    """User writes cell number 1-9, which is converted
    to the coordinates of the list item of the field"""
    return (num - 1) // 3, (num - 1) % 3


def play_input(obj):
    """Handling the execution of a move by the user. He must enter
    only numbers, numbers only from 1 to 9 or coordinates of the form 01, 02,
    the number of only the cell that is free, otherwise the move will not be counted,
    and the program will ask you to try again to enter the cell number,
    by writing an appropriate SMS about an input error"""
    while True:
        player_answer = input("Ход {} за {} в клетку: "\
            .format((obj.players[obj.stroke]).upper(), player[obj.stroke]))
        if len(player_answer) == 1:
            try:
                player_answer = int(player_answer)
            except TypeError:
                print("Введите число от 1 до 9 либо координату клетки (пример: 01)")
                continue
        else:
            if len(player_answer) != 2:
                print("Введите число от 1 до 9 либо координату клетки (пример: 01)")
                continue

        coord = [f"{i // 3}{i % 3}" for i in range(9)]
        if player_answer in list(range(1, 10)):
            if not obj.cell_is_busy(coor(player_answer)[0], coor(player_answer)[1]):
                return coor(player_answer)[0], coor(player_answer)[1]
            print("Эта клетка уже занята")

        elif player_answer in coord:
            answer = list(map(int, list(player_answer)))
            if not obj.cell_is_busy(answer[0], answer[1]):
                return answer[0], answer[1]
            print("Эта клетка уже занята")

        else:
            print("Введите число от 1 до 9 либо координату клетки (пример: 01)")


def restart_game(obj):
    """After the end of the game, the user is asked if he wants to repeat
    a duel in the same composition, depending on the answer, either a new game
    will start, for which the corresponding fields will be "reset", the score will
    be kept for the current players, or the program will exit to the menu, and upon
    restarting the game it will ask again for the names of the players"""
    print("Хотите сыграть еще раз?")
    answer = input("N/Y: ")
    answer = answer.lower()
    if answer == "n":
        menu()
    if answer == "y":
        obj.restart()
        main_game(obj)


def main_game(obj):
    """The function of the game itself. A field is drawn at each step. User enters
    the cell number that is converted to coordinates, the move is performed. The cycle lasts
    until game_done evaluates to True (in case of a tie, or
    one of the players wins). We print the winner / sms about the draw. And we ask
    player, whether he wants to play again with the same lineup."""
    draw_field(obj.field)
    while not obj.game_done:
        row, col = play_input(obj)
        obj.do_stroke(obj.stroke, row, col)
        draw_field(obj.field)

    if obj.win is not None:
        print(f"Победил игрок {obj.players[obj.win]}")
    else:
        print("Игра закончилась ничьей")

    restart_game(obj)


def play():
    """Game start function. User enters player names, is created
    object of class TicTacToe, the game starts."""
    name_1 = input("Введите имя первого игрока (X): ")
    name_2 = input("Введите имя второго игрока (O): ")
    game = T.TicTacToe(name_1, name_2)
    main_game(game)


def draw_menu():
    """Menu rendering function. Menu items are displayed in the form of a plate"""
    point_menu = [["1 Играть >"],
                ["2 Посмотреть лог побед >"],
                ["3 Очистить логи побед >"],
                ["4 Выход >"]]
    table = Texttable()
    for item in point_menu:
        table.add_row(item)
    print(table.draw())


def input_menu():
    """Menu item selection function. The user only needs to enter numbers,
    digits only from 1 to 4, otherwise the menu item will not be selected,
    and the program will ask you to try the selection again,
    by writing an appropriate SMS about an input error"""
    while True:
        point = input("Выберите пункт меню (1 - 4): ")
        try:
            point = int(point)
        except TypeError:
            print("Введите число от 1 до 4")
            continue
        if point in list(range(1, 5)):
            return point - 1
        print("Введите число от 1 до 4")


def menu():
    """Processing of each menu item. If the user chose
    Play - the game will start;
    View the victory log - the contents of the file will be displayed
    (or sms that the file is empty).
    Clear victory logs - the file with the logs will be cleared, and
    the corresponding SMS will be displayed.
    Exit - script execution will end."""
    draw_menu()
    responce = input_menu()
    if responce == 0:
        play()
        menu()
    if responce == 1:
        with open("tic_tac_toe.log", 'r') as file:
            data = file.read()
            if data != '':
                print(data)
            else:
                print("Файл пуст")
        menu()
    if responce == 2:
        with open("tic_tac_toe.log", 'w'):
            pass
        print("Файл с логами был очищен")
        menu()
    if responce == 3:
        sys.exit()
