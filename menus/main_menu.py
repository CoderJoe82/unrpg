import pygame
from constants import *
from menus.button import Button # We need to import our Button class

class MainMenu:
    def __init__(self, game):
        """
        The constructor for the MainMenu.
        
        Args:
            game (Game): The main game object, which holds shared resources
                         like the screen surface and fonts.
        """
        # --- 1. Store a reference to the main game object ---
        self.game = game

        # --- 2. Create a list to hold all our buttons ---
        self.buttons = []

        # --- 3. Define properties for our buttons ---
        # Let's make all buttons the same size
        button_width = 250
        button_height = 60
        
        # We want to center the buttons horizontally on the screen.
        # The x-coordinate of the top-left corner of a centered object is:
        # (SCREEN_WIDTH / 2) - (object_width / 2)
        button_x = (SCREEN_WIDTH / 2) - (button_width / 2)
        
        # Let's stack them vertically. We can start the first button
        # at 30% down the screen, and then place the next one below it.
        button_y_new_game = SCREEN_HEIGHT * 0.37
        button_y_load = button_y_new_game + button_height + 20
        button_y_quit = button_y_load + button_height + 20

        # --- 4. Create the "New Game" button ---
        # Remember the arguments for a Button:
        # x, y, width, height, text, color, text_color, font
        
        # We need a font. Let's create one here for the buttons.
        # It's better to create it once than inside the button class every time.
        button_font = pygame.font.Font(GAME_FONT_PATH, 30)

        new_game_button = Button(
            x = button_x, 
            y= button_y_new_game,
            width = button_width,
            height = button_height,
            text= "New Game",
            color = (70, 60, 55),          # A darker earthen color for the button
            text_color= COLOR_TEXT_DEFAULT,
            font= button_font
        )

        new_load_button = Button(
            x = button_x, 
            y= button_y_load,
            width = button_width,
            height = button_height,
            text= "Load Game",
            color = (70, 60, 55),          # A darker earthen color for the button
            text_color= COLOR_TEXT_DEFAULT,
            font= button_font
        )
        
        # --- 5. Create the "Quit" button ---
        quit_button = Button(
            x = button_x,
            y= button_y_quit,
            width= button_width,
            height= button_height,
            text="Quit",
            color=(70, 60, 55),
            text_color=COLOR_TEXT_DEFAULT,
            font= button_font
        )

        # --- 6. Add the created buttons to our list ---
        self.buttons.append(new_game_button)
        self.buttons.append(new_load_button)
        self.buttons.append(quit_button)


    def draw(self):
        """
        Draws the main menu and all of its buttons onto the screen.
        """
        # The main game loop will handle clearing the screen, so we don't do it here.
        # We just need to draw our own components.
        
        # We can loop through our list of buttons and tell each one to draw itself.
        for button in self.buttons:
            button.draw(self.game.surface) # Pass the surface to the button's draw method