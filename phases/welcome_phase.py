from constants import *
from data.text_data import WELCOME_MESSAGE
from menus.button import Button
from phases.creation_phase_base import CreationPhaseBase

class WelcomePhase(CreationPhaseBase):
    def __init__(self, game, character_creation_screen):
        super().__init__(game, character_creation_screen)

        self._create_phase_title(GAME_FONT_PATH, 55, "Welcome!", COLOR_TEXT_DEFAULT, (SCREEN_WIDTH /  2), (SCREEN_HEIGHT * .10))

        self. welcome_text_segments = WELCOME_MESSAGE
        self.font = pygame.font.Font(GAME_FONT_PATH, 20)
        self.welcome_rect = pygame.Rect(50, 150, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200)

        button_width = 250
        button_height = 60

        button_y = SCREEN_HEIGHT * 0.75

        button_x_create_character = ((SCREEN_WIDTH / 2) - button_width - 50)
        button_x_go_back_to_main_screen = (
            button_x_create_character + button_width + 50)

        button_font = pygame.font.Font(GAME_FONT_PATH, 30)

        button_names = ["Create Character", "Go Back"]

        current_x = button_x_create_character
        for index, value in enumerate(button_names):
            self._create_phase_buttons_test(
                Button(
                    x = current_x,
                    y = button_y,
                    width = button_width,
                    height = button_height,
                    text = value,
                    color = (70, 60, 55),
                    text_color = COLOR_TEXT_DEFAULT,
                    font = button_font
                )
            )
            current_x += button_width + 50

    def draw(self):
        self.game.surface.blit(self.title_surface, self.title_rect)

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
                    elif button.text == "Create Character":
                        self.manager._setup_race_selection_phase()