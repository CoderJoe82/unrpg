# ===================== IMPORTANT NOTE: THE CURRENT CHARACTERS IN THIS FILE ARE PLACEHOLDERS FOR TESTING IMMEDIATELY =========

from constants import Size

CHARACTER_RACES = {
    "sentient_rock": {
        "race_name": "Sentient Rock",
        "race_description": "Born of geologic pressure and a stray bolt of wild magic, Sentient Rocks are thoughtful, patient, and incredibly dense. They make for stalwart, if slow, companions.",
        "racial_stat_mods": {
            "Constitution": 2,
            "Strength": 1,
            "Dexterity": -2  # It's hard to be nimble when you're a rock.
        },
        "racial_abilities": {"Stone's Endurance", "Unmoving Resolve", "Geologic Patience"}, # A set of abilities
        "movement_speed": 20, # Very slow
        "size": Size.MEDIUM, # Using the Enum from your constants file
        "languages": {"Terran", "Understands Common"} # A set of languages
    },

    "reformed_mimic": {
        "race_name": "Reformed Mimic",
        "race_description": "Having grown tired of a life of ambushing and being kicked by adventurers, this Mimic has chosen a path of self-improvement and polite conversation. Still a bit sticky, though.",
        "racial_stat_mods": {
            "Strength": 1,
            "Constitution": 1,
            "Charisma": -1 # Years of trickery have made others wary.
        },
        "racial_abilities": {"Minor Shapeshift (Objects)", "Adhesive Grip", "Natural Armor"},
        "movement_speed": 25,
        "size": Size.MEDIUM,
        "languages": {"Common", "Undercommon"}
    },
    
    "sapient_scarecrow": {
        "race_name": "Sapient Scarecrow",
        "race_description": "Animated by harvest spirits and a lingering sense of duty, these beings are surprisingly observant and resilient. They have an irrational fear of fire and a deep love for crows.",
        "racial_stat_mods": {
            "Wisdom": 2,
            "Dexterity": 1,
            "Constitution": -1 # Made of straw and old clothes.
        },
        "racial_abilities": {"Unsettling Gaze", "Stand Unwaveringly", "Immunity to Fear"},
        "movement_speed": 30,
        "size": Size.MEDIUM,
        "languages": {"Common", "Auran"} # Can speak with the wind
    }
}