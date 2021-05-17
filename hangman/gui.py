"""This module is used to create a user interface"""
from time import sleep
from string import ascii_lowercase as ALPHABET
import pygame
import hangman


pygame.init()
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

FONT = "font.otf"
background = pygame.image.load('background.jpg')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 30

white = (255, 255, 255)
black = (0, 0, 0)
red = (176, 9, 9)

guessed_words = ["GUESSED WORDS:"]
ATTEMPTS = 6


def text_format(message, text_font, text_size, text_color):
    """This function converts the string to the specified format"""
    new_font = pygame.font.Font(text_font, text_size)
    new_text = new_font.render(message, 0, text_color)
    return new_text


def draw_hangman(step):
    """This function draws a person according to the number of misses"""
    mass = [1, 2, 3, 4, 5, 6]
    pygame.draw.line(screen, black, (1300, 30), (1300, 670), 30)
    pygame.draw.line(screen, black, (1000, 40), (1300, 40), 20)
    pygame.draw.line(screen, black, (950, 660), (1350, 660), 80)
    pygame.draw.line(screen, black, (1050, 35), (1050, 130), 10)

    if step in mass[:]:
        pygame.draw.circle(screen, red, (1050, 180), 50, 5)
    if step in mass[1:]:
        pygame.draw.ellipse(screen, red, (1020, 230, 60, 200), 10)
    if step in mass[2:]:
        pygame.draw.line(screen, red, (1025, 280), (970, 360), 5)
    if step in mass[3:]:
        pygame.draw.line(screen, red, (1075, 280), (1130, 360), 5)
    if step in mass[4:]:
        pygame.draw.line(screen, red, (1030, 400), (970, 480), 5)
    if step in mass[5:]:
        pygame.draw.line(screen, red, (1070, 400), (1130, 480), 5)
        pygame.draw.line(screen, red, (1030, 170), (1035, 170), 5)
        pygame.draw.line(screen, red, (1065, 170), (1070, 170), 5)
        pygame.draw.arc(screen, red, (1026, 190, 50, 30), 0, 3.14, 4)


def press_key(letters):
    """This function processes the pressed key when guessing the letter"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                input_letter = event.unicode
                input_letter = input_letter.lower()

                if event.key == pygame.K_ESCAPE:
                    main_menu()

                if len(input_letter) != 1:
                    print('Это не буква')
                elif input_letter in letters:
                    print('Вы уже пробовали эту букву. Выберите другую')
                elif input_letter not in ALPHABET:
                    print('Введите английскую букву')
                else:
                    return input_letter


def guessed_words_menu():
    """This function creates and fills out a form with
    a list of guessed words"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        pygame.display.set_caption("H A N G M A N")

        title = text_format("H A N G M A N", FONT, 90, black)
        guessed = text_format('++++++++++++++++++', FONT, 30, red)
        text_quit = text_format("< QUIT >", FONT, 75, white)

        title_rect = title.get_rect()
        guessed_rect = guessed.get_rect()
        quit_rect = text_quit.get_rect()

        screen.blit(title, (SCREEN_WIDTH // 2 - (title_rect[2] // 2), 80))
        for temp, item in enumerate(guessed_words):
            gue = text_format(item, FONT, 30, red)
            screen.blit(gue, (SCREEN_WIDTH // 2 - (guessed_rect[2] // 2),
                              200 + (temp + 1) * 30))
        screen.blit(text_quit, (SCREEN_WIDTH // 2 - (quit_rect[2] // 2), 500))

        pygame.display.update()
        clock.tick(FPS)


def window_game():
    """This function creates and fills out a form with
    the direct process of the game"""
    word = list(hangman.random_word(hangman.words))
    print(word)
    correct_letters_in_word = ['_'] * len(word)
    missed_letters_in_word = []

    while True:
        screen.blit(background, (0, 0))
        pygame.display.set_caption("H A N G M A N")

        title = text_format("H A N G M A N", FONT, 90, black)
        missing_letters = text_format('MISSED: ' +
                                      ' '.join(missed_letters_in_word),
                                      FONT, 50, red)
        current_word = text_format(' '.join(correct_letters_in_word),
                                   FONT, 90, black)

        title_rect = title.get_rect()
        word_rect = current_word.get_rect()
        missing_rect = missing_letters.get_rect()

        screen.blit(title, (SCREEN_WIDTH // 3 - (title_rect[2] // 2), 80))
        screen.blit(current_word, (SCREEN_WIDTH // 3 -
                                   (word_rect[2] // 2), 360))
        screen.blit(missing_letters, (SCREEN_WIDTH // 3 -
                                      (missing_rect[2] // 2), 490))

        draw_hangman(len(missed_letters_in_word))

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if hangman.word_is_guessed(correct_letters_in_word, word):
            if hangman.game_is_done(correct_letters_in_word, word,
                                    guessed_words):
                print(guessed_words)
                win_text = text_format('You won! This word is ' +
                                       ''.join(word), FONT, 40, red)
                win_rect = win_text.get_rect()
                screen.blit(win_text, (SCREEN_WIDTH // 3 -
                                       (win_rect[2] // 2), 200))
                pygame.display.update()
                clock.tick(FPS)
                sleep(2)
                main_menu()

        if hangman.attempts_ended(missed_letters_in_word, ATTEMPTS):
            over_text = text_format('Game over! This word is ' +
                                    ''.join(word), FONT, 40, red)
            over_rect = over_text.get_rect()
            screen.blit(over_text, (SCREEN_WIDTH // 3 -
                                    (over_rect[2] // 2), 200))
            pygame.display.update()
            clock.tick(FPS)
            sleep(2)
            main_menu()

        input_letter = press_key(correct_letters_in_word +
                                 missed_letters_in_word)
        if input_letter in word:
            correct_letters_in_word = \
                hangman.correct_letter(correct_letters_in_word,
                                       input_letter, word)
        else:
            missed_letters_in_word = \
                hangman.missed_letters(missed_letters_in_word, input_letter)


def main_menu():
    """This function creates and fills out a form with a main menu"""
    selected = "start"
    while True:
        screen.blit(background, (0, 0))
        pygame.display.set_caption("H A N G M A N")
        title = text_format("H A N G M A N", FONT, 90, black)

        if selected == "start":
            text_start = text_format("< START >", FONT, 75, white)
        else:
            text_start = text_format("START", FONT, 75, black)

        if selected == "guessed":
            text_guessed = text_format("< GUESSED WORDS >", FONT, 75, white)
        else:
            text_guessed = text_format("GUESSED WORDS", FONT, 75, black)

        if selected == "quit":
            text_quit = text_format("< QUIT >", FONT, 75, white)
        else:
            text_quit = text_format("QUIT", FONT, 75, black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        guessed_rect = text_guessed.get_rect()
        quit_rect = text_quit.get_rect()

        screen.blit(title, (SCREEN_WIDTH // 3 - (title_rect[2] // 2), 80))
        screen.blit(text_start, (SCREEN_WIDTH // 3 -
                                 (start_rect[2] // 2), 300))
        screen.blit(text_guessed, (SCREEN_WIDTH // 3 -
                                   (guessed_rect[2] // 2), 380))
        screen.blit(text_quit, (SCREEN_WIDTH // 3 - (quit_rect[2] // 2), 460))

        draw_hangman(ATTEMPTS)

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and (selected == "guessed" or
                                                 selected == "start"):
                    selected = "start"
                elif event.key == pygame.K_UP and (selected == "quit"):
                    selected = "guessed"
                elif event.key == pygame.K_DOWN and (selected == "guessed" or
                                                     selected == "quit"):
                    selected = "quit"
                elif event.key == pygame.K_DOWN and (selected == "start"):
                    selected = "guessed"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        window_game()
                    if selected == "guessed":
                        guessed_words_menu()
                    if selected == "quit":
                        pygame.quit()
                        quit()
