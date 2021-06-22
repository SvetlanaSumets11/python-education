"""This module is designed to ensure the viability of the tic-tac-toe game by
connecting the functions of the two modules - the game and the visual interface"""
import sys
from tic_tac_toe import TicTacToe
from view import View
import numpy as np


class Controller:
    """This is the main class of the module - controller.
    Provides interaction between the visual and game module"""

    def __init__(self):
        self.view = View()
        self.mask = {0: ' ', 1: 'X', -1: 'O'}
        self.a_i = None
        self.game = None
        self.player = {0: 'X', 1: 'O'}


    def mask_field(self, field):
        """We put a mask on the field of the game, all 0s will become empty lines,
        all cells with 1 become X, all cells with -1 become O"""
        return np.array([[self.mask[cell] for cell in row] for row in field])


    def user_stroke(self):
        """We put a mask on the playing field for display. The function of
        the visualization is passed functions-handlers of events of clicking
        on the buttons as parameters and SMS about the status of the move
        (in the case of a game between people)."""
        new_field = self.mask_field(self.game.field)
        status = None
        if self.a_i is None:
            status = "Ход {} за {}"\
                    .format((self.game.players[self.game.stroke]).upper(),
                    self.player[self.game.stroke])
        self.view.field_click(self.click_cell, self.back_to_menu, new_field, status)
        self.view.basis.mainloop()


    def ai_stroke(self):
        """Computer stroke function"""
        row, col = self.game.minimax[1]
        self.game.do_stroke(self.game.stroke, row, col)


    def restart_game(self):
        """The function to start the game again, the required fields
        are canceled and the user's turn is started"""
        def restart():
            self.game.restart()
            self.user_stroke()
        return restart


    def window_with_sms(self, text, restart = None):
        """Function for displaying text messages on forms. In the visualization module,
        in the corresponding function, the functions-handlers for pressing the button
        and the text SMS itself are passed to display"""
        if restart is not None:
            self.view.text_message(text, self.back_to_menu, self.restart_game)
            self.view.basis.mainloop()
        self.view.text_message(text, self.back_to_menu)
        self.view.basis.mainloop()


    def end_game(self):
        """If the game ends (a draw or one of the players wins), a text SMS appears
        in the form of a player's victory or the end of the game in a draw"""
        if self.game.win is not None:
            self.window_with_sms(f"Победил игрок {self.game.players[self.game.win]}", "restart")
        else:
            self.window_with_sms("Игра закончилась ничьей", "restart")
        self.view.button_menu(self.click_menu)
        self.view.basis.mainloop()


    def click_cell(self, row, col):
        """The function of processing clicks on the playing field - cell buttons.
        Either the players take turns, where the status of the move's ownership changes
        inside the game mechanism, or in the case of a game with a computer, the player
        and the machine move in turns"""
        def click_action():
            self.game.do_stroke(self.game.stroke, row, col)

            if not self.game.game_done:
                if self.a_i is not None:
                    self.ai_stroke()
                    if not self.game.check_win(1) and not self.game.check_standoff:
                        self.user_stroke()
                else:
                    self.user_stroke()

            if self.game.game_done:
                self.end_game()

        return click_action


    def back_to_menu(self):
        """Back to main menu function"""
        return self.main()


    def get_name(self, name_1, name_2):
        """The function of initializing the object of the game class,
        the entered names of the players are passed"""
        def input_name():
            if name_2 == self.a_i:
                self.game = TicTacToe(name_1.get(), self.a_i)
                self.user_stroke()
            else:
                self.game = TicTacToe(name_1.get(), name_2.get())
                self.user_stroke()
        return input_name


    def click_menu(self, row):
        """Processing of each menu item. If the user chose
        Play - starts a game for two human players.
        Play with a computer - a game between a computer and a human will start.
        View the victory log - the contents of the file will be displayed
        (or sms that the file is empty).
        Clear victory logs - the file with the logs will be cleared,
        and the corresponding SMS will be displayed.
        Exit - script execution will end."""
        if row == 0:
            self.a_i = None
            self.view.mess_box_for_name(self.get_name, self.a_i)
        if row == 1:
            self.a_i = "Компьютер"
            self.view.mess_box_for_name(self.get_name, self.a_i)
        if row == 2:
            with open("tic_tac_toe.log", 'r') as file:
                data = file.read()
                if data != '':
                    self.window_with_sms(data)
                else:
                    self.window_with_sms("Файл пуст")
        if row == 3:
            with open("tic_tac_toe.log", 'w'):
                pass
            self.window_with_sms("Файл с логами был очищен")
        if row == 4:
            sys.exit()


    def main(self):
        """Main menu call function"""
        self.view.button_menu(self.click_menu)
        self.view.basis.mainloop()
