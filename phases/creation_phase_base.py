import pygame

class CreationPhaseBase:
    def __init__(self, game, character_creation_screen):
        self.game = game
        self.manager = character_creation_screen
        self.buttons = []

    def _add_phase_text(self, font, font_size, text, text_color, x, y, alignment = "topleft"):
        rect_font = pygame.font.Font(font, font_size)
        rect_surface = rect_font.render(text, True, text_color)
        rect = rect_surface.get_rect(**{alignment:(x, y)})
        return rect_surface, rect

    def _add_phase_buttons(self, button_data):
        self.buttons.append(button_data)

    def _add_divider_lines(self, surface, color, x_and_y_start, x_and_y_end, pixel_width):
        pygame.draw.line(surface, color, x_and_y_start, x_and_y_end, pixel_width)
    
    def draw(self):
        pass

    def handle_event(self):
        pass