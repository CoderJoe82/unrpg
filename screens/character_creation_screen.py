import pygame
from constants import *
from menus.button import Button


class CharacterCreationScreen:
    def __init__(self, game):
        """
        The constructor for the Character Creation Screen

        Args:
            game. The main game object. To where we'll change states on clicking and on clicking new game, the player moves on to the character creation screen.
        """
        self.game = game
        self.font = pygame.font.Font(GAME_FONT_PATH, 20)
        self.welcome_rect = pygame.Rect(50, 150, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200)
        self.welcome_text_segments = [
            ("Welcome to a world not of conquest, but of ", COLOR_TEXT_DEFAULT),
            ("confluence", COLOR_EMPHASIS),
            (", where the line between civilization and the wild has blurred into a ",
             COLOR_TEXT_DEFAULT),
            ("vibrant tapestry.", COLOR_NATURE),

            ("\n\nHere, cities are not built against the forest, but within it. Towers of stone are entwined with the ", COLOR_TEXT_DEFAULT),
            ("living wood of ancient trees", COLOR_NATURE),
            (", and rivers, once obstacles, now flow through the heart of communities as natural thoroughfares. Humanity has not tamed the wild; it has learned to live in harmony with its rhythms, and in turn, the wild has adapted, its ", COLOR_TEXT_DEFAULT),
            ("magic and mystery", COLOR_MAGIC),
            (" seeping into the very foundations of society.", COLOR_TEXT_DEFAULT),

            ("\n\nThis is a land shaped by more than just humans, elves, and dwarves. It is a world where you might share a path with the bark-skinned ", COLOR_TEXT_DEFAULT),
            ("Verdant", COLOR_NATURE),
            (" whose forms shift with the seasons, consult the ancient wisdom of the ",
             COLOR_TEXT_DEFAULT),
            ("crystalline Geodekin", COLOR_EMPHASIS),
            (", or witness the silent, unified construction of a ", COLOR_TEXT_DEFAULT),
            ("Kith'rin hive-city.", COLOR_EMPHASIS),

            ("\n\nThe ", COLOR_TEXT_DEFAULT),
            ("stories", COLOR_MAGIC),
            (" of this world are waiting to be written, and its greatest ",
             COLOR_TEXT_DEFAULT),
            ("legends", COLOR_MAGIC),
            (" are yet to be forged. The only question that remains is...",
             COLOR_TEXT_DEFAULT),

            ("\n\nwho will you be?", COLOR_CHOICE)
        ]

        self.buttons = []

        button_width = 250
        button_height = 60
        button_spacing = 20

        button_y = SCREEN_HEIGHT * 0.75

        button_x_create_character = ((SCREEN_WIDTH / 2) - button_width - 50)
        button_x_go_back_to_main_screen = (button_x_create_character + button_width + 50)

        button_font = pygame.font.Font(GAME_FONT_PATH, 30)

        create_character_button = Button(
            x = button_x_create_character,
            y = button_y,
            width = button_width,
            height = button_height,
            text = "Create Character",
            color = (70, 60, 55),
            text_color = COLOR_TEXT_DEFAULT,
            font = button_font
        )

        back_button = Button(
            x = button_x_go_back_to_main_screen,
            y = button_y,
            width = button_width,
            height = button_height,
            text = "Go Back",
            color = (70, 60, 55),
            text_color = COLOR_TEXT_DEFAULT,
            font = button_font
        )

        self.buttons.append(create_character_button)
        self.buttons.append(back_button)

    def draw(self):
        draw_multi_line_colored_text(
            self.game.surface,
            self.welcome_text_segments,
            self.welcome_rect,
            self.font
        )

        for button in self.buttons:
            button.draw(self.game.surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "Go Back":
                        self.game.current_state = self.game.main_menu