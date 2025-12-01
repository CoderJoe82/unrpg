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
        self.buttons = []
        def start_game():
            print("Start Game Clicked!")
        def load_game():
            print("Load Game Clicked!")
        def quit_game():
            self.events.post(QuitEvent())
        button_data = [
            ("Start Game", start_game),
            ("Load Game", load_game),
            ("Quit Game", quit_game)
        ]
        button_width = config.TITLE_BUTTON_WIDTH
        button_height = config.TITLE_BUTTON_HEIGHT
        button_x = (config.SCREEN_WIDTH // 2) - (button_width // 2)
        button_current_y = config.SCREEN_HEIGHT * config.TITLE_BUTTON_STARTING_Y

        for button_text, func in button_data:
            self.buttons.append(
                Button(
                    x = button_x,
                    y = button_current_y,
                    width = button_width,
                    height = button_height,
                    text = button_text,
                    font_size = config.TITLE_BUTTON_FONT_SIZE,
                    callback = func
                )
            )
            button_current_y += button_height + config.TITLE_BUTTON_PADDING

        self.events.subscribe("MouseClick", self.handle_click_event)

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
        
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.render(screen, mouse_pos)
        pygame.display.flip()

    def handle_click_event(self, event):
        for button in self.buttons:
            button.handle_click(event.pos)