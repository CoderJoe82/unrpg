from constants import *
from menus.button import Button
from data.character.character_races import ALL_RACES
from phases.creation_phase_base import CreationPhaseBase

class RaceSelectionPhase(CreationPhaseBase):
    # --- Buttons ---
    BUTTON_WIDTH = 180
    BUTTON_HEIGHT = 60
    BUTTON_PADDING = 15
    RACE_BUTTON_X = SCREEN_WIDTH * 0.02
    RACE_BUTTON_PANEL_PADDING = SCREEN_WIDTH * 0.02
    RACE_BUTTON_PANEL_WIDTH = (RACE_BUTTON_PANEL_PADDING * 2)  + BUTTON_WIDTH
    NAVIGATION_BUTTON_Y = SCREEN_WIDTH * 0.75
    CONFIRM_BUTTON_X = SCREEN_WIDTH * 0.5 #<--- placeholder
    BACK_BUTTON_X = CONFIRM_BUTTON_X + BUTTON_WIDTH + BUTTON_PADDING #<--- placeholder

    # --- Phase title section ---
    TITLE_SECTION_HEIGHT = SCREEN_HEIGHT * 0.2
    TITLE_SECTION_RECT = pygame.Rect(
        RACE_BUTTON_PANEL_WIDTH,
        0,
        SCREEN_WIDTH - RACE_BUTTON_PANEL_WIDTH,
        TITLE_SECTION_HEIGHT
    )
    TITLE_FONT = pygame.font.Font(GAME_FONT_PATH, 48)
    TITLE_TEXT_SURFACE = TITLE_FONT.render("Choose A Race", True, COLOR_TEXT_DEFAULT)
    TITLE_TEXT_RECT = TITLE_TEXT_SURFACE.get_rect(center = TITLE_SECTION_RECT.center)

    # --- Divider Lines ---
    DIVIDERS = [
        ((RACE_BUTTON_PANEL_WIDTH, 0), (RACE_BUTTON_PANEL_WIDTH, SCREEN_WIDTH)),
        ((RACE_BUTTON_PANEL_WIDTH, ), ())
    ]




    def __init__(self, game, character_creation_screen):
        super().__init__(game, character_creation_screen)

        self.selected_race = None
        self.race_buttons_starting_y = None

    def _draw(self):
        pass

    def _handle_even(self):
        pass