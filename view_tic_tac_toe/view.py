"""This module is used to implement the functions of drawing
the forms necessary for the game tic-tac-toe."""
from tkinter import Tk, Button, StringVar, Label, Entry


class View:
    """This is a class that stores methods for drawing forms, displaying text on forms,
    creating buttons - a visual user interface for playing tic-tac-toe"""
    def __init__(self):
        self.basis = Tk()
        self.basis.title('Tic_tac_toe')
        self.field = []
        self.text = ['Новая игра', 'Игра с ботом', 'Логи побед', 'Очистка логов', 'Выход']


    def clear(self):
        """Form cleaning function"""
        basis_mass = self.basis.grid_slaves()
        for row in basis_mass:
            row.destroy()


    def mess_box_for_name(self, function, a_i):
        """The function of drawing two input fields with an SMS next to it.
        The form has a button to confirm the entered text. The user (or users in
        the case of a game between people) enters his name, clicks on a button -
        as a result, the game starts"""
        self.clear()

        message_1 = StringVar()
        message_entry_1 = Label(text="Введите имя игрока Х: ", font=('Verdana', 15, 'bold'))
        message_entry_1.grid(row=0, column=0, sticky="w")

        message_entry_1 = Entry(textvariable=message_1)
        message_entry_1.grid(row=0,column=1, padx=5, pady=5)

        if a_i is None:
            message_2 = StringVar()
            message_entry_2 = Label(text="Введите имя игрока О: ", font=('Verdana', 15, 'bold'))
            message_entry_2.grid(row=1, column=0, sticky="w")

            message_entry_2 = Entry(textvariable=message_2)
            message_entry_2.grid(row=1,column=1, padx=5, pady=5)

            message_button = Button(text="Начать игру",
                                    font=('Verdana', 15, 'bold'),
                                    command=function(message_1, message_2))
            message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")

        else:
            message_button = Button(text="Начать игру",
                                    font=('Verdana', 20, 'bold'),
                                    command=function(message_1, "Компьютер"))
            message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")


    def field_click(self, function, exit_game, field, status):
        """Function for processing clicks on the field of play. The occupied cells
        will be inactive. When you press the button, a move will be made and the field
        will be redrawn. Likewise when the computer is running. In the case of a game between
        people, there will be an SMS about the state of the move under the main field. At the
        bottom there is a button to exit the game, it will return the user to the main menu"""
        self.clear()

        for row in range(3):
            line = []
            for col in range(3):
                button = Button(self.basis, text=field[row][col], width=6, height=3,
                                    font=('Verdana', 20, 'bold'),
                                    background='lavender',
                                    command= function(row, col))
                if field[row][col] != ' ':
                    button['state'] = 'disabled'
                button.grid(row=row, column=col, sticky='nsew')
                line.append(button)
            self.field.append(line)

        if status is not None:
            message = Label(text=status, font=('Verdana', 15, 'bold'))
            message.grid(row=3, column=0, columnspan=3, sticky='nsew')

        new_button = Button(self.basis, text='Выход',
                            font=('Verdana', 20, 'bold'), command=exit_game)
        new_button.grid(row=4, column=0, columnspan=3, sticky='nsew')


    def button_menu(self, function):
        """The function of drawing menu buttons and processing of clicks on them."""
        self.clear()
        line = []
        for row in range(5):
            button = Button(self.basis, text=self.text[row], width=15, height=2,
                    font=('Verdana', 20, 'bold'),
                    background='lavender',
                    command=lambda row=row: function(row))
            button.grid(row=row, sticky='nsew')
            line.append(button)
            self.field.append(line)


    def text_message(self, mess_text, exit_game, function = None):
        """Form design function with displayed SMS. Buttons are accessible
        - one or two for different occasions"""
        self.clear()

        message = Label(text=mess_text, font=('Verdana', 15, 'bold'))
        message.grid(row=1, column=0, sticky="w")

        message_button = Button(text="В меню",
                                font=('Verdana', 15, 'bold'),
                                command=exit_game)
        message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")

        if function is not None:
            restart = Button(text="Сыграть снова",
                                font=('Verdana', 15, 'bold'),
                                command=function())
            restart.grid(row=3,column=1, padx=5, pady=5, sticky="e")
