import pygame
from constants import *
from menus.button import Button
# from data.character.character_races import character_races as races


class CharacterCreationScreen:
    def __init__(self, game):
        """
        The constructor for the Character Creation Screen

        Args:
            game. The main game object. To where we'll change states on clicking and on clicking new game, the player moves on to the character creation screen.
        """
        self.game = game
        self.font = pygame.font.Font(GAME_FONT_PATH, 20)
        self.welcome_rect = pygame.Rect(
            50, 150, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200)
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

        self.current_phase = 0

        self._setup_welcome_phase()

    #--- Helper Functions ---
    def _create_phase_title(self, font, font_size, text, text_color, x, y):
        self.title_font = pygame.font.Font(font, font_size)
        self.title_surface = self.title_font.render(text, True, text_color)
        self.title_rect = self.title_surface.get_rect(center=(x, y))

    def _create_phase_buttons(self, button_data):
        for index, button in enumerate(button_data):
            self.buttons.append(
                Button(
                    x=button['x'],
                    y=button['y'],
                    width=button['width'],
                    height=button['height'],
                    text=button['text'],
                    color=button['color'],
                    text_color=button['text_color'],
                    font=button['font']
                )
            )

    def _create_lines(self, surface, color, x_and_y_start, x_and_y_end, pixel_width):
        pygame.draw.line(surface, color, x_and_y_start, x_and_y_end, pixel_width)

    #--- Main draw functions ---
    def draw(self):
        if self.current_phase == 0:
            self.draw_welcome_phase()
        elif self.current_phase == 1:
            self.draw_race_selection_phase()

    def draw_welcome_phase(self):
        self.game.surface.blit(self.title_surface, self.title_rect)

        draw_multi_line_colored_text(
            self.game.surface,
            self.welcome_text_segments,
            self.welcome_rect,
            self.font
        )

        for button in self.buttons:
            button.draw(self.game.surface)

    def draw_race_selection_phase(self):
        self._create_lines(self.game.surface, (70, 60, 55), (self.divider_line_starting_x, self.divider_line_starting_y), (self.divider_line_ending_x, self.divider_line_ending_y), 3)

        self._create_lines(self.game.surface, (70, 60, 55), (self.divider_line_2_starting_x,
                         self.divider_line_2_starting_y), (self.divider_line_2_ending_x, self.divider_line_2_ending_y), 3)
       
        self.game.surface.blit(self.title_surface, self.title_rect)

        for button in self.buttons:
            button.draw(self.game.surface)

    #--- Main phase setup functions ---
    def _setup_welcome_phase(self):
        self.buttons = []

        self._create_phase_title(GAME_FONT_PATH, 55, "Welcome!", COLOR_TEXT_DEFAULT, (SCREEN_WIDTH /  2), (SCREEN_HEIGHT * .10))

        button_width = 250
        button_height = 60

        button_y = SCREEN_HEIGHT * 0.75

        button_x_create_character = ((SCREEN_WIDTH / 2) - button_width - 50)
        button_x_go_back_to_main_screen = (
            button_x_create_character + button_width + 50)

        button_font = pygame.font.Font(GAME_FONT_PATH, 30)

        self._create_phase_buttons(
            [
                {
                    'x' : button_x_create_character,
                    'y' : button_y,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Create Character",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                {
                    'x' : button_x_go_back_to_main_screen,
                    'y' : button_y,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : 'Go Back',
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                }
            ]
        )


    def _setup_race_selection_phase(self):
        self.buttons = []

        button_width = 180
        button_height = 60
        button_padding = 15

        button_x = SCREEN_WIDTH * 0.02

        half_of_screen_height = SCREEN_HEIGHT / 2
        number_of_buttons = 6
        total_padding_between_buttons = button_padding * \
            (number_of_buttons - 1)
        full_button_segment_height = (
            button_height * number_of_buttons) + total_padding_between_buttons
        half_point_of_button_segment_height = full_button_segment_height / 2

        self.divider_line_starting_x = button_x + button_width + button_x
        self.divider_line_ending_x = self.divider_line_starting_x
        self.divider_line_starting_y = 0
        self.divider_line_ending_y = SCREEN_HEIGHT

        self.divider_line_2_starting_x = self.divider_line_starting_x
        self.divider_line_2_ending_x = SCREEN_WIDTH
        self.divider_line_2_starting_y = SCREEN_HEIGHT * 0.15
        self.divider_line_2_ending_y = self.divider_line_2_starting_y

        race_selection_header_width = SCREEN_WIDTH - self.divider_line_starting_x
        race_choice_rect_x_section_center = (
            race_selection_header_width / 2) + self.divider_line_starting_x
        
        self._create_phase_title(GAME_FONT_PATH, 55, "Choose Your Race!", COLOR_TEXT_DEFAULT, race_choice_rect_x_section_center, self.divider_line_2_starting_y / 2)
        
        #--- Temp: Just testing to see the size of the square I'm going to put text in
        self.race_data_section_box_padding = SCREEN_WIDTH * 0.02
        self.race_data_section_box_x = self.divider_line_starting_x + \
            self.race_data_section_box_padding
        self.race_data_section_box_y = self.divider_line_2_starting_y + \
            self.race_data_section_box_padding
        self.race_data_section_box_width = 50
        self.race_data_section_box_height = 50
        #------------------------------------------

        button_x = SCREEN_WIDTH * 0.02
        button_y = (half_of_screen_height -
                    half_point_of_button_segment_height)
        button_y_race_2 = button_y + button_height + button_padding
        button_y_race_3 = button_y_race_2 + button_height + button_padding
        button_y_race_4 = button_y_race_3 + button_height + button_padding
        button_y_race_5 = button_y_race_4 + button_height + button_padding
        button_y_race_6 = button_y_race_5 + button_height + button_padding

        button_font = pygame.font.Font(GAME_FONT_PATH, 20)

        self._create_phase_buttons(
            [
                {
                    'x' : button_x,
                    'y' : button_y,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : 'Human',
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                {
                    'x' : button_x,
                    'y' : button_y_race_2,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Sylvan Elf",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                {
                    'x' : button_x,
                    'y' : button_y_race_3,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Stoneheart Dwarf",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                {
                    'x' : button_x,
                    'y' : button_y_race_4,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Verdant",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                                {
                    'x' : button_x,
                    'y' : button_y_race_5,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Geodekin",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
                                {
                    'x' : button_x,
                    'y' : button_y_race_6,
                    'width' : button_width,
                    'height' : button_height,
                    'text' : "Kithrin",
                    'color' : (70, 60, 55),
                    'text_color' : COLOR_TEXT_DEFAULT,
                    'font' : button_font
                },
            ]
        )

        self.divider_line_starting_x = button_x + button_width + button_x
        self.divider_line_ending_x = self.divider_line_starting_x
        self.divider_line_starting_y = 0
        self.divider_line_ending_y = SCREEN_HEIGHT
    
    #--- Event Handler---
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "Go Back":
                        self.game.current_state = self.game.main_menu
                    elif button.text == "Create Character":
                        self._setup_race_selection_phase()
                        self.current_phase = 1
