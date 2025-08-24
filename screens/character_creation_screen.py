from phases.welcome_phase import WelcomePhase
from phases.race_selection_phase import RaceSelectionPhase

class CharacterCreationScreen:
    def __init__(self, game):
        self.game = game
        self.current_phase = WelcomePhase(self.game, self)

    def _setup_race_selection_phase(self):
        self.current_phase = RaceSelectionPhase(self.game, self)

    #--- Main draw functions ---
    def draw(self):
        self.current_phase.draw()

    #--- Event Handler---
    def handle_event(self, event):
        self.current_phase.handle_event(event)