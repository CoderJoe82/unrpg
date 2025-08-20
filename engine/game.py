import pygame
from constants import *
from menus.main_menu import MainMenu
from data.character.character_creation import Character
# ---- Testing imports ----
from engine.data_loader import load_all_abilities, load_all_weapons, load_all_shields, load_all_rings, load_all_charms, load_all_light_armors, load_all_medium_armors, load_all_heavy_armors, load_all_amulets, load_all_equipment
# --- End of Testing imports ---


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.caption = pygame.display.set_caption("Unnamed RPG")
        self.title_font = pygame.font.Font(GAME_FONT_PATH, 55)
        self.title_surface = self.title_font.render(
            "Unnamed RPG", True, COLOR_TEXT_DEFAULT)
        self.title_rect = self.title_surface.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * .10))
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
        self.master_amulet_case = load_all_amulets()
        self.master_equipment_compendium = load_all_equipment()

        # === Tester functions ---
        EQUIPPED_GEAR = {
            'head': {
                'item': {
                    "id": "heavy_head_010",
                    "name": "Crown of the Undaunted",
                    "level": 10,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "head",
                    "description": "A helm worn by a king who never retreated. Its presence grants immunity to fear.",
                    "armor": 75,
                    "scaling": {"strength": 0.5},
                    "effects": [
                        {"type": "passive_buff", "stat": "constitution", "value": 18},
                        {"type": "passive_buff",
                            "stat": "fear_immunity", "value": True}
                    ]
                }
            },
            'shoulders': {
                'item': {
                    "id": "heavy_shoulders_007",
                    "name": "Spaulders of the Juggernaut",
                    "level": 7,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "shoulders",
                    "description": "Huge, layered pauldrons that can absorb the force of a devastating blow.",
                    "armor": 45,
                    "scaling": {},
                    "effects": [
                        {"type": "passive_buff", "stat": "strength", "value": 8}
                    ]
                },
            },
            'wrist': {
                'item': {
                    "id": "heavy_wrist_008",
                    "name": "Vambraces of Retribution",
                    "level": 8,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "wrist",
                    "description": "These forearm guards are covered in holy runes that sometimes lash out when you block an attack.",
                    "armor": 38,
                    "scaling": {"faith": 0.2},
                    "effects": [
                        {"type": "on_block_effect", "effect": {
                            "type": "retaliation_damage", "damage": "2d4", "damage_type": "holy"}}
                    ]
                },
            },
            'hands': {
                'item': {
                    "id": "heavy_hand_004",
                    "name": "Knight's Gauntlets",
                    "level": 4,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "hands",
                    "description": "Finely crafted gauntlets that protect the hand without completely sacrificing dexterity.",
                    "armor": 20,
                    "scaling": {},
                    "effects": [
                        {"type": "passive_buff", "stat": "strength", "value": 3}
                    ]
                },
            },
            'chest': {
                'item': {
                    "id": "heavy_chest_010",
                    "name": "Heart of the Forge",
                    "level": 10,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "chest",
                    "description": "The masterpiece of a legendary dwarven smith, this breastplate is still warm from the forge-fires of a mountain's heart.",
                    "armor": 120,
                    "scaling": {"strength": 0.6},
                    "effects": [
                        {"type": "passive_buff", "stat": "strength", "value": 20},
                        {"type": "passive_buff",
                            "stat": "fire_resistance", "value": 25},
                        {"type": "on_hit_chance", "chance": 0.2, "effect": {
                            "type": "absorb_shield", "health": 150, "duration": 8, "name": "Forgemaster's Ward"}}
                    ]
                }
            },
            'waist': {
                'item': {
                    "id": "heavy_waist_005",
                    "name": "Girdle of the Mountain",
                    "level": 5,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "waist",
                    "description": "A massive belt of steel plates that makes you feel rooted to the ground.",
                    "armor": 25,
                    "scaling": {},
                    "effects": [
                        {"type": "passive_buff", "stat": "constitution", "value": 5}
                    ]
                },
            },
            'legs': {
                'item': {
                    "id": "heavy_legs_009",
                    "name": "Legplates of the Colossus",
                    "level": 9,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "legs",
                    "description": "Impossibly heavy legplates that make you an immovable object on the battlefield.",
                    "armor": 80,
                    "scaling": {"strength": 0.4},
                    "effects": [
                        {"type": "passive_buff", "stat": "constitution", "value": 15},
                        {"type": "passive_buff",
                            "stat": "knockback_resistance", "value": 0.50}
                    ]
                },
            },
            'feet': {
                'item': {
                    "id": "heavy_feet_004",
                    "name": "Knight's Sabatons",
                    "level": 4,
                    "type": "armor",
                    "category": "plate",
                    "equip_slot": "feet",
                    "description": "Reinforced steel boots designed to withstand the crushing weight of a cavalry charge.",
                    "armor": 22,
                    "scaling": {},
                    "effects": [
                        {"type": "passive_buff",
                            "stat": "stun_resistance", "value": 0.10}
                    ]
                },
            },
            'neck': {
                'item': {
                    'amulet_007': {
                        'id': 'amulet_007',
                        'name': "Sorcerer's Eye",
                        'level': 7,
                        'type': 'amulet',
                        'category': 'amulet',
                        'equip_slot': 'neck',
                        'description': 'A polished obsidian sphere set in silver. It seems to find the weaknesses in magical defenses.',
                        'scaling': {},
                        'effects': [
                            {
                                'type': 'passive_buff',
                                'stat': 'intelligence',
                                'value': 10
                            },
                            {
                                'type': 'passive_buff',
                                'stat': 'spell_crit_chance',
                                'value': 7
                            }
                        ]
                    }
                }
            },
            'main_hand': {
                'item': {'heavy_head_001': {
                    'id': 'heavy_head_001',
                    'name': 'Dented Iron Helm',
                    'level': 1, 'type': 'armor',
                    'category': 'plate',
                    'equip_slot': 'head',
                    'description': "A crude, heavy helmet beaten into shape from scrap iron. It's seen a few too many impacts.",
                    'armor': 12,
                    'scaling': {},
                    'effects': []}
                }
            },
            'off_hand': {
                'item': {'heavy_head_001': {
                    'id': 'heavy_head_001',
                    'name': 'Dented Iron Helm',
                    'level': 1, 'type': 'armor',
                    'category': 'plate',
                    'equip_slot': 'head',
                    'description': "A crude, heavy helmet beaten into shape from scrap iron. It's seen a few too many impacts.",
                    'armor': 12,
                    'scaling': {},
                    'effects': []}
                }
            },
            'fingers': {
                'ring_1': {
                    "id": "ring_010",
                    "name": "Archmage's Soulstone",
                    "level": 10,
                    "type": "ring",
                    "equip_slot": "fingers",
                    "description": "A legendary ring housing a crystal that resonates with your own magical essence, sometimes preserving it.",
                    "scaling": {"intelligence": 0.1},
                    "effects": [
                        {"type": "passive_buff", "stat": "intelligence", "value": 20},
                        {"type": "on_spell_cast_chance", "chance": 0.10, "effect": {"type": "buff",
                                                                                    "stat": "mana_cost_reduction_next_spell", "value": 1.0, "duration": 1, "name": "Arcane Clarity"}}
                    ]
                },
                'ring_2': {
                    "id": "ring_009",
                    "name": "Bulwark Ring",
                    "level": 9,
                    "type": "ring",
                    "equip_slot": "fingers",
                    "description": "This wide, adamantine ring occasionally flares with protective energy when you are struck.",
                    "scaling": {},
                    "effects": [
                        {"type": "on_hit_chance", "chance": 0.15, "effect": {
                            "type": "absorb_shield", "health": 100, "duration": 10, "name": "Guardian Ward"}}
                    ]
                },
            },
            'charms': {
                'charm_1': {
                    "id": "charm_010",
                    "name": "Heart of the Aspects",
                    "level": 10,
                    "type": "charm",
                    "equip_slot": "charms",
                    "description": "A legendary artifact that channels raw elemental and arcane power, sometimes aligning perfectly with your own spells.",
                    "scaling": {"intelligence": 0.15},
                    "effects": [
                        {"type": "passive_buff", "stat": "intelligence", "value": 25},
                        {"type": "on_spell_cast_chance", "chance": 0.08, "effect": {"type": "buff",
                                                                                    "stat": "next_spell_free_and_instant", "value": True, "duration": 1, "name": "Flow of Magic"}}
                    ]
                },
                'charm_2': {
                    "id": "charm_009",
                    "name": "Shard of Unstable Power",
                    "level": 9,
                    "type": "charm",
                    "equip_slot": "charms",
                    "description": "This crystalline shard vibrates erratically, occasionally surging with immense power when you engage in combat.",
                    "scaling": {},
                    "effects": [
                        {"type": "on_damage_chance", "chance": 0.15, "effect": {"type": "buff",
                                                                                "stat": "primary_stat_increase", "value": 50, "duration": 8, "name": "Unstable Power"}}
                    ]
                },
            }
        }

        def get_stat_modifiers_from_gear():
            modifiers = []
            gear_list = EQUIPPED_GEAR
            for gear_equip_slot, gear_equipped_dictionary in gear_list.items():
                for gear_item_label, equipped_gear_data in gear_equipped_dictionary.items():
                    gear_slot = gear_equip_slot
                    gear_data = gear_equipped_dictionary
                    gear_full_data = equipped_gear_data
                    # gear_full_data is the right data for the items with only one effect or less
                    only_gear_data = equipped_gear_data.values()
                    only_gear_ids = equipped_gear_data.keys()
                    multi_slot_gear_item = gear_item_label
                    effects_container = {}


                    for data in only_gear_data:
                        
                        if isinstance(data, dict):
                            print(data)
                        # effects = data['effects']
                        # for index, effect in enumerate(effects):
                        #     gear_name = data['name']
                        #     gear_id = data['id']
                        #     effect_type = effect['type']
                        #     effect_stat = effect['stat']
                        #     effect_value = effect['value']
                        #     effects_container[gear_id] = {
                        #         'name': gear_name,
                        #         'effect_type': effect_type,
                        #         'effect_stat': effect_stat,
                        #         'effect_value': effect_value
                        #     }


        get_stat_modifiers_from_gear()
        # --- End of tester Fucntions ---#

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill(COLOR_BACKGROUND)
            self.main_menu.draw()

            self.surface.blit(self.title_surface, self.title_rect)

            pygame.display.flip()
