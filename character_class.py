class Character:
    """
    A blueprint for createing all characters in the game, including the player, NPC'S and monsters
    """
    def __init__(self,
                   name,
                   health,
                   race,
                   character_class,
                   base_stats,
                   racial_bonus_stats,
                   abilities = None,
                   racial_abilities = None,
                   inventory = None,
                   equipment = None,
                   gold = 0):
        """
        The initializer (or 'constructor') for the Character class.
        This method is called automatically whenever a new character object
        is created. It's where you set up all the starting attributes.

        __init__ The underscores tell python this means make this initialize/work please.

        'self' refers to the specific object being created.
        """
        # --- Attributes ---
        self.name = name
        self.health = health
        self.race = race
        self.character_class = character_class
        self.inventory = inventory if inventory is not None else []
        self.equipment = equipment if equipment is not None else []
        self.abilities = abilities if abilities is not None else []
        self.racial_abilities = racial_abilities if racial_abilities is not None else []
        self.racial_bonuses = racial_bonus_stats
        self.gold = gold
        self.base_stats = base_stats

        # --- METHODS ---
        pass # <- placeholder for now.

