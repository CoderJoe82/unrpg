import pygame
from src.core.scene import Scene
from src.utils import config
from src.ui.button import Button
from src.core.events import QuitEvent

class TitleScreen(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        self.raw_image = pygame.image.load(f"{config.IMAGES_DIR}/title_background_image.png")
        self.background = pygame.transform.scale(self.raw_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.button_data = [
            ("Start Game", start_game),
            ("Load Game", load_game),
            ("Quit Game", quit_game)
        ]
        def start_game():
            print("Start Game Clicked!")
        def quit_game():
            self.events.post(QuitEvent())
        button_width = config.TITLE_BUTTON_WIDTH
        button_height = config.TITLE_BUTTON_HEIGHT
        button_x = (config.SCREEN_WIDTH // 2) - (button_width // 2)
        button_current_y = config.TITLE_SCREEN_STARTING_Y



        # def __init__(self, x, y, width, height, text, font_size, callback, button_base_color = (70, 70, 70), button_hover_color = (150, 150, 150), button_text_color = (255, 255, 255)):

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        font = pygame.font.Font(None, config.TITLE_FONT_SIZE)
        shadow = font.render("Untitled RPG", True, config.BLACK)
        shadow_x = (config.SCREEN_WIDTH // 2) - (shadow.get_width() // 2) + 4
        shadow_y = 100 + 4
        screen.blit(shadow, (shadow_x, shadow_y))
        title = font.render("Untitled RPG", True, config.PALE_GOLD)
        title_x = (config.SCREEN_WIDTH // 2) - (title.get_width() // 2)
        title_y = 100
        screen.blit(title, (title_x, title_y))
        pygame.display.flip()
