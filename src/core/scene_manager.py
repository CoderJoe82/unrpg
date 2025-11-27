"""
Scene management system for the UnRPG game engine.

This module handles switching between different game states (scenes) such as
menus, combat, exploration, and dialogue.
"""

class SceneManager:
    """
    Manages the active scene and delegates update and render calls.

    The SceneManager acts as a state machine controller, holding a reference to
    the current scene and routing game loop calls to it.

    Attributes:
        event_manager (EventManager): Reference to the game's event system.
        current_scene (Scene): The currently active scene, or None if no scene is loaded.
    """
    def __init__(self, event_manager):
        """
        Initializes the SceneManager.

        Args:
            event_manager (EventManager): The game's event management system.
        """
        self.event_manager = event_manager
        self.current_scene = None

    def set_scene(self, scene):
        """
        Switches to a new scene.

        Args:
            scene (Scene): The scene object to activate.
        """
        self.current_scene = scene
        # Optional: Call scene.enter() if it exists later

    def update(self):
        """
        Updates the current scene's state.

        Delegates the update call to the active scene if one exists.
        """
        if self.current_scene is not None:
            self.current_scene.update()

    def render(self, screen):
        """
        Renders the current scene to the screen.

        Args:
            screen (pygame.Surface): The display surface to render onto.
        """
        if self.current_scene is not None:
            self.current_scene.render(screen)