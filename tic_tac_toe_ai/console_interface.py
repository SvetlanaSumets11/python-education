"""Этот модуль для консольного интерфейса игры крестики-нолики"""
import sys
from random import randint
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


def restart_game(obj, a_i):
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
        main_game(obj, a_i)

def user_stroke(obj):
    """Функция осуществления хода игроком-человеком. Человек вводит число 1-9,
    что соответствует ячейке поля, куда он хочет сделать ход, осуществляется ход,
    где автоматически право ходить следующим передается сопернику, отрисовуется новое
    состояние поля"""
    row, col = play_input(obj)
    obj.do_stroke(obj.stroke, row, col)
    draw_field(obj.field)

def ai_stroke(obj):
    """Функция осуществления хода компьютером. С minimax распаковуем индексы
    выбранной для хода клетки, если это не конец игры (выигрыш одного из игроков или ничья),
    то отображаем надпись про ход игрока Компьютер и делаем ход в выбранную клетку,
    отрисовуем новое состояние поля игры."""
    row, col = obj.minimax[1]
    if row is not None:
        print("Ход {} за {} в клетку: {}"\
            .format((obj.players[obj.stroke]).upper(),
                player[obj.stroke],
                row * 3 + col + 1))
        obj.do_stroke(obj.stroke, row, col)
        draw_field(obj.field)


def main_game(obj, a_i):
    """Функция самой игры. На каждом шаге отрисовуется поле. Пользователь вводит
    номер ячейки, что преобразовуется в координаты, выполняется ход. Цикл длится,
    пока game_done не приймет значение True (в случае, если наступит ничья, или
    выиграет один из игроков). Печатаем победителя/смс про ничью. И спрашиваем
    игрока, хочет ли он сыграть снова в том же составе.

    Если игра идет между двумя людьми, просто поочередно ход предоставляется
    каждому. Если с компьютером, то в зависимости от того, кто играет за Х (то есть
    делает первых ход)(кто играет за Х, программа выбирает случайным образом),
    меняется порядок хода."""
    draw_field(obj.field)
    while not obj.game_done:
        if a_i is None:
            user_stroke(obj)
        else:
            if obj.players[0] == "Компьютер":
                ai_stroke(obj)
                if not obj.check_win(0) and not obj.check_standoff:
                    user_stroke(obj)
            else:
                user_stroke(obj)
                ai_stroke(obj)

    if obj.win is not None:
        print(f"Победил игрок {obj.players[obj.win]}")
    else:
        print("Игра закончилась ничьей")

    restart_game(obj, a_i)


def play(a_i = None):
    """Функция начала игры.
    Если игра происходит между двумя игроками-людьми,
    просто вводятся имена, где пользователи сами могут решить, за кого хотят
    играть. Создается объект, и запускается игра.
    Если игра будет между человком и компьютером, тогда прежде мы случайно
    выбираем, кто будет играть за крестик, в зависимости от результата,
    передаем в обьект в правильном порядке имена игроков (имя игрока и "Компьютер").
    И запускаем игру"""
    if a_i is None:
        name_1 = input("Введите имя первого игрока (X): ")
        name_2 = input("Введите имя второго игрока (O): ")
        game = T.TicTacToe(name_1, name_2)
    else:
        if not randint(0, 1):
            name_1 = input("Введите имя игрока: ")
            game = T.TicTacToe(name_1, "Компьютер")
            print(f"Случайно выбрано, что за Х играет {name_1}")
        else:
            name_2 = input("Введите имя игрока: ")
            game = T.TicTacToe("Компьютер", name_2)
            print("Случайно выбрано, что за Х играет Компьютер")
    main_game(game, a_i)


def draw_menu():
    """Функция отрисовки меню. В виде таблички выводятся пункты меню"""
    point_menu = [["1 Играть >"],
                ["2 Играть с компьютером >"],
                ["3 Посмотреть лог побед >"],
                ["4 Очистить логи побед >"],
                ["5 Выход >"]]
    table = Texttable()
    for item in point_menu:
        table.add_row(item)
    print(table.draw())


def input_menu():
    """Функция выбора пункта меню. Пользователь должен вводить лишь цифры,
    цифры лишь от 1 до 5, в ином случае пункт меню не будет выбран,
    и программа попросит повторить попытку выбора,
    написав соответствующее смс об ошибке ввода"""
    while True:
        point = input("Выберите пункт меню (1 - 5): ")
        try:
            point = int(point)
        except TypeError:
            print("Введите число от 1 до 5")
            continue
        if point in list(range(1, 6)):
            return point - 1
        print("Введите число от 1 до 5")


def menu():
    """Обработка каждого пункта меню. Если пользователь выбрал
    Играть - запустится игра для двоих игроков-людей.
    Играть с компьютером - запустится игра между компьютером и человеком.
    Посмотреть лог побед - выведется содержимое файла (или смс, что файл пуст).
    Очистить логи побед - очистится файл с логами, и выведется соответствующее смс.
    Выход - выполнение скрипта завершится."""
    draw_menu()
    responce = input_menu()
    if responce == 0:
        play()
        menu()
    if responce == 1:
        play("ai")
        menu()
    if responce == 2:
        with open("tic_tac_toe.log", 'r') as file:
            data = file.read()
            if data != '':
                print(data)
            else:
                print("Файл пуст")
        menu()
    if responce == 3:
        with open("tic_tac_toe.log", 'w'):
            pass
        print("Файл с логами был очищен")
        menu()
    if responce == 4:
        sys.exit()
