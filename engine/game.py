import pygame
from constants import *
from engine.data_loader import *
from menus.main_menu import MainMenu

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Unnamed RPG")
        self.running = True
        self.character = None

        self._load_master_data()
        
        self.main_menu = MainMenu(self)
        self.current_state = self.main_menu

    def _load_master_data(self):
        print("Loading game data...")
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

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.current_state.handle_event(event)

            self.surface.fill(COLOR_BACKGROUND)
            self.current_state.draw()
            self.surface.blit(self.current_state.surface, (0, 0))

            pygame.display.flip()