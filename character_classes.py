# ===================== IMPORTANT NOTE: THE CURRENT CHARACTERS IN THIS FILE ARE PLACEHOLDERS FOR TESTING IMMEDIATELY =========

CHARACTER_CLASSES = {
    "accountant": {
        "class_name": "Accountant",
        "class_description": "A master of ledgers and loopholes, who vanquishes foes with the sheer force of fiscal policy.",
        "class_stat_mods": {
            "Intelligence": 2,
            "Charisma": 1,
            "Strength": -1  # All that sitting is bad for the muscles
        },
        "primary_stats": ("Intelligence", "Wisdom", "Charisma"), # <-- A tuple, for order!
        "hit_dice_per_level": 6, # Not very sturdy
        "ability_progression": {
            1: {"abilities_learned": ("Audit", "Calculate Interest")},
            2: {"abilities_learned": ("Find Loophole",)},
            3: {"abilities_learned": ("Fiscal Year End Fury",)},
        },
        "weapon_proficiencies": {"sharpened_pencil", "stapler", "heavy_ledger"}, # <-- A set, order doesn't matter
        "armor_proficiencies": {"business_suit", "tie_clip"}
    },

    "professional_napper": {
        "class_name": "Professional Napper",
        "class_description": "A connoisseur of comfort who has mastered the art of strategic slumber, drawing immense power from rest.",
        "class_stat_mods": {
            "Constitution": 2,
            "Wisdom": 1,
            "Dexterity": -1 # A bit groggy
        },
        "primary_stats": ("Constitution", "Wisdom", "Strength"),
        "hit_dice_per_level": 12, # Incredibly resilient
        "ability_progression": {
            1: {"abilities_learned": ("Power Nap", "Strategic Doze")},
            2: {"abilities_learned": ("Summon Pillow",)},
            3: {"abilities_learned": ("Hibernate",)},
        },
        "weapon_proficiencies": {"pillow", "heavy_blanket"},
        "armor_proficiencies": {"pajamas", "slippers", "eye_mask"}
    },
    
    "cat_herder": {
        "class_name": "Cat Herder",
        "class_description": "An individual of impossible patience and lightning-fast reflexes, dedicated to the chaotic art of managing the unmanageable.",
        "class_stat_mods": {
            "Dexterity": 2,
            "Wisdom": 1,
            "Charisma": -1 # Constantly covered in cat hair
        },
        "primary_stats": ("Dexterity", "Wisdom", "Constitution"),
        "hit_dice_per_level": 8,
        "ability_progression": {
            1: {"abilities_learned": ("Laser Pointer Distraction", "Tempting Treat")},
            2: {"abilities_learned": ("Find Lost Toy Under Couch",)},
            3: {"abilities_learned": ("Summon the Herd (Unreliably)",)},
        },
        "weapon_proficiencies": {"feather_wand", "spray_bottle", "catnip_pouch"},
        "armor_proficiencies": {"hoodie", "thick_gloves"}
    }
}