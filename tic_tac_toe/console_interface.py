"""Этот модуль для консольного интерфейса игры крестики-нолики"""
import sys
from texttable import Texttable
import numpy as np
import tic_tac_toe as T

mask = {0: ' ', 1: 'X', -1: 'O'}
player = {0: 'X', 1: 'O'}


def mask_field(field):
    """Накладываем маску на поле игры, все 0 станут пустыми строками,
    все ячейки с 1 станут Х, все ячейки с -1 станут О"""
    return np.array([[mask[cell] for cell in row] for row in field])


def draw_field(field):
    """Рисуем поле игры"""
    new_field = mask_field(field)
    table = Texttable()
    for item in range(3):
        table.add_row(new_field[item])
    print(table.draw())


def coor(num):
    """Пользователь пишет номер ячейки 1-9, что преобразовуется
    в координаты элемента списка поля"""
    return (num - 1) // 3, (num - 1) % 3


def play_input(obj):
    """Обработка осуществления хода пользователем. Он должен вводить
    лишь цифры, цифры лишь от 1 до 9, цифру лишь той ячейки, что свободна,
    в ином случае ход не будет засчитан, и программа попросит повторить попытку
    ввода номера ячейки, написав соответствующее смс об ошибке ввода"""
    while True:
        player_answer = input("Ход {} за {} в клетку: "\
            .format((obj.players[obj.stroke]).upper(), player[obj.stroke]))
        try:
            player_answer = int(player_answer)
        except TypeError:
            print("Введите число от 1 до 9")
            continue

        if player_answer in list(range(1, 10)):
            if not obj.cell_is_busy(coor(player_answer)[0], coor(player_answer)[1]):
                return coor(player_answer)[0], coor(player_answer)[1]
            print("Эта клетка уже занята")
        else:
            print("Введите число от 1 до 9")


def restart_game(obj):
    """После окончания игры у пользователя спрашивают, хочет ли он повторить
    поединок в том же составе, в зависимости от ответа, начнется либо новая игра,
    для которой "обнулятся" соответствующие поля, счет будет вестись для текущих игроков,
    либо программа выйдет в меню, а при повторном начале игры запросит заново имена игроков"""
    print("Хотите сыграть еще раз?")
    answer = input("N/Y: ")
    answer = answer.lower()
    if answer == "n":
        menu()
    if answer == "y":
        obj.restart()
        main_game(obj)


def main_game(obj):
    """Функция самой игры. На каждом шаге отрисовуется поле. Пользователь вводит
    номер ячейки, что преобразовуется в координаты, выполняется ход. Цикл длится,
    пока game_done не приймет значение True (в случае, если наступит ничья, или
    выиграет один из игроков). Печатаем победителя/смс про ничью. И спрашиваем
    игрока, хочет ли он сыграть снова в том же составе."""
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
    """Функция начала игры. Пользователь вводит имена игроков, создается
    обьект класса TicTacToe, запускается игра."""
    name_1 = input("Введите имя первого игрока (X): ")
    name_2 = input("Введите имя второго игрока (O): ")
    game = T.TicTacToe(name_1, name_2)
    main_game(game)


def draw_menu():
    """Функция отрисовки меню. В виде таблички выводятся пункты меню"""
    point_menu = [["1 Играть >"],
                ["2 Посмотреть лог побед >"],
                ["3 Очистить логи побед >"],
                ["4 Выход >"]]
    table = Texttable()
    for item in point_menu:
        table.add_row(item)
    print(table.draw())


def input_menu():
    """Функция выбора пункта меню. Пользователь должен вводить лишь цифры,
    цифры лишь от 1 до 4, в ином случае пункт меню не будет выбран,
    и программа попросит повторить попытку выбора,
    написав соответствующее смс об ошибке ввода"""
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
    """Обработка каждого пункта меню. Если пользователь выбрал
    Играть - запустится игра;
    Посмотреть лог побед - выведется содержимое файла (или смс, что файл пуст).
    Очистить логи побед - очистится файл с логами, и выведется соответствующее смс.
    Выход - выполнение скрипта завершится."""
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
