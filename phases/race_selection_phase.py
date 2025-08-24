from constants import *
from data.text_data import WELCOME_MESSAGE
from menus.button import Button
from data.character.character_races import ALL_RACES
from phases.creation_phase_base import CreationPhaseBase

class RaceSelectionPhase(CreationPhaseBase):
    def __init__(self, game, character_creation_screen):
        super().__init__(game, character_creation_screen)

        button_width = 180
        button_height = 60
        button_padding = 15

        button_x = SCREEN_WIDTH * 0.02

        half_of_screen_height = SCREEN_HEIGHT / 2
        number_of_buttons = len(ALL_RACES.keys())
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

        button_font = pygame.font.Font(GAME_FONT_PATH, 20)
        
        current_y = button_y
        for key, value in ALL_RACES.items():
            race_data = value
            self._create_phase_buttons_test(
                Button(
                    x = button_x,
                    y = current_y,
                    width = button_width,
                    height = button_height,
                    text = race_data.character_race_name,
                    color = (70, 60, 55),
                    text_color = COLOR_TEXT_DEFAULT,
                    font = button_font
                )
            )
            current_y += button_height + button_padding

        self.divider_line_starting_x = button_x + button_width + button_x
        self.divider_line_ending_x = self.divider_line_starting_x
        self.divider_line_starting_y = 0
        self.divider_line_ending_y = SCREEN_HEIGHT

    def draw(self):
        self._create_lines(self.game.surface, (70, 60, 55), (self.divider_line_starting_x, self.divider_line_starting_y), (self.divider_line_ending_x, self.divider_line_ending_y), 3)
        self._create_lines(self.game.surface, (70, 60, 55), (self.divider_line_2_starting_x,
        self.divider_line_2_starting_y), (self.divider_line_2_ending_x, self.divider_line_2_ending_y), 3)
       
        self.game.surface.blit(self.title_surface, self.title_rect)

        for button in self.buttons:
            button.draw(self.game.surface)