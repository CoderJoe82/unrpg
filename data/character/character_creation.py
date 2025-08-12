

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
                skills
                 ):
        self.name = name
        self.description = description
        self.primary_resource = primary_resource
        self.unique_mechanics = unique_mechanics if unique_mechanics is not None else ()
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
        self.skills = skills if skills is not None else ()