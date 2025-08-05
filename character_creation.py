class CharacterClass:
    def __init__(self, starting_abilities, # <-- list of strings
                 class_stat_bonuses, # <-- dictionary
                 class_name, # <-- string
                 class_description, # <-- string
                 primary_stats, # <-- list of strings to show order of importance of abilities to the class.
                 hit_dice_per_level, # <-- a string something like d10 or d6 depending on class
                 ability_progression, #<-- planned as a dictionary
                 weapon_proficiencies, #<-- planned as a list of weapon types: i.e. 'light' 'medium' 'heavy' etc..
                 armor_proficiencies): # <-- planned as a list of armor types: i.e. 'sword' 'dagger' 'whip' etc..
        self.starting_abilities = starting_abilities
        self.class_stat_bonuses = class_stat_bonuses
        self.class_name = class_name
        self.class_description = class_description
        self.primary_stats = primary_stats
        self.hit_dice_per_level = hit_dice_per_level # <-- Later, will be implementing giving the player a choice between the average health of the hit dice number, or letting them let the fate of the dice roll give their hp upgrade on level up.
        self.ability_progression = ability_progression
        self.weapon_proficiencies = weapon_proficiencies
        self.armor_proficiencies = armor_proficiencies

class CharacterRace:
    def __init__(self,
                name, # <-- string
                description, # <-- string
                racial_stat_mods, # <-- dictionary
                racial_abilities, # <-- list of strings
                movement_speed,
                size,
                languages
                ):
        self.name = name
        self.description = description
        self.racial_stat_mods = racial_stat_mods
        self.racial_abilties = racial_abilities
        self.movement_speed = movement_speed
        self.size = size
        self.languages = languages


class Character:
    """
    A blueprint for createing all characters in the game, including the player, NPC'S and monsters
    """
    def __init__(self,
                   name,
                   max_health, # <-- We don't need to set hp here because we'll use max_hp to also assign it to hp at character creation
                   race,
                   character_class,
                   racial_bonus_stats,
                   base_stats = None,
                   abilities = None,
                   racial_abilities = None,
                   inventory = None,
                   equipment = None,
                   gold = 0):
        """
        The initializer (or 'constructor') for the Character class.
        This method is called automatically whenever a new character object
        is created. It's where you set up all the starting attributes.

        __init__ The double underscores on either side of init are lines python uses for special built in functions. Init is the one that initializes something.

        'self' refers to the specific object being created.
        """
        # --- Attributes ---
        self.name = name
        self.max_health = max_health
        self.race = race
        self.character_class = character_class
        self.base_stats = {}
        # - These coding functions are saying if no inventory is provided, the inventory defaults to []. Otherwise, it gives the character the inventory provided when made.
        # - The above comment applies to equipment, abilities, and racial abilities.
        self.inventory = inventory if inventory is not None else []
        self.equipment = equipment if equipment is not None else {}
        self.abilities = abilities if abilities is not None else []
        self.racial_abilities = racial_abilities if racial_abilities is not None else []
        self.base_stats = base_stats if base_stats is not None else {}
        self.racial_bonus_stats = racial_bonus_stats
        self.gold = gold
        self.stats = {}
        for stat_name, value in base_stats.items():
            bonus = racial_bonus_stats.get(stat_name, 0)
            self.stats[stat_name] = value + bonus


        # --- METHODS ---
        pass # <- placeholder for now. Will add methods later.


# Character creation flow:
# 1.) Create a function to create a new character.
# 2.) Inside the function, create a variable holding a CharacterClass object with data passed in to fill out the character class.
# 3.) Inside the function, create a variable holding a CharacterRace object with data passed in to fill out the race class.
# 4.) Using those two objects, fill in all the data the Character object needs, which includes data from the two objects now created inside of the object.