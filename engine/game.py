import pygame
from constants import *

class Game:
    # The CONSTRUCTOR method. This runs ONCE when we create a Game object.
    # Its job is to do all the one-time setup.
    def __init__(self):
        # Initialize all the Pygame modules we need. This is a mandatory first step.
        pygame.init()
        
        # Create the main game window (our 'canvas'). Store it in `self.surface`
        # so all methods in the class can access it.
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Set the title of the window that appears in the OS.
        # Note: We don't strictly need to store this in `self.caption`, but it's fine to.
        self.caption = pygame.display.set_caption("Unnamed RPG")
        
        # Create a Font object (our 'stamp') from the specified file and size.
        self.title_font = pygame.font.Font(GAME_FONT_PATH, 55)
        
        # Use the font 'stamp' to create a new Surface with the text rendered on it.
        # This is our 'stamped image'. It takes 3 arguments: (text, anti-aliasing, color).
        self.title_surface = self.title_font.render("Unnamed RPG", True, COLOR_TEXT_DEFAULT)
        
        # Get the rectangle that encloses the `title_surface`.
        # This `Rect` object holds the image's dimensions and its (x,y) position.
        # We then immediately position its `center` anchor point.
        self.title_rect = self.title_surface.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * .10))
        
        # This is the main on/off switch for our game loop.
        # It starts as True, and when we set it to False, the game ends.
        self.running = True

    # This method contains the main game loop. It's the 'engine' that runs over and over.
    def run_game(self):
        # As long as our on/off switch (`self.running`) is True, this loop will continue.
        while self.running:
            # --- EVENT HANDLING ---
            # The event queue. This `for` loop checks for all user input that has happened
            # since the last frame.
            for event in pygame.event.get():
                # If the user clicks the window's 'X' button...
                if event.type == pygame.QUIT:
                    # ...flip the on/off switch to False. The `while` loop will terminate.
                    self.running = False

            # --- DRAWING ---
            # Erase the previous frame by filling the entire screen with our background color.
            self.surface.fill(COLOR_BACKGROUND)
            
            # Draw the 'stamped image' (`self.title_surface`) onto our main 'canvas' (`self.surface`)
            # at the position defined by `self.title_rect`.
            self.surface.blit(self.title_surface, self.title_rect)
            
            # --- UPDATE DISPLAY ---
            # Update the full display. This takes everything we've drawn in memory and
            # shows it on the actual screen. This must happen last in the loop.
            pygame.display.flip()