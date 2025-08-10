# We need this, or the game can't run
# We call the game from it's home in the engine folder
import pygame
from engine.game import Game

# --- The Blueprint for our entire game engine ---
# A class is a blueprint. We will create one 'Game' object from this blueprint.



# This is the 'entry point' of our program.
# This code only runs when we execute `main.py` directly.
if __name__ == "__main__":
    # Create an instance of our Game class (build the machine from the blueprint).
    game = Game()
    # Call the `run_game` method to start the engine.
    game.run_game()

# This line is only reached AFTER the `run_game` loop has finished.
# It cleans up all the Pygame modules and closes the window.
pygame.quit()