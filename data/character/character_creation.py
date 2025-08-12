

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
                specializations
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
        self.abilities = starting_abilities if starting_abilities is not None else {}
        self.progression = progression if progression is not None else {}
        self.saving_throw_progression = saving_throw_progression if saving_throw_progression is not None else {}
        self.role_type = role_type
        self.specializations = specializations if specializations is not None else ()
        self.starting_abilities = starting_abilities if starting_abilities is not None else ()

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
        return self.progression.get(character_level, {})
        # <-- This will have more to add here, but for now, I'm leaving it at this.
        
    
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
        self.movement_speed = movement_speed
        self.languages = languages if languages is not None else ()
        self.resistance_bonuses = resistance_bonuses if resistance_bonuses is not None else {}
        self.general_alignment = general_alignment
        self.life_span = life_span

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