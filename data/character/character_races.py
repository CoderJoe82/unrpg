from data.character.character_creation import CharacterRace

# ======================================================================================
# --- CHARACTER RACE DEFINITIONS ---
# This file contains the instantiated objects for each playable character race.
# Each race is created using the CharacterRace blueprint and is designed to fit
# the world's theme of nature and civilization co-existing.
# ======================================================================================

# --- HUMAN ---
human = CharacterRace(
    name="Human",
    description="Adaptable, ambitious, and sociable, Humans are the glue that often holds the diverse cities of the world together. While lacking the deep innate connections of other races, their ingenuity and ability to learn from others is unmatched.",
    racial_abilities=("racial_human_01",),
    racial_stat_bonuses={"charisma": 2, "intelligence": 1},
    size="Medium",
    movement_speed={"land": 30},
    languages=("Common", "Trade Tongue"),
    resistance_bonuses={},
    general_alignment="Any",
    life_span="Typically around 80-100 years.",
    racial_traits=("Adaptable Learner", "Sociable")
)

# --- SYLVAN ELF ---
sylvan_elf = CharacterRace(
    name="Sylvan Elf",
    description="Graceful and patient, Sylvan Elves are the architects of the living world, guiding the growth of trees and plants into breathtaking structures. They see civilization and nature not as two separate things, but as a single, beautiful work of art.",
    racial_abilities=("racial_elf_01",),
    racial_stat_bonuses={"dexterity": 2, "wisdom": 1},
    size="Medium",
    movement_speed={"land": 35},
    languages=("Common", "Elvish"),
    resistance_bonuses={"nature": 15},
    general_alignment="Often Good or Neutral.",
    life_span="Can live for over 700 years.",
    racial_traits=("Fey Ancestry", "Keen Senses", "Green Thumb")
)

# --- STONEHEART DWARF ---
stoneheart_dwarf = CharacterRace(
    name="Stoneheart Dwarf",
    description="Resilient and stout, the Stoneheart Dwarves live in harmony with the mountains. They are masters of geomancy and artisanship, carving breathtaking cities within the earth and cultivating veins of crystal and ore like gardens.",
    racial_abilities=("racial_dwarf_01",),
    racial_stat_bonuses={"strength": 2, "constitution": 1},
    size="Medium",
    movement_speed={"land": 25},
    languages=("Common", "Dwarvish"),
    resistance_bonuses={"frost": 10, "physical": 5}, # Naturally hardy
    general_alignment="Often Lawful.",
    life_span="Around 350 years.",
    racial_traits=("Darkvision", "Stonecunning", "Poison Resilience")
)

# --- VERDANT ---
verdant = CharacterRace(
    name="Verdant",
    description="Born from the great Seed-Trees, the Verdant are sentient, humanoid plants. Their bark-like skin and leafy hair change with the seasons. Deeply connected to the cycle of life, they are patient, resilient, and possess a unique understanding of the natural world.",
    racial_abilities=("racial_verdant_01",),
    racial_stat_bonuses={"wisdom": 2, "constitution": 1},
    size="Medium",
    movement_speed={"land": 30},
    languages=("Common", "Sylvan"),
    resistance_bonuses={"nature": 20},
    general_alignment="Often Neutral.",
    life_span="Varies wildly, from 200 to over 1,000 years.",
    racial_traits=("Barkskin", "Plant Communication", "Seasonal Adaptation")
)

# --- GEODEKIN ---
geodekin = CharacterRace(
    name="Geodekin",
    description="Living, crystalline beings who grow slowly over millennia. The Geodekin are logical, thoughtful, and see the world in terms of intricate patterns. Their very bodies are inherently tough, allowing them to shrug off physical blows.",
    racial_abilities=("racial_geodekin_01",),
    racial_stat_bonuses={"intelligence": 2, "strength": 1},
    size="Medium",
    movement_speed={"land": 30},
    languages=("Common", "Terran"),
    resistance_bonuses={"physical": 15}, # Significant innate physical damage reduction
    general_alignment="Often Lawful Neutral.",
    life_span="Ageless, their consciousness persists as long as their crystal form is intact.",
    racial_traits=("Crystalline Form", "Arcane Conduit", "Unaging")
)

# --- KITH'RIN ---
kithrin = CharacterRace(
    name="Kith'rin",
    description="A communal insectoid race renowned for their efficiency and incredible building prowess. Operating with a collective mindset, they create vast, intricate hive-cities from hardened resin and natural fibers. They are pragmatic, community-focused, and surprisingly resourceful.",
    racial_abilities=("racial_kithrin_01",),
    racial_stat_bonuses={"dexterity": 2, "intelligence": 1},
    size="Medium",
    movement_speed={"land": 30},
    languages=("Common", "Kith'rin Sign"),
    resistance_bonuses={"physical": 5}, # Natural chitin plating
    general_alignment="Often True Neutral.",
    life_span="A short but productive 40-50 years.",
    racial_traits=("Chitinous Plating", "Extra Limbs", "Hive-Minded")
)


# --- DICTIONARY OF ALL RACES ---
# A single, accessible dictionary to hold all the defined character races for easy access.
ALL_RACES = {
    "human": human,
    "sylvan_elf": sylvan_elf,
    "stoneheart_dwarf": stoneheart_dwarf,
    "verdant": verdant,
    "geodekin": geodekin,
    "kithrin": kithrin
}