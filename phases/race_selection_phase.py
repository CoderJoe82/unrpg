from constants import *
from data.text_data import WELCOME_MESSAGE
from menus.button import Button
from data.character.character_races import ALL_RACES
from phases.creation_phase_base import CreationPhaseBase

class RaceSelectionPhase(CreationPhaseBase):
    def __init__(self, game, character_creation_screen):
        super().__init__(game, character_creation_screen)

        #---- NOTE!!! NEXT TIME YOU DO SOMETHING LIKE THIS, CONSIDER THIS FROM THE START AND LAY IT OUT THIS WAY ***FIRST***

        #--- Configuration math---
        self.button_width = 180
        self.button_height = 60
        self.button_padding = 15
        self.button_x = SCREEN_WIDTH * 0.02

        self._calculate_positions()
        self._create_race_buttons()
        self._create_section_title()
        self._create_navigation_buttons()

    def _calculate_positions(self):
        number_of_buttons = len(ALL_RACES.keys())
        half_of_screen_height = SCREEN_HEIGHT / 2
        total_padding_between_buttons = self.button_padding * (number_of_buttons - 1)
        full_button_segment_height = (self.button_height * number_of_buttons) + total_padding_between_buttons
        half_point_of_button_segment_height = full_button_segment_height / 2
        self.button_y = (half_of_screen_height - half_point_of_button_segment_height)
        self.divider_line_starting_x = self.button_x + self.button_width + self.button_x
        self.divider_line_ending_x = self.divider_line_starting_x
        self.divider_line_starting_y = 0
        self.divider_line_ending_y = SCREEN_HEIGHT
        self.divider_line_2_starting_x = self.divider_line_starting_x
        self.divider_line_2_ending_x = SCREEN_WIDTH
        self.divider_line_2_starting_y = SCREEN_HEIGHT * 0.15
        self.divider_line_2_ending_y = self.divider_line_2_starting_y
        self.race_selection_header_width = SCREEN_WIDTH - self.divider_line_starting_x
        self.race_choice_rect_x_section_center = (self.race_selection_header_width / 2) + self.divider_line_starting_x

    def _create_section_title(self):
        self._add_phase_text(GAME_FONT_PATH, 55, "Choose Your Race!", COLOR_TEXT_DEFAULT, self.race_choice_rect_x_section_center, self.divider_line_2_starting_y / 2)
    
    def _create_race_buttons(self):
        button_font = pygame.font.Font(GAME_FONT_PATH, 20)
        current_y = self.button_y
        for key, value in ALL_RACES.items():
            race_data = value
            self._add_phase_buttons(
                Button(
                    x = self.button_x,
                    y = current_y,
                    width = self.button_width,
                    height = self.button_height,
                    text = race_data.character_race_name,
                    color = (70, 60, 55),
                    text_color = COLOR_TEXT_DEFAULT,
                    font = button_font
                )
            )
            current_y += self.button_height + self.button_padding

    def _create_navigation_buttons(self):
        button_texts = ["Confirm", "Go back"]
        button_font = pygame.font.Font(GAME_FONT_PATH, 25)
        button_width = 250
        button_height = 45
        button_y = SCREEN_HEIGHT * 0.9
        button_padding = 15
        half_of_race_section_width = self.race_choice_rect_x_section_center
        number_of_buttons = len(button_texts)
        full_width_of_buttons = (button_width * number_of_buttons) + ((number_of_buttons - 1) * button_padding)
        button_x = half_of_race_section_width - full_width_of_buttons / 2

        current_x = button_x
        for index, value in enumerate(button_texts):
            button_text = value
            self._add_phase_buttons(
                Button(
                    x = current_x,
                    y = button_y,
                    width = button_width,
                    height = button_height,
                    text = button_text,
                    color = (70, 60, 55),
                    text_color = COLOR_TEXT_DEFAULT,
                    font = button_font
                )
            )
            current_x += button_width + button_padding


    def draw(self):
        self._add_divider_lines(self.game.surface, (70, 60, 55), (self.divider_line_starting_x, self.divider_line_starting_y), (self.divider_line_ending_x, self.divider_line_ending_y), 3)
        self._add_divider_lines(self.game.surface, (70, 60, 55), (self.divider_line_2_starting_x,
        self.divider_line_2_starting_y), (self.divider_line_2_ending_x, self.divider_line_2_ending_y), 3)
       
        self.game.surface.blit(self.title_surface, self.title_rect)

        for button in self.buttons:
            button.draw(self.game.surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    print('YOOOOOOOOOOOOOOOOOOOOOO')