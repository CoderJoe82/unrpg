import pygame
from constants import *
from menus.main_menu import MainMenu
from data.character.character_creation import Character
#---- Testing imports ----
from engine.data_loader import load_all_spells
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

        self.master_spellbook = load_all_spells()


        #=== Tester functions --- 
        ABILITIES = {
            "racial" : (),
            "spell" : (),
            "attack" : (),
            "hot" : ()
        }

        spell_ids = ("nature_007", "nature_005", "nature_012")

        book = self.master_spellbook
        for spell_id in spell_ids:
            if spell_id in book:
                print(book[spell_id]['id'])
                ABILITIES[book[spell_id]['type']] += (book[spell_id]['id'], )




        print(ABILITIES)
        
        #=== end of tester functions---

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(COLOR_BACKGROUND)
            self.main_menu.draw()
            
            self.surface.blit(self.title_surface, self.title_rect)
            
            pygame.display.flip()

    