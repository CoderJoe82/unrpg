from src.core.scene import Scene
import pygame

class TestScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

    def render(self, screen):
        screen.fill((20, 20, 60))
        pygame.display.flip()