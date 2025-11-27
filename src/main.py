"""
The main entry point for the UnRPG application.

This module initializes the game environment and starts the primary game loop.
It serves as the bootstrapper for the entire application.
"""
from src.core.game_loop import GameLoop

def main():
    """
    Initializes the game engine and begins execution.

    Instantiates the GameLoop class and calls its run method to start
    the application lifecycle.
    """
    game_loop = GameLoop()
    game_loop.run()

if __name__ == "__main__":
    main()