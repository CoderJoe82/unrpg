"""
Base scene class for the UnRPG game engine.

This module defines the abstract Scene class that all game states
(menus, combat, exploration, etc.) inherit from.
"""

class Scene:
    """
    Abstract base class for all game scenes.

    Scenes represent different game states such as menus, combat encounters,
    dialogue sequences, or exploration areas. All scenes must inherit from
    this class to ensure they implement the required interface.

    Attributes:
        manager (SceneManager): Reference to the scene manager for scene switching.
        events (EventManager): Reference to the event system for communication.
    """
    def __init__(self, manager):
        """
        Initializes the base scene.

        Args:
            manager (SceneManager): The scene manager controlling this scene.
        """
        self.manager = manager
        self.events = manager.event_manager

    def update(self):
        """
        Updates the scene's state logic.

        This method is called once per frame. Override in subclasses to implement
        scene-specific update logic (e.g., handling button states, game logic).
        """
        pass

    def render(self, screen):
        """
        Renders the scene to the display.

        Args:
            screen (pygame.Surface): The display surface to render onto.

        Note:
            Override in subclasses to draw scene-specific graphics.
        """
        pass

    def enter(self):
        """
        Called when the scene becomes the active scene.

        Use this method to initialize scene-specific resources, reset state,
        or perform setup tasks when transitioning into this scene.
        """
        pass

    def exit(self):
        """
        Called when the scene is being replaced by another scene.

        Use this method to clean up resources, save state, or perform
        teardown tasks when transitioning away from this scene.
        """
        pass