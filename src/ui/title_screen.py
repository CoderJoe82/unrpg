import pygame
from src.core.scene import Scene

class TitleScreen(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self.raw_image = pygame.image.load("src/assets/images/title_background_image.png")
        self.background = pygame.transform.scale(self.raw_image, (1270, 720))

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()