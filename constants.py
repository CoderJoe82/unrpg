# --- Screen Dimensions ---
SCREEN_WIDTH = 1280  # Let's use a more modern widescreen resolution
SCREEN_HEIGHT = 720

# --- Colors ---
# The "Earthen" Palette
COLOR_BACKGROUND = (40, 35, 30)
COLOR_TEXT_DEFAULT = (220, 215, 200)

# --- Game fonts path ---
GAME_FONT_PATH = "assets/EBGaramond-VariableFont_wght.ttf"

#--- Stats ---
STATS = {
    "strength" : {
        "name" : "Strength",
        "description" : "This governs your pure physical prowess and power"
    },
    "dexterity" : {
        "name" : "Dexterity",
        "description": "This stat governs your reflexes, acrobatics, and all things ability and dodging."
    },
    "constitution" : {
        "name" : "Constitution",
        "description" : "This stat governs your overall health and ability to travel and brush off diseases and other physical ailments"
    },
    "intelligence" : {
        "name" : "Intelligence",
        "description" : "This stat governs your inttelect and gives various bonuses to certain things including many spell critical chance"
    },
    "charisma" : {
        "name" : "Charisma",
        "description" : "This stat governs how well you speak, how appealing you are to those around you, whether it be in appearance or command of those around you."
    },
    "wisdom" : {
        "name" : "Wisdom",
        "description" : "This stat governs your ability to reason things out and also influences a few things. Also is the source of magic for druids and rangers"
    },
    "faith" : {
        "name" : "Faith",
        "description" : "This stat governs your connection to divinity and holy magics. The stronger it is, the stronger your holy spells are."
    }
}

BASE_STATS = {
    "strength" : 5,
    "dexterity" : 5,
    "constitution" : 5,
    "intelligence" : 5,
    "charisma" : 5,
    "wisdom" : 5,
    "faith" : 5
}

RESISTANCES = {
    "fire" : 0,
    "frost" : 0,
    "darkness" : 0,
    "holy" : 0,
    "lightning" : 0,
    "nature" : 0,
    "psychic" : 0,
    "physical": 0
}

BASE_ARMOR = 0

#--- Abilities---
ABILITIES = {
    "racial" : (),
    "spell" : (),
    "attack" : (),
    "hot" : ()
}

#--- Inventory ---
INVENTORY = {}

#--- Gear ---
EQUIPPED_GEAR = {
    'head' : {
        'item' : None
    },
    'shoulders' : {
        'item' : None
    },
    'wrist' : {
        'item' : None
    },
    'hands' : {
        'item' : None
    },
    'chest' : {
        'item' : None
    },
    'waist' : {
        'item' : None
    },
    'legs' : {
        'item' : None
    },
    'feet' : {
        'item' : None
    },
    'neck' : {
        'item' : None
    },
    'main_hand' : {
        'item' : None
    },
    'off_hand' : {
        'item' : None
    },
    'fingers' : {
        'ring_1' : None,
        'ring_2' : None
    },
    'charms' : {
        'charm_1' : None,
        'charm_2' : None
    }
}

#--- Starting Level ---
PLAYER_STARTING_LEVEL = 1

#--- XP ---
BASE_XP_TO_LEVEL = 1000

#--- Tuning knob ---
ARMOR_SCALING_FACTOR = 50

MAGIC_RESISTANCE_SCALING_FACTOR = 40

HP_PER_CONSTITUTION_POINT = 8

BASE_HP_POOL = 50