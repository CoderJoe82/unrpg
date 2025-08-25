import pygame

class CreationPhaseBase:
    def __init__(self, game, character_creation_screen):
        self.game = game
        self.manager = character_creation_screen
        self.buttons = []

    def _add_phase_text(self, font, font_size, text, text_color, x, y):
        self.title_font = pygame.font.Font(font, font_size)
        self.title_surface = self.title_font.render(text, True, text_color)
        self.title_rect = self.title_surface.get_rect(center=(x, y))

    def _add_phase_buttons(self, button_data):
        self.buttons.append(button_data)

    def _add_divider_lines(self, surface, color, x_and_y_start, x_and_y_end, pixel_width):
        pygame.draw.line(surface, color, x_and_y_start, x_and_y_end, pixel_width)
    
    def draw(self):
        pass

    def handle_event(self):
        pass