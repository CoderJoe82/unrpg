import pygame
from constants import *
from menus.main_menu import MainMenu
from data.character.character_creation import Character
#---- Testing imports ----
from engine.data_loader import load_all_abilities, load_all_weapons, load_all_shields, load_all_rings, load_all_charms, load_all_light_armors, load_all_medium_armors, load_all_heavy_armors, load_all_equipment
#--- End of Testing imports ---



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Unnamed RPG")
        self.title_font = pygame.font.Font(GAME_FONT_PATH, 55)
        self.title_surface = self.title_font.render("Unnamed RPG", True, COLOR_TEXT_DEFAULT)
        self.title_rect = self.title_surface.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * .10))
        self.running = True
        self.main_menu = MainMenu(self)
        self.character = None
        self.master_ability_compendium = load_all_abilities()
        self.master_weapon_rack = load_all_weapons()
        self.master_ring_case = load_all_rings()
        self.master_charm_display = load_all_charms()
        self.master_shield_wall = load_all_shields()
        self.master_light_armor_catalogue = load_all_light_armors()
        self.master_medium_armor_catalogue = load_all_medium_armors()
        self.master_heavy_armor_catalogue = load_all_heavy_armors()
        self.master_equipment_compendium = load_all_equipment()
        #=== Tester functions --- 
        EQUIPPED_GEAR = {
            'head' : {
                'item' : None
            },
            'shoulders' : {
                'item' : None
            },
            'wrist' : {
                'item' : None
            },
            'hands' : {
                'item' : None
            },
            'chest' : {
                'item' : None
            },
            'waist' : {
                'item' : None
            },
            'legs' : {
                'item' : None
            },
            'feet' : {
                'item' : None
            },
            'neck' : {
                'item' : None
            },
            'main_hand' : {
                'item' : None
            },
            'off_hand' : {
                'item' : None
            },
            'fingers' : {
                'ring_1' : None,
                'ring_2' : None
            },
            'charms' : {
                'charm_1' : None,
                'charm_2' : None
            }
        }

        print(EQUIPPED_GEAR['off_hand'])
        # ---- end of tester functions ---
        

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(COLOR_BACKGROUND)
            self.main_menu.draw()
            
            self.surface.blit(self.title_surface, self.title_rect)
            
            pygame.display.flip()

    