from character_classes import CHARACTER_CLASSES
from character_races import CHARACTER_RACES
from constants import BASE_STATS

class CharacterClass:
    def __init__(self,
                 class_stat_mods, # <-- dictionary
                 class_name, # <-- string
                 class_description, # <-- string
                 primary_stats, # <-- tuple of stat strings to show order of importance of abilities to the class.
                 hit_dice_per_level, # <-- an integer
                 ability_progression, #<-- planned as a dictionary # !!!!!! Note !!!!!! Grab starting abilities from ability_progress's first dictionary item so you're not repeating code.
                 weapon_proficiencies, #<-- planned as a list of weapon types: i.e. 'light' 'medium' 'heavy' etc..
                 armor_proficiencies): # <-- planned as a list of armor types: i.e. 'sword' 'dagger' 'whip' etc..
        self.class_stat_mods = class_stat_mods if class_stat_mods is not None else {} #<-- dictionary
        self.class_name = class_name
        self.class_description = class_description
        self.primary_stats = primary_stats if primary_stats is not None else () # <-- tuple
        self.hit_dice_per_level = hit_dice_per_level # int <-- Later, will be implementing giving the player a choice between the average health of the hit dice number, or letting them let the fate of the dice roll give their hp upgrade on level up.
        self.ability_progression = ability_progression if ability_progression is not None else {} # <-- dictionary
        self.weapon_proficiencies = weapon_proficiencies if weapon_proficiencies is not None else set() # <-- set
        self.armor_proficiencies = armor_proficiencies if armor_proficiencies is not None else set() # <-- set

class CharacterRace:
    def __init__(self,
                race_name, # <-- string
                race_description, # <-- string
                racial_stat_mods, # <-- dictionary
                racial_abilities, # <-- set of strings
                movement_speed, # <-- number
                size, # <-- number
                languages # <-- set
                ):
        self.race_name = race_name
        self.race_description = race_description
        self.racial_stat_mods = racial_stat_mods if racial_stat_mods is not None else {}
        self.racial_abilities = racial_abilities if racial_abilities is not None else set()
        self.movement_speed = movement_speed
        self.size = size
        self.languages = languages if languages is not None else set()


class Character:
    """
    A blueprint for createing all characters in the game, including the player, NPC'S and monsters
    """
    def __init__(self,
                   character_name,
                   max_health, # <-- We don't need to set hp here because we'll use max_hp to also assign it to hp at character creation
                   character_race,
                   character_class,
                   base_stats = None,
                   abilities = None,
                   inventory = None,
                   equipment = None,
                   starting_gold = 0):
        """
        The initializer (or 'constructor') for the Character class.
        This method is called automatically whenever a new character object
        is created. It's where you set up all the starting attributes.

        __init__ The double underscores on either side of init are lines python uses for special built in functions. Init is the one that initializes something.

        'self' refers to the specific object being created.
        """
        # --- Attributes ---
        self.character_name = character_name
        self.max_health = max_health
        self.character_race = character_race
        self.character_class = character_class
        # - These coding functions are saying if no inventory is provided, the inventory defaults to []. Otherwise, it gives the character the inventory provided when made.
        # - The above comment applies to equipment, abilities, and racial abilities.
        self.inventory = inventory if inventory is not None else []
        self.equipment = equipment if equipment is not None else {}
        self.abilities = abilities if abilities is not None else []
        self.racial_abilities = character_race.racial_abilities
        self.base_stats = base_stats if base_stats is not None else {}
        self.starting_gold = starting_gold
        self.stats = {}
        for stat_name, value in base_stats.items():
            bonus = character_race.racial_stat_mods.get(stat_name, 0) + character_class.class_stat_mods.get(stat_name, 0)
            self.stats[stat_name] = value + bonus


        # --- METHODS ---
        pass # <- placeholder for now. Will add methods later.

class Player(Character):
    def __init__(self, character_name, character_race, character_class):
         # This is where the magic happens. We need to gather all the
        # ingredients required by the main Character class's __init__ method.
        # Let's call them one by one.

        # --- Ingredient 1: Max Health ---
        # A level 1 character's health is typically the max value of their class's hit die.
        # We can add a Constitution bonus later, but this is a great start.
        starting_max_health = character_class.hit_dice_per_level

        # --- Ingredient 2: Abilities ---
        # You had a great note about this! We grab the starting abilities
        # from the class's ability progression for level 1.
        # .get(1, []) is a safe way to do this. It gets the list for key 1,
        # or returns an empty list [] if level 1 has no abilities.
        starting_abilities = character_class.ability_progression.get(1, [])
        
        # --- Ingredient 3: Starting Gear/Gold (A thought for the future) ---
        # Your class doesn't have starting gold/inventory yet, but if it did,
        # you'd get it here. For now, we'll use empty defaults.
        starting_inventory = [] # e.g., character_class.starting_inventory
        starting_gold = 0       # e.g., character_class.starting_gold

        # --- Now, we call the parent class's __init__ method (the "super" class) ---
        # We pass it all the ingredients we just prepared.
        super().__init__(
            character_name=character_name,
            max_health=starting_max_health,
            character_race=character_race,
            character_class=character_class,
            base_stats=BASE_STATS.copy(),  # Use a copy so we don't accidentally change the constant
            abilities=starting_abilities,
            inventory=starting_inventory,
            equipment={}, # Players start with nothing equipped
            starting_gold=starting_gold
        )
        
        # We also need to set the player's current health. A new character starts at full health.
        self.current_health = self.max_health

        # Finally, we can add any attributes that are UNIQUE to the Player
        self.level = 1
        self.experience_points = 0


# Character creation flow:
# 1.) Create a function to create a new character.
# 2.) Inside the function, create a variable holding a CharacterClass object with data passed in to fill out the character class.
# 3.) Inside the function, create a variable holding a CharacterRace object with data passed in to fill out the race class.
# 4.) Using those two objects, fill in all the data the Character object needs, which includes data from the two objects now created inside of the object.