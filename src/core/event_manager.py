class EventManager:
    """
    Handles the publication and subscription of events within the game engine.

    This system allows different components (Input, UI, Game Logic) to communicate
    without direct dependencies (decoupling).

    Plain English:
        Think of this as a central message board.
        - Systems can 'Subscribe' to specific topics (e.g., "I want to know when the mouse clicks").
        - Systems can 'Post' messages to a topic (e.g., "The mouse just clicked!").
        - The sender doesn't need to know who is listening.

    Attributes:
        listeners (dict): A dictionary mapping event types (str) to a list of
                          callback functions.
    """
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        """
        Subscribes a listener function to a specific event type.

        Args:
            event_type (str): The unique identifier for the event (e.g., "MouseClick").
            listener (callable): The function to call when the event is posted.
                                 This function must accept a single argument (the event).
        """
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def post(self, event):
        """
        Broadcasts an event to all subscribed listeners.

        Args:
            event (object): The event object to broadcast. Must have a .type attribute.
        """
        if event.type in self.listeners:
            for listener_function in self.listeners[event.type]:
                listener_function(event)