from constants import *
import pygame

class Button():
    def __init__(self, x, y, width, height, text, color, text_color, font):
        # --- 1. The Main Button Box ---
        # We create the main rectangle for the button's background.
        self.rect = pygame.Rect(x, y, width, height)

        self.text = text
        # --- 2. The Colors & Font (Simple for now) ---
        self.color = color # A simple grey
        self.text_color = text_color # White
        # We create the font object ONCE right here.
        self.font = font

        # --- 3. The Text Image (The "Nameplate") ---
        # We create the IMAGE of the text just ONCE.
        self.text_surface = self.font.render(text, True, self.text_color)
        
        # We get the rectangle for the text image.
        self.text_rect = self.text_surface.get_rect()

        # And now we position the text's rectangle to be perfectly
        # centered inside our main button rectangle.
        self.text_rect.center = self.rect.center

    def draw(self, surface):
        # --- This method is very simple, it just draws the prepared parts ---

        # 1. Draw the main background rectangle onto the screen.
        pygame.draw.rect(surface, self.color, self.rect)

        # 2. Draw the text image on top of the background.
        surface.blit(self.text_surface, self.text_rect)