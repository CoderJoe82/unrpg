from enum import Enum, auto

# --- character sizes ---
class Size(Enum):
    """
    Represents the size categories for creatures in the game.
    Unsing an Enum prevents typos and makes the code more readable.
    """
    TINY = auto()
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()
    HUGE = auto()
    GARGANTUAN = auto()

# --- The list of primary stats for the game. ---
PRIMARY_STATS = ('Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma')

# --- Equipment slots ---
EQUIPMENT_SLOTS = {
    'main_hand',
    'off_hand',
    'head',
    'shoulders',
    'chest',
    'wrist',
    'hands',
    'waist',
    'legs',
    'feet',
    'ring_one',
    'ring_two',
    'accessory_one',
    'accessory_two'
}

BASE_STATS = {
    "strength" : 10,
    "dexterity" : 10,
    "constitution" : 10,
    "intelligence" : 10,
    "charisma" : 10,
    "wisdom" : 10
}