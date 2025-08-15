from constants import BASE_STATS, ABILITIES
from engine.data_loader import load_all_spells

class CharacterClass:
    def __init__(
                self,
                name,
                description,
                primary_resource,
                unique_mechanics,
                hit_dice,
                bonus_stats,
                passive_ability_bonus,
                starting_equipment,
                armors_allowed,
                weapons_allowed,
                primary_stats,
                starting_abilities,
                progression,
                saving_throw_progression,
                role_type,
                specializations,
                allowed_ability_source
                 ):
        self.name = name
        self.description = description
        self.primary_resource = primary_resource
        self.unique_mechanics = unique_mechanics if unique_mechanics is not None else {}
        self.hit_dice = hit_dice
        self.bonus_stats = bonus_stats if bonus_stats is not None else {}
        self.passive_ability_bonus = passive_ability_bonus if passive_ability_bonus is not None else {}
        self.starting_equipment = starting_equipment if starting_equipment is not None else ()
        self.armors_allowed = armors_allowed if armors_allowed is not None else ()
        self.weapons_allowed = weapons_allowed if weapons_allowed is not None else ()
        self.primary_stats = primary_stats if primary_stats is not None else ()
        self.progression = progression if progression is not None else {}
        self.saving_throw_progression = saving_throw_progression if saving_throw_progression is not None else {}
        self.role_type = role_type
        self.specializations = specializations if specializations is not None else ()
        self.starting_abilities = starting_abilities if starting_abilities is not None else ()
        self.allowed_ability_source = allowed_ability_source if allowed_ability_source is not None else ()

    def get_summary(self):
        class_summary = {
            "name" : self.name,
            "description" : self.description,
            "role" : self.role_type,
            "hit_dice" : self.hit_dice,
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
        if language_name in self.langugaes:
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
                 ):
        self.game = game
        self.character_name = character_name
        self.character_class = character_class if character_class is not None else {}
        self.character_race = character_race if character_race is not None else {}

    def _get_finalized_stats(self):
        finalized_stats = BASE_STATS.copy()
        for stat in self.character_class.bonus_stats:
            finalized_stats[stat] += self.character_class.bonus_stats[stat]
        for stat in self.character_race.racial_stat_bonuses:
            finalized_stats[stat] += self.character_race.racial_stat_bonuses[stat]
        self.finalized_stats = finalized_stats

    def _get_abilities(self, abilities):
        player_abilities = ABILITIES.copy()
        book = self.master_spellbook
        for spell_id in abilities:
            if spell_id in book:
                spell_data = book[spell_id]
                ability_type = spell_data['type']
                player_abilities[ability_type] += (spell_data['id'], )
        return player_abilities

                        # spell_ids = ("nature_007", "nature_005", "nature_012")
        # for spell_id in spell_ids:
        #     for spell in self.master_spellbook.values():
        #         if spell_id == spell['id']:
        #             for spell_type in ABILITIES:
        #                 if spell_type == spell['type']:
        #                     ABILITIES[spell_type] += (spell['id'], )
        # print(ABILITIES)