import pygame

class Button:
    def __init__(self, x, y, width, height, text, font_size, callback, button_base_color = (70, 70, 70), button_hover_color = (150, 150, 150), button_text_color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.callback = callback
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.button_base_color = button_base_color
        self.button_hover_color = button_hover_color
        self.button_text_color = button_text_color

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handle_click(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.callback()

    def render(self, screen, mouse_pos):
        color = self.button_hover_color if self.is_hovered(mouse_pos) else self.button_base_color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, self.button_text_color)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)