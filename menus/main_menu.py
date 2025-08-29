import pygame
from constants import *
from menus.button import Button

class MainMenu:
    TITLE_TEXT = "Unnamed RPG"
    TITLE_FONT_SIZE = 55
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 60

    def __init__(self, game):
        self.game = game
        self._configure_menu_surface()

    def _configure_menu_surface(self):
        self.surface = pygame.Surface(self.game.surface.get_size())
        self.title_font = pygame.font.Font(GAME_FONT_PATH, self.TITLE_FONT_SIZE)
        self.title_surface = self.title_font.render(self.TITLE_TEXT, True, COLOR_TEXT_DEFAULT)
        self.title_rect = self.title_surface.get_rect(center = (self.surface.get_width() / 2, self.surface.get_height() * 0.25))

    def draw(self):
        self.surface.blit(self.title_surface, self.title_rect)

    def handle_event(self):
        pass