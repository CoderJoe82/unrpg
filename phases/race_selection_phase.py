from constants import *
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
        
        self._get_race_data()
        self._calculate_positions()
        self._create_race_buttons()
        self._create_section_title()
        self._create_navigation_buttons()
        self.selected_race = None


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

        self.race_data_box_starting_x = self.divider_line_2_starting_x + (SCREEN_WIDTH * 0.03)
        self.race_data_box_starting_y = self.divider_line_2_starting_y + (SCREEN_HEIGHT * 0.04)

    def _create_section_title(self):
        self.title_surface, self.title_rect = self._add_phase_text(GAME_FONT_PATH, 55, "Choose Your Race!", COLOR_TEXT_DEFAULT, self.race_choice_rect_x_section_center, self.divider_line_2_starting_y / 2, "center")
    
    def _create_race_buttons(self):
        button_font = pygame.font.Font(GAME_FONT_PATH, 20)
        current_y = self.button_y
        for key, value in ALL_RACES.items():
            race_key = key
            race_data = value
            self._add_phase_buttons(
                Button(
                    x = self.button_x,
                    y = current_y,
                    width = self.button_width,
                    height = self.button_height,
                    display_text = race_data.character_race_name,
                    key_text = race_key,
                    color = (70, 60, 55),
                    text_color = COLOR_TEXT_DEFAULT,
                    font = button_font
                )
            )
            current_y += self.button_height + self.button_padding

    def _get_race_data(self):
        self.race_data = {}
        for key, value in ALL_RACES.items():
            race_name = key
            race_data = value
            self.race_data[race_name] = {
                'name' : race_data.character_race_name,
                'description' : race_data.character_race_description,
                'racial_abilities' : race_data.character_race_racial_abilities,
                'size' : race_data.character_race_size,
                'movement_speed' : race_data.character_race_size,
                'languages' : race_data.character_race_languages,
                'resistance_bonuses' : race_data.character_race_resistance_bonuses,
                'general_alignment' : race_data.character_race_general_alignment,
                'life_span' : race_data.character_race_life_span,
                'racial_traits' : race_data.character_race_racial_traits
            }
        

    def _create_racial_data_area(self, race_display_name):
        box_x = self.race_data_box_starting_x
        box_y = self.race_data_box_starting_y

        self.race_data_surface, self.race_header_rect = self._add_phase_text(GAME_FONT_PATH, 30, race_display_name, COLOR_CHOICE, box_x, box_y)

        header_underline_starting_y = box_y + self.race_header_rect.height
        header_underline_ending_y = header_underline_starting_y
        header_underline_ending_x = box_x + self.race_header_rect.width
        self.race_header_underline = self._add_divider_lines(self.game.surface, COLOR_CHOICE, (box_x, header_underline_starting_y), (header_underline_ending_x, header_underline_ending_y), 2)

        header_race_subheader_x = box_x
        header_race_subheader_y = header_underline_ending_y + 10
        self.header_race_subheader_surface, self.header_race_subheader_rect = self._add_phase_text(GAME_FONT_PATH, 22, "Description:", COLOR_CHOICE, header_race_subheader_x, header_race_subheader_y)

        chosen_race_description_x = box_x
        self.chosen_race_description_y = self.header_race_subheader_rect.bottom + 5
        self.race_description_string = f"• {self.race_data[self.selected_race]['description']}"
        self.font = pygame.font.Font(GAME_FONT_PATH, 22)
        self.race_description_rect = pygame.Rect(chosen_race_description_x, self.chosen_race_description_y, SCREEN_WIDTH - box_x - 10, 150)

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
                    display_text = button_text,
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

        if self.selected_race is not None:
            self._create_racial_data_area(f"{self.race_data[self.selected_race]['name']}:")
            self.description_box_bottom = draw_multi_line_colored_text(self.game.surface, [(self.race_description_string, COLOR_CHOICE)], self.race_description_rect, self.font)
            self.race_description_rect_bottom_y = self.description_box_bottom
            self.race_description_rect_height = self.race_description_rect_bottom_y - self.chosen_race_description_y
            self.game.surface.blit(self.race_data_surface, self.race_header_rect)
            self.game.surface.blit(self.header_race_subheader_surface, self.header_race_subheader_rect)
            # self.game.surface.blit(self.chosen_race_desciprtion_surface, self.chosen_race_description_rect)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    self.selected_race = button.key_text