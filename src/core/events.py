"""
Core event definitions for the UnRPG game engine.

This module contains event classes used by the EventManager to communicate
between different systems without tight coupling.
"""

class QuitEvent:
    """
    Represents a request to terminate the game application.

    This event is posted when the user closes the window or triggers an exit action.
    Listeners (such as GameLoop) subscribe to this event to perform cleanup and shutdown.

    Attributes:
        type (str): Event identifier set to "Quit".
    """
    def __init__(self):
        self.type = "Quit"

class MouseClickEvent:
    """
    Triggered when the user clicks the mouse button.
    
    Attributes:
        type (str): "MouseClick"
        pos (tuple): The (x, y) coordinates of the click.
    """
    def __init__(self, pos):
        self.type = "MouseClick"
        self.pos = pos