import pygame
from constants import *
from menus.main_menu import MainMenu
from data.character.character_creation import Character
#---- Testing imports ----
from engine.data_loader import load_all_abilities, load_all_weapons, load_all_armors
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

        # self.character = Character(self)

        self.master_ability_compendium = load_all_abilities()

        self.master_weapon_rack = load_all_weapons()

        self.master_armory = load_all_armors()
        #=== Tester functions --- 

        level = 8
        new_dict = {
            'armor' : 0
        }

        resistances_progression={
            5: {"armor": 15},
            10: {"armor": 25}
        }

            
        for things in resistances_progression.keys():
            for key, value in resistances_progression[things].items():
                if level >= things:
                    print("key", key)
                    print('value', value)
                    new_dict[key] += value

        print("new dict", new_dict)
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

    