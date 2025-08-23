import pygame
from constants import *
from menus.main_menu import MainMenu
from screens.character_creation_screen import CharacterCreationScreen
# ---- Testing imports ----
from engine.data_loader import load_all_abilities, load_all_weapons, load_all_shields, load_all_rings, load_all_charms, load_all_light_armors, load_all_medium_armors, load_all_heavy_armors, load_all_amulets, load_all_equipment
# --- End of Testing imports ---


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Unnamed RPG")
        self.running = True
        self.main_menu = MainMenu(self)
        self.character_creation_screen = CharacterCreationScreen(self)
        self.current_state = self.main_menu
        self.character = None
        self.master_ability_compendium = load_all_abilities()
        self.master_weapon_rack = load_all_weapons()
        self.master_ring_case = load_all_rings()
        self.master_charm_display = load_all_charms()
        self.master_shield_wall = load_all_shields()
        self.master_light_armor_catalogue = load_all_light_armors()
        self.master_medium_armor_catalogue = load_all_medium_armors()
        self.master_heavy_armor_catalogue = load_all_heavy_armors()
        self.master_amulet_case = load_all_amulets()
        self.master_equipment_compendium = load_all_equipment()

        # === Tester functions ---
        
        # --- End of tester Fucntions ---#

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.current_state.handle_event(event)

            self.surface.fill(COLOR_BACKGROUND)
            self.current_state.draw()

            pygame.display.flip()
