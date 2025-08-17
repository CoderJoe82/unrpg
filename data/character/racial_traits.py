# New File: data/character/racial_traits.py

# ======================================================================================
# --- RACIAL TRAIT DEFINITIONS ---
# This file contains the data for passive racial traits.
# The game logic will check if a character has a trait (from CharacterRace) and then
# look up its effects here during stat calculations or specific game events.
# ======================================================================================

RACIAL_TRAITS = {
    # --- Human Traits ---
    "Adaptable Learner": {
        "description": "Gain 10% more experience from all sources.",
        "bonus": {"xp_gain_modifier": 0.10}
    },
    "Sociable": {
        "description": "Unlocks unique dialogue options and gain reputation faster.",
        "bonus": {"reputation_gain_modifier": 0.10} # A hook for a future system
    },
    "Skilled": {
        "description": "Your adaptability allows you to master new talents more quickly through practice, increasing your chance to improve skills from use.",
        "bonus": {"skill_up_chance_modifier": 0.10} # A hook for your skill-gain calculations.
    },

    # --- Sylvan Elf Traits ---
    "Fey Ancestry": {
        "description": "You are immune to magical sleep and charm effects.",
        "bonus": {"immunity": ["sleep", "charm"]}
    },
    "Keen Senses": {
        "description": "Your sharp senses allow you to notice subtle details that others might miss, both in your environment and in conversation.",
        "bonus": {"flag": "enhanced_perception"} # A flag for dialogue and exploration systems to check.
    },
    "Green Thumb": {
        "description": "Your innate connection to life makes you more receptive to natural healing.",
        "bonus": {"healing_from_nature_modifier": 0.10}
    },

    # --- Stoneheart Dwarf Traits ---
    "Darkvision": {
        "description": "Accustomed to the dark of the underground, you can see clearly in dim light and darkness.",
        "bonus": {"vision_mode": "darkvision"} # An always on ability that just happens as it gets darker.
    },
    "Stonecunning": {
        "description": "You have an intuitive sense for stonework, allowing you to spot hidden passages in dungeons.",
        "bonus": {"skill": "dungeoneering"} # A hook for a future skill system
    },
    "Poison Resilience": {
        "description": "Your hardy nature grants you significant resistance to poisons.",
        "bonus": {"resistance": {"nature": 20}}
    },

    # --- Verdant Traits ---
    "Barkskin": {
        "description": "Your naturally tough, bark-like skin provides innate protection.",
        "bonus": {"armor": 10}
    },
    "Plant Communication": {
        "description": "You can understand and speak with simple plants, potentially learning secrets of the land.",
        "bonus": {"skill": "nature_lore"}
    },
    "Seasonal Adaptation": {
        "description": "Your form adapts to the environment, granting you minor resistance to the prevailing elements.",
        "bonus": {"dynamic_resistance": "seasonal"} # A hook for a future seasonal system
    },

    # --- Geodekin Traits ---
    "Crystalline Form": {
        "description": "Your body is made of living crystal, making you heavier and more resistant to being moved.",
        "bonus": {"knockback_resistance": 0.50}
    },
    "Arcane Conduit": {
        "description": "Your body naturally stores and channels magic, increasing your maximum mana.",
        "bonus": {"resource_modifier": {"mana": 0.10}}
    },
    "Unaging": {
        "description": "You do not suffer the frailty of old age and cannot be magically aged.",
        "bonus": {"immunity": ["aging"]}
    },

    # --- Kith'rin Traits ---
    "Chitinous Plating": {
        "description": "Your exoskeleton provides an additional layer of protection.",
        "bonus": {"armor": 5}
    },
    "Extra Limbs": {
        "description": "Your smaller, secondary arms aid in grappling and resisting being grappled.",
        "bonus": {"skill": "grapple_advantage"} # A hook for a future combat mechanic
    },
    "Hive-Minded": {
        "description": "Your connection to the Kith'rin collective makes you resistant to mental attacks that cause fear or confusion.",
        "bonus": {"resistance": {"psychic": 25}} # A hook for a future damage type
    }
}