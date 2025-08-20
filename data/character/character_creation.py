from constants import BASE_STATS, ABILITIES, PLAYER_STARTING_LEVEL, RESISTANCES, INVENTORY, EQUIPPED_GEAR
from engine.mechanics import calculate_max_hp, calculate_damage_taken, calculate_xp_to_next_level
import copy

class CharacterClass:
    def __init__(
                self,
                name,
                description,
                primary_resource,
                unique_mechanics,
                base_hp_per_level,
                bonus_stats,
                passive_ability_bonus,
                starting_equipment,
                armors_allowed,
                weapons_allowed,
                primary_stats,
                starting_abilities,
                progression,
                resistances_progression,
                role_type,
                specializations,
                allowed_ability_source
                 ):
        self.name = name
        self.description = description
        self.primary_resource = primary_resource
        self.unique_mechanics = unique_mechanics if unique_mechanics is not None else {}
        self.base_hp_per_level = base_hp_per_level
        self.bonus_stats = bonus_stats if bonus_stats is not None else {}
        self.passive_ability_bonus = passive_ability_bonus if passive_ability_bonus is not None else {}
        self.starting_equipment = starting_equipment if starting_equipment is not None else ()
        self.armors_allowed = armors_allowed if armors_allowed is not None else ()
        self.weapons_allowed = weapons_allowed if weapons_allowed is not None else ()
        self.primary_stats = primary_stats if primary_stats is not None else ()
        self.progression = progression if progression is not None else {}
        self.resistances_progression = resistances_progression if resistances_progression is not None else {}
        self.role_type = role_type
        self.specializations = specializations if specializations is not None else ()
        self.starting_abilities = starting_abilities if starting_abilities is not None else ()
        self.allowed_ability_source = allowed_ability_source if allowed_ability_source is not None else ()

    def get_summary(self):
        class_summary = {
            "name" : self.name,
            "description" : self.description,
            "role" : self.role_type,
            "base_hp_per_level" : self.base_hp_per_level,
            "passive"  : self.passive_ability_bonus,
            "weapons_allowed" : self.weapons_allowed,
            "primary_stats" : self.primary_stats,
            "primary_resource" : self.primary_resource,
            "unique_mechanics" : self.unique_mechanics,
            "armors_allowed" : self.armors_allowed,
            "specializations" : self.specializations,
            "starting_abilities" : self.starting_abilities,

        }        
        return class_summary

    def check_proficiencies(self, equipment_type):
        if equipment_type in self.weapons_allowed or equipment_type in self.armors_allowed:
            return True
        return False
    
    def get_benefits_for_level(self, character_level):
        return {
            "progression": self.progression.get(character_level, {}),
            "saving_throw_progression" : self.saving_throw_progression.get(character_level, {}),
        }

    def is_role(self, role_name):
        if role_name == self.role_type:
            return True
        return False
    
    def can_learn_ability(self, ability_source):
        if ability_source in self.allowed_ability_source:
            return True
        return False
    
    def get_starting_kit(self):
        return {
            "mechanics" : self.unique_mechanics if self.unique_mechanics is not None else {},
            "starting_equipment" : self.starting_equipment,
            "starting_abilities" : self.starting_abilities,
            "primary_resource" : self.primary_resource,
            "hit_dice" : self.hit_dice,
            "passive_ability_bonus" : self.passive_ability_bonus,
            "bonus_stats" : self.bonus_stats
        }

    # --- Finished with methods for CharacterClass. May add more later.
        

class CharacterRace:
    def __init__(
                self,
                name,
                description,
                racial_abilities,
                racial_stat_bonuses,
                size,
                movement_speed,
                languages,
                resistance_bonuses,
                general_alignment,
                life_span,
                racial_traits
                # <-- This will be a spot for skill bonuses
                # <-- This will be a spot for sub races
                # <-- This will be a spot for proficiences
                # <-- For starting location, IF I go into that much.
                 ):
        self.size = size
        self.name = name
        self.description = description
        self.racial_abilities = racial_abilities if racial_abilities is not None else ()
        self.racial_stat_bonuses = racial_stat_bonuses if racial_stat_bonuses is not None else {}
        self.movement_speed = movement_speed if movement_speed is not None else {}
        self.languages = languages if languages is not None else ()
        self.resistance_bonuses = resistance_bonuses if resistance_bonuses is not None else {}
        self.general_alignment = general_alignment
        self.life_span = life_span
        self.racial_traits = racial_traits if racial_traits is not None else ()

    def get_summary(self):
        race_summary = {
            "name" : self.name,
            "description" : self.description,
            "racial_abilities" : self.racial_abilities,
            "racial_stat_bonuses" : self.racial_stat_bonuses,
            "size" : self.size,
            "movement_speed" : self.movement_speed,
            "languages" : self.languages,
            "resistance_bonuses" : self.resistance_bonuses,
            "general_alignment" : self.general_alignment,
            "life_span" : self.life_span

        }
        return race_summary
    
    def get_racial_bonuses(self):
        return {
            "stat_bonuses" : self.racial_stat_bonuses,
            "racial_abilities" : self.racial_abilities,
            "resistance_bonuses" : self.resistance_bonuses,
            "languages" : self.languages,
            # <--- later, skill_bonuses/proficiencies
        }
    
    def has_trait(self, trait_name):
        if trait_name in self.racial_traits:
            return True
        return False

    def can_speak(self, language_name):
        if language_name in self.languages:
            return True
        return False
    
    def get_speed_in(self, environment_type):
        return self.movement_speed.get(environment_type, self.movement_speed['land'])
        
    
    # <----- possible future check for if a character has any racial proficiencies.

    # <----- possible subrace method here later.

class Character:
    def __init__(self,
                 game,
                 character_name,
                 character_class,
                 character_race,
                 character_level = PLAYER_STARTING_LEVEL
                 ):
        self.game = game
        self.character_name = character_name
        self.character_class = character_class if character_class is not None else {}
        self.character_race = character_race if character_race is not None else {}
        self.character_level = character_level
        self.character_stats = self._get_finalized_stats()
        self.character_current_hp = self.character_max_hp
        self.character_abilities = self._get_abilities()
        self.character_starting_inventory = self._get_starting_inventory()
        self.character_is_alive = True
        self.character_xp = 0
        self.character_xp_to_next_level = self._get_xp_to_next_level()
        self.character_resistances = self._get_finalized_resistances()
        self.character_equipped_gear = copy.deepcopy(EQUIPPED_GEAR)
        self.character_active_modifiers = {
            'buffs',
            'debuffs'
        }
        self.charcter_current_armor = 0  #< ---- placeholder
        self.character_block_chance = 0 #<-- placeholder
        
    # --- Stats methods ---

    def _get_finalized_stats(self):
        finalized_stats = BASE_STATS.copy()
        for stat in self.character_class.bonus_stats:
            finalized_stats[stat] += self.character_class.bonus_stats[stat]
        for stat in self.character_race.racial_stat_bonuses:
            finalized_stats[stat] += self.character_race.racial_stat_bonuses[stat]
        return finalized_stats
    
    def _get_hp(self, bonuses):
        base_hp = calculate_max_hp(self.character_level, self.character_stats['constitution'], self.character_class.base_hp_per_level)
        bonuses = ()
        for number in bonuses:
            base_hp += number
        return base_hp
    
    def _take_damage(self, resistance_value, attack_source):
        damage_taken = calculate_damage_taken(resistance_value, attack_source)
        if damage_taken >= self.character_current_hp:
            self.character_current_hp = 0
            self.character_is_alive = False
        else:
            self.character_current_hp -= damage_taken

    def _get_healed(self, healed_amount):
        if self.character_is_alive == False:
            return
        self.character_current_hp += healed_amount
        self.character_current_hp = min(self.character_max_hp, self.character_current_hp)

    def _get_finalized_resistances(self):
        final_resistances = RESISTANCES.copy()

        race_resistances = self.character_race.resistance_bonuses
        class_resistances = self.character_class.resistances_progression
        level = self.character_level


        resistance_bonus = (self.character_stats['wisdom'] * 2) + self.character_stats['faith']

        for resistance in race_resistances:
            final_resistances[resistance] += race_resistances[resistance]

        for keys in class_resistances.keys():
            for key, value in class_resistances[keys].items():
                if level >= keys:
                    if key in final_resistances:
                        final_resistances[key] += value

        for resistance_to_apply_bonus_to in final_resistances:
            final_resistances[resistance_to_apply_bonus_to] += resistance_bonus

        return final_resistances
    
    #--- Equipment methods ---
    
    def _get_equipment(self):
        return self.character_equipped_gear

    def _check_if_slot_full(self, equipped_gear_list, gear_item):
        equip_slot = gear_item.get('equip_slot', "Equipment slot not found")
        main_hand = equipped_gear_list['main_hand'].items()
        off_hand = equipped_gear_list['off_hand'].items()

        if equip_slot == ["main_hand", "off_hand"]:
            for key, value in main_hand:
                if value is not None:
                    return True
            for key, value in off_hand:
                if value is not None:
                    return True
        else:
            equip_slot_allowed_positions = list(equipped_gear_list[equip_slot].values())
            equip_slots_amount = len(equip_slot_allowed_positions)
            if equip_slot in equipped_gear_list:

                if equip_slots_amount > 1:
                    if equip_slot_allowed_positions[0] == None or equip_slot_allowed_positions[1] == None:
                        return False
                    if equip_slot_allowed_positions[0] is not None and equip_slot_allowed_positions[1] is not None:
                        return True
                else:
                    if equip_slot_allowed_positions[0] is not None:
                        return True
                    else:
                        return False
            else:
                print("Could not find slot in equipment slots")
                return

        return False
    
    def _get_stat_modifiers_from_gear_effects(self, effects_dictionary, wanted_key, wanted_key_2):
        ed = effects_dictionary
        if wanted_key in ed or wanted_key_2 in ed:
            modifier_data = {
                "type" : ed.get('type', 'Type not found'),
                "stat" : ed.get('stat', "Stat not found"),
                "value" : ed.get('value', "Value not found"),
                "duration" : ed.get('duration', 'Duration not found')
            }

            return modifier_data
        
        for key, value in ed.items():
            if isinstance(value, dict):
                result = self._get_stat_modifiers_from_gear_effects(value, wanted_key, wanted_key_2)

                if result is not None:
                    return result
                
        return None
    

    def get_stat_modifiers_from_gear(self):
        modifiers = []
        gear_list = self.character_equipped_gear
        for gear_equip_slot, gear_equipped_dictionary in gear_list.items():
            for gear_item, gear_data in gear_equipped_dictionary.items():
                for data_id, data_details in gear_data.items():
                    pass  
                # gear_equip_slot = 'hands', 'neck', etc.
                # gear_equipped_dictionary = {'item' : None}
                # gear_id =    
                
                

    
    #--- Stat modifications ---
    #   THIS IS WHAT i'M WORKING ON TOMORROW, THIS FUNCTION NEEDS MODIFIED. FORGOT TO INCLUDE IF AN ITEM HAS MORE THAN ONE STAT BONUS IN THE SAME ITEM.
    def _add_modifiers_from_equipment(self):
        modifiers = []


        pass
      



    # def _check_for_equipment_stat_modifiers(self, wanted_key):

    
    #--- Abilities methods ---
    
    def _get_abilities(self):
        class_abilities = self.character_class.starting_abilities
        race_abilities = self.character_race.racial_abilities
        all_abilities = class_abilities + race_abilities
        player_abilities = ABILITIES.copy()
        book = self.game.master_ability_compendium
        for spell_id in all_abilities:
            if spell_id in book:
                spell_data = book[spell_id]
                ability_type = spell_data['type']
                player_abilities[ability_type] += (spell_data['id'], )
        return player_abilities    
    
    #--- Experience methods ---        

    def _get_xp_to_next_level(self):
        xp_needed= calculate_xp_to_next_level(self.character_level)
        return xp_needed
    
    #--- Inventory methods ---

    def _get_starting_inventory(self):
        starting_equipment = self.character_class.starting_equipment
        full_equipment_list = self.game.master_equipment_compendium
        character_inventory = INVENTORY.copy()

        for equipment_id in starting_equipment:
            if equipment_id in full_equipment_list:
                equipment_data = full_equipment_list.get(equipment_id, "ID INCORRECT")
                character_inventory[equipment_id] = equipment_data
            else:
                print(f'The object: {equipment_data} was not found')

        return character_inventory
    
    

    
   
   
   
   
   
   
   
   
    #--- Area to remind me of things to create ---


        
    
# STAT & SKILL SYSTEM PHILOSOPHY
# ======================================================================================
# --- CORE STAT & SKILL SYSTEM PHILOSOPHY ---
# This document outlines the guiding principles for character stats, skills, and progression. All future ability and item design should align with this philosophy.
# --- 1. CORE GOALS ---
# Replayability: Encourage players to start new characters to try different builds.
# Experimentation: Support creative and "un-optimized" builds without punishing the player.
# Meaningful Choice: Every point invested and every action taken should feel impactful.
# Avoid "Useless" Builds: No path should lead to a non-viable character.
# --- 2. PRIMARY STATS: The "Foundation and Keystone Model" ---
# Primary stats represent a character's innate talent and core aptitudes. They are improved through deliberate investment upon leveling up.
# 2a. STARTING BASELINE
# All player characters begin with a baseline of 5 in every primary stat.
# This represents a "Competent Adventurer" - capable, but with significant room for growth.
# This ensures a smooth early game and provides good pacing towards the first milestone.
# 2b. THE "FOUNDATION" (Incremental Growth)
# Every single point invested in a primary stat provides a small, direct, and permanent bonus.
# This is the "Foundation" of the build. It guarantees constant, tangible progression.
# Example: +1 Strength might always grant +5 Health and +0.5% Melee Damage.
# This system ensures that no point is ever wasted.
# 2c. THE "KEYSTONES" (Milestone Perks)
# At major stat thresholds (e.g., 25, 50, 75), the player unlocks a "Keystone" perk choice.
# These are powerful, build-defining passive abilities that create a character's unique identity.
# Example: At 25 Dexterity, a player might choose between a "Dual Wielding" perk or a "Lethal Precision" perk that dramatically increases critical damage.
# These Keystone choices are the primary driver for build diversity and replayability.
# --- 3. SKILLS: The "Mastery Through Practice" Model ---
# While primary stats represent innate talent, skills represent learned expertise. They are improved not by spending points, but by taking direct action in the world.
# 3a. LEARNING BY DOING
# The world itself is the training ground. Every relevant action grants a small amount of "skill experience" to the corresponding skill behind the scenes.
# This system rewards active engagement. Brewing a potion improves Alchemy, mining an ore vein improves Mining, and successfully identifying an item improves Identification. The character grows by doing.
# 3b. PASSIVE BENEFITS
# Each level gained in a skill provides a small, incremental, and permanent passive bonus.
# This reflects a growing mastery. For example, a higher Metalsmithing level might slightly reduce the materials needed for crafting, while a higher Herbology level could increase the yield gathered from plants. These bonuses are automatically applied as the skill improves.
# 3c. SKILL CATEGORIES
# Skills are organized into several practical and magical disciplines, including:
# Crafting: Woodworking, Metalsmithing, etc.
# Gathering: Mining, Herbology, Surveying (runecrafting related)
# Magical: Enchanting, Alchemy, Runecrafting
# Practical: Identification, etc.
# ======================================================================================