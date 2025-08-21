from constants import BASE_STATS, ABILITIES, PLAYER_STARTING_LEVEL, RESISTANCES, INVENTORY, EQUIPPED_GEAR, HP_PER_CONSTITUTION_POINT, BASE_HP_POOL
from engine.mechanics import calculate_damage_taken, calculate_xp_to_next_level
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
        self.character_class_name = name
        self.character_class_description = description
        self.character_class_primary_resource = primary_resource
        self.character_class_unique_mechanics = unique_mechanics if unique_mechanics is not None else {}
        self.character_class_base_hp_per_level = base_hp_per_level
        self.character_class_bonus_stats = bonus_stats if bonus_stats is not None else {}
        self.character_class_passive_ability_bonus = passive_ability_bonus if passive_ability_bonus is not None else {}
        self.character_class_starting_equipment = starting_equipment if starting_equipment is not None else ()
        self.character_class_armors_allowed = armors_allowed if armors_allowed is not None else ()
        self.character_class_weapons_allowed = weapons_allowed if weapons_allowed is not None else ()
        self.character_class_primary_stats = primary_stats if primary_stats is not None else ()
        self.character_class_progression = progression if progression is not None else {}
        self.character_class_resistances_progression = resistances_progression if resistances_progression is not None else {}
        self.character_class_role_type = role_type
        self.character_class_specializations = specializations if specializations is not None else ()
        self.character_class_starting_abilities = starting_abilities if starting_abilities is not None else ()
        self.character_class_allowed_ability_source = allowed_ability_source if allowed_ability_source is not None else ()

    def get_summary(self):
        class_summary = {
            "name": self.character_class_name,
            "description": self.character_class_description,
            "role": self.character_class_role_type,
            "base_hp_per_level": self.character_class_base_hp_per_level,
            "passive": self.character_class_passive_ability_bonus,
            "weapons_allowed": self.character_class_weapons_allowed,
            "primary_stats": self.character_class_primary_stats,
            "primary_resource": self.character_class_primary_resource,
            "unique_mechanics": self.character_class_unique_mechanics,
            "armors_allowed": self.character_class_armors_allowed,
            "specializations": self.character_class_specializations,
            "starting_abilities": self.character_class_starting_abilities,
        }
        return class_summary

    def check_proficiencies(self, equipment_type):
        if equipment_type in self.character_class_weapons_allowed or equipment_type in self.character_class_armors_allowed:
            return True
        return False

    def get_benefits_for_level(self, character_level):
        return {
            "progression": self.character_class_progression.get(character_level, {}),
            "resistances_progression": self.character_class_resistances_progression.get(character_level, {}),
        }

    def is_role(self, role_name):
        if role_name == self.character_class_role_type:
            return True
        return False

    def can_learn_ability(self, ability_source):
        if ability_source in self.character_class_allowed_ability_source:
            return True
        return False

    def get_starting_kit(self):
        return {
            "mechanics": self.character_class_unique_mechanics if self.character_class_unique_mechanics is not None else {},
            "starting_equipment": self.character_class_starting_equipment,
            "starting_abilities": self.character_class_starting_abilities,
            "primary_resource": self.character_class_primary_resource,
            "base_hp_per_level": self.character_class_base_hp_per_level,
            "passive_ability_bonus": self.character_class_passive_ability_bonus,
            "bonus_stats": self.character_class_bonus_stats
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
        self.character_race_size = size
        self.character_race_name = name
        self.character_race_description = description
        self.character_race_racial_abilities = racial_abilities if racial_abilities is not None else ()
        self.character_race_racial_stat_bonuses = racial_stat_bonuses if racial_stat_bonuses is not None else {}
        self.character_race_movement_speed = movement_speed if movement_speed is not None else {}
        self.character_race_languages = languages if languages is not None else ()
        self.character_race_resistance_bonuses = resistance_bonuses if resistance_bonuses is not None else {}
        self.character_race_general_alignment = general_alignment
        self.character_race_life_span = life_span
        self.character_race_racial_traits = racial_traits if racial_traits is not None else ()

    def get_summary(self):
        race_summary = {
            "name": self.character_race_name,
            "description": self.character_race_description,
            "racial_abilities": self.character_race_racial_abilities,
            "racial_stat_bonuses": self.character_race_racial_stat_bonuses,
            "size": self.character_race_size,
            "movement_speed": self.character_race_movement_speed,
            "languages": self.character_race_languages,
            "resistance_bonuses": self.character_race_resistance_bonuses,
            "general_alignment": self.character_race_general_alignment,
            "life_span": self.character_race_life_span

        }
        return race_summary

    def get_racial_bonuses(self):
        return {
            "stat_bonuses": self.character_race_racial_stat_bonuses,
            "racial_abilities": self.character_race_racial_abilities,
            "resistance_bonuses": self.character_race_resistance_bonuses,
            "languages": self.character_race_languages,
            # <--- later, skill_bonuses/proficiencies
        }

    def has_trait(self, trait_name):
        if trait_name in self.character_race_racial_traits:
            return True
        return False

    def can_speak(self, language_name):
        if language_name in self.character_race_languages:
            return True
        return False

    def get_speed_in(self, environment_type):
        return self.character_race_movement_speed.get(environment_type, self.character_race_movement_speed['land'])

    # <----- possible future check for if a character has any racial proficiencies.

    # <----- possible subrace method here later.


class Character:
    def __init__(self,
                 game,
                 character_name,
                 character_class,
                 character_race,
                 character_level=PLAYER_STARTING_LEVEL
                 ):
        #--- Non depenant on self functions ---
        self.game = game
        self.character_name = character_name
        self.character_class = character_class if character_class is not None else {}
        self.character_race = character_race if character_race is not None else {}
        self.character_level = character_level
        self.character_is_alive = True
        self.character_xp = 0
        self.character_equipped_gear = copy.deepcopy(EQUIPPED_GEAR)
        #--- self objects dependant on character class and or character race and or gear
        gear_modifiers = self._apply_stat_modifiers_from_gear()
        self.character_stat_modifiers = gear_modifiers['stat_modifiers']
        self.character_active_status_effects = gear_modifiers['effect_statuses']
        self.character_stats = self._get_finalized_stats()
        self.character_abilities = self._get_abilities()
        self.character_starting_inventory = self._get_starting_inventory()
        self.character_resistances = self._get_finalized_resistances()
        self.character_block_chance = 0  # <-- placeholder
        self.character_max_hp = self._get_max_hp()
        #--- self objects dependant on character level and or stats
        self.character_xp_to_next_level = self._get_xp_to_next_level()
        self.character_current_hp = self.character_max_hp

    # --- Stats methods ---

    def _get_finalized_stats(self):
        finalized_stats = BASE_STATS.copy()
        modifiers = self.character_stat_modifiers
        statuses = self.character_active_status_effects
        for stat in self.character_class.character_class_bonus_stats:
            finalized_stats[stat] += self.character_class.character_class_bonus_stats[stat]
        for stat in self.character_race.character_race_racial_stat_bonuses:
            finalized_stats[stat] += self.character_race.character_race_racial_stat_bonuses[stat]
        for stat in modifiers:
            finalized_stats[stat] += modifiers[stat]
        for status in statuses:
            finalized_stats[status] = statuses[status]

        return finalized_stats

    def _get_max_hp(self):        
        class_hp = self.character_class.character_class_base_hp_per_level
        character_level = self.character_level
        hp_pool = BASE_HP_POOL
        class_hp_per_level = class_hp * character_level
        constitution = self.character_stats['constitution']
        constitution_bonus = constitution * HP_PER_CONSTITUTION_POINT

        return hp_pool + class_hp_per_level + constitution_bonus
        
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
        self.character_current_hp = min(
            self.character_max_hp, self.character_current_hp)

    def _get_finalized_resistances(self):
        final_resistances = RESISTANCES.copy()

        race_resistances = self.character_race.character_race_resistance_bonuses
        class_resistances = self.character_class.character_class_resistances_progression
        level = self.character_level

        resistance_bonus = (
            self.character_stats['wisdom'] * 2) + self.character_stats['faith']

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

    # --- Equipment methods ---
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
            equip_slot_allowed_positions = list(
                equipped_gear_list[equip_slot].values())
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
                "type": ed.get('type', 'Type not found'),
                "stat": ed.get('stat', "Stat not found"),
                "value": ed.get('value', "Value not found"),
                "duration": ed.get('duration', 'Duration not found')
            }

            return modifier_data

        for key, value in ed.items():
            if isinstance(value, dict):
                result = self._get_stat_modifiers_from_gear_effects(
                    value, wanted_key, wanted_key_2)

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

    def _add_modifiers_from_equipment(self):
        modifiers = []

        pass

    # def _check_for_equipment_stat_modifiers(self, wanted_key):

    # --- Abilities methods ---

    def _get_abilities(self):
        class_abilities = self.character_class.character_class_starting_abilities
        race_abilities = self.character_race.character_race_racial_abilities
        all_abilities = class_abilities + race_abilities
        player_abilities = ABILITIES.copy()
        book = self.game.master_ability_compendium
        for spell_id in all_abilities:
            if spell_id in book:
                spell_data = book[spell_id]
                ability_type = spell_data['type']
                player_abilities[ability_type] += (spell_data['id'], )
        return player_abilities

    # --- Experience methods ---

    def _get_xp_to_next_level(self):
        xp_needed = calculate_xp_to_next_level(self.character_level)
        return xp_needed

    # --- Inventory methods ---

    def _get_starting_inventory(self):
        starting_equipment = self.character_class.character_class_starting_equipment
        full_equipment_list = self.game.master_equipment_compendium
        character_inventory = INVENTORY.copy()

        for equipment_id in starting_equipment:
            if equipment_id in full_equipment_list:
                equipment_data = full_equipment_list.get(
                    equipment_id, "ID INCORRECT")
                character_inventory[equipment_id] = equipment_data
            else:
                print(f'The object: {equipment_data} was not found')

        return character_inventory

    def _get_gear_player_buffs_and_debuffs_from_gear(self):
        gear_list = self.character_equipped_gear
        gear_effects_data = {}
        for slot_where_gear_is_worn, key_is_id_and_value_is_dictionary_with_item_label_key_and_gear_data_value in gear_list.items():
            gear_slot = slot_where_gear_is_worn
            gear_box_of_each_gear_slot = key_is_id_and_value_is_dictionary_with_item_label_key_and_gear_data_value
            item_label_names = gear_box_of_each_gear_slot.keys()
            for label in item_label_names:
             # <---- Dictionary just holding only gear data
                gear_data = gear_box_of_each_gear_slot[label]
                
                if gear_data:
                    gear_effects = gear_data.get('effects', [])
                    gear_effects_container = []
                    for index, effects in enumerate(gear_effects):
                        if effects['type'] == 'passive_buff' or effects['type'] == 'debuff':
                            gear_effects_container.append(
                                {
                                    'name': gear_data['name'],
                                    'modifier_type': effects['type'],
                                    'stat': effects['stat'],
                                    'value': effects['value']
                                }
                            )
                    gear_effects_data[gear_data['id']] = gear_effects_container
        return gear_effects_data
    
    def _apply_stat_modifiers_from_gear(self):
        final_stat_modifiers = {}
        special_effects_statuses = {}
        stat_modifiers = self._get_gear_player_buffs_and_debuffs_from_gear()
        for key, value in stat_modifiers.items():
            gear_data_list = value
            for gear_data in gear_data_list:
                stat_value = gear_data['value']
                stat_name = gear_data['stat']
                if isinstance(stat_value, (int, float)) and not isinstance(stat_value, bool):
                    if stat_name in final_stat_modifiers:
                        final_stat_modifiers[stat_name] += stat_value
                    else:
                        final_stat_modifiers[stat_name] = stat_value
                else:
                    special_effects_statuses[stat_name] = stat_value
        print([final_stat_modifiers, special_effects_statuses])
        # Possibly adding a feature that measures stat modifier 'priority' numbers so that if a cursed object is equipped that induces fear can negate fear immunity, etc..
        return {
                'stat_modifiers': final_stat_modifiers,
                'effect_statuses': special_effects_statuses
        }

    # --- Area to remind me of things to create ---


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
