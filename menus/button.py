from constants import *
import pygame

class Button():
    def __init__(self, x, y, width, height, display_text, color, text_color, font, key_text = "default"):
        self.rect = pygame.Rect(x, y, width, height)
        self.display_text = display_text
        self.key_text = key_text
        self.color = color
        self.text_color = text_color
        self.font = font
        self.text_surface = self.font.render(display_text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text_surface, self.text_rect)