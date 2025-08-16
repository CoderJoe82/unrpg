from data.character.character_creation import CharacterClass

# ======================================================================================
# --- CHARACTER CLASS DEFINITIONS ---
# This file contains the instantiated objects for each playable character class.
# Each class is created using the CharacterClass blueprint and is designed to fit
# the established game data (spells, items, etc.).
# ======================================================================================


# --- MAGE ---
mage = CharacterClass(
    name="Mage",
    description="A scholar of the arcane, the Mage manipulates raw elemental energies to devastating effect, keeping enemies at a distance with potent spells.",
    primary_resource="Mana",
    unique_mechanics={},
    base_hp_per_level=6,
    bonus_stats={"intelligence": 5},
    passive_ability_bonus={"name": "Arcane Attunement", "description": "Naturally regenerates 5% more mana."},
    starting_equipment=("staff_001",),
    armors_allowed=("cloth",),
    weapons_allowed=("staff", "dagger"),
    primary_stats=("intelligence",),
    starting_abilities=("fire_001", "frost_001"),
    progression={},
    resistances_progression={
        5: {"fire": 10, "frost": 10, "lightning": 10},
        10: {"fire": 15, "frost": 15, "lightning": 15}
    }, # Mages attune to the elements they wield, gaining resistance.
    role_type="Ranged Damage",
    specializations=("Pyromancer", "Cryomancer", "Stormcaller"),
    allowed_ability_source=("fire", "frost", "lightning")
)

# --- PALADIN ---
paladin = CharacterClass(
    name="Paladin",
    description="A bastion of faith and steel, the Paladin serves as both a stalwart defender and a source of divine power, able to heal wounds and vanquish darkness.",
    primary_resource="Mana",
    unique_mechanics={},
    base_hp_per_level=10,
    bonus_stats={"strength": 3, "faith": 2},
    passive_ability_bonus={"name": "Aura of Protection", "description": "Reduces magic damage taken by all nearby allies by 5%."},
    starting_equipment=("sword_1h_001", "shield_001"),
    armors_allowed=("cloth", "leather", "mail", "plate", "shield"),
    weapons_allowed=("sword",),
    primary_stats=("strength", "faith"),
    starting_abilities=("holy_001", "holy_002"),
    progression={},
    resistances_progression={
        4: {"holy": 15, "darkness": 10},
        8: {"holy": 15, "darkness": 10}
    }, # Paladins are bastions against divine and profane energies.
    role_type="Hybrid (Tank/Healer/Melee Damage)",
    specializations=("Retribution", "Protection", "Holy"),
    allowed_ability_source=("holy",)
)

# --- WARRIOR ---
warrior = CharacterClass(
    name="Warrior",
    description="A disciplined master of combat, the Warrior uses superior strength and tactics to overwhelm opponents and protect allies, shrugging off blows that would fell lesser fighters.",
    primary_resource="Stamina",
    unique_mechanics={},
    base_hp_per_level=10,
    bonus_stats={"strength": 3, "constitution": 2},
    passive_ability_bonus={"name": "Defensive Stance", "description": "Increases armor value from all equipped gear by 10%."},
    starting_equipment=("sword_1h_001", "shield_001"),
    armors_allowed=("cloth", "leather", "mail", "plate", "shield"),
    weapons_allowed=("sword", "dagger"),
    primary_stats=("strength", "constitution"),
    starting_abilities=("phys_001",),
    progression={},
    resistances_progression={
        3: {"armor": 20},
        6: {"armor": 30},
        9: {"armor": 50}
    }, # Warriors master their armor and become physically tougher.
    role_type="Melee Damage / Tank",
    specializations=("Arms", "Protection"),
    allowed_ability_source=("attack",)
)

# --- ROGUE ---
rogue = CharacterClass(
    name="Rogue",
    description="A master of stealth and subterfuge, the Rogue strikes from the shadows, exploiting weaknesses with poison-laced blades and vanishing before a response can be made.",
    primary_resource="Energy",
    unique_mechanics={"combo_points": "Some abilities generate combo points on a target, which can be spent to unleash powerful finishing moves."},
    base_hp_per_level=8,
    bonus_stats={"dexterity": 5},
    passive_ability_bonus={"name": "Lethality", "description": "Increases critical strike chance with all attacks by 5%."},
    starting_equipment=("dagger_001", "dagger_001"),
    armors_allowed=("cloth", "leather"),
    weapons_allowed=("dagger", "sword"),
    primary_stats=("dexterity",),
    starting_abilities=("phys_002",),
    progression={},
    resistances_progression={
        5: {"nature": 25}
    }, # Rogues build a tolerance to poisons (which are often nature-based).
    role_type="Melee Damage",
    specializations=("Assassination", "Subtlety"),
    allowed_ability_source=("attack",)
)

# --- RANGER ---
ranger = CharacterClass(
    name="Ranger",
    description="A peerless hunter and survivalist, the Ranger is a master of the bow, striking down foes from a distance. Their connection to the wild grants them minor boons from nature.",
    primary_resource="Focus",
    unique_mechanics={},
    base_hp_per_level=8,
    bonus_stats={"dexterity": 4, "wisdom": 1},
    passive_ability_bonus={"name": "Keen Eyes", "description": "Increases accuracy with all ranged attacks by 5."},
    starting_equipment=("bow_001",),
    armors_allowed=("cloth", "leather", "mail"),
    weapons_allowed=("bow", "sword", "dagger"),
    primary_stats=("dexterity", "wisdom"),
    starting_abilities=("nature_001",),
    progression={},
    resistances_progression={
        4: {"nature": 15},
        8: {"armor": 25}
    }, # Rangers are hardy survivalists, resistant to nature and toughened by the wild.
    role_type="Ranged Damage",
    specializations=("Marksmanship", "Beast Mastery"),
    allowed_ability_source=("attack", "nature")
)

# --- DRUID ---
druid = CharacterClass(
    name="Druid",
    description="A versatile guardian of the natural order, the Druid can call upon nature's fury to strike foes, heal allies with restorative magic, or shapeshift into powerful beast forms.",
    primary_resource="Mana",
    unique_mechanics={"shapeshifting": "Can transform into various animal forms, gaining new abilities and roles in combat."},
    base_hp_per_level=8,
    bonus_stats={"wisdom": 3, "intelligence": 2},
    passive_ability_bonus={"name": "Child of the Wild", "description": "Healing-over-time effects you apply are 10% more potent."},
    starting_equipment=("staff_001",),
    armors_allowed=("cloth", "leather"),
    weapons_allowed=("staff", "dagger"),
    primary_stats=("wisdom", "intelligence"),
    starting_abilities=("nature_002", "nature_004"),
    progression={},
    resistances_progression={
        3: {"nature": 20},
        7: {"frost": 15, "fire": 15}
    }, # Druids are one with nature and the core elements.
    role_type="Hybrid (Healer/Ranged Damage/Melee Damage/Tank)",
    specializations=("Balance", "Feral", "Restoration"),
    allowed_ability_source=("nature",)
)

# --- CLERIC ---
cleric = CharacterClass(
    name="Cleric",
    description="A devoted vessel of the divine, the Cleric is a master of restorative and protective magic, mending even the most grievous wounds and shielding allies from harm.",
    primary_resource="Mana",
    unique_mechanics={},
    base_hp_per_level=7,
    bonus_stats={"faith": 4, "wisdom": 1},
    passive_ability_bonus={"name": "Divine Grace", "description": "Direct healing spells you cast have a chance to critically heal for 50% more."},
    starting_equipment=("staff_002",),
    armors_allowed=("cloth", "mail", "shield"),
    weapons_allowed=("staff",),
    primary_stats=("faith", "wisdom"),
    starting_abilities=("holy_001", "holy_004"),
    progression={},
    resistances_progression={
        5: {"holy": 25},
        10: {"darkness": 25}
    }, # Clerics' deep faith shields them from divine forces, both good and evil.
    role_type="Healer",
    specializations=("Discipline", "Holy"),
    allowed_ability_source=("holy",)
)

# --- BERSERKER ---
berserker = CharacterClass(
    name="Berserker",
    description="A whirlwind of pure fury, the Berserker throws caution to the wind, channeling their pain and rage into devastating attacks. The more wounded they are, the more dangerous they become.",
    primary_resource="Rage",
    unique_mechanics={"enrage": "Generates Rage from dealing and taking damage. Spends Rage on powerful attacks. Deals more damage at lower health."},
    base_hp_per_level=12,
    bonus_stats={"strength": 4, "constitution": 1},
    passive_ability_bonus={"name": "Unstoppable", "description": "Reduces the duration of all crowd control effects by 20%."},
    starting_equipment=("sword_2h_001",),
    armors_allowed=("leather", "mail"),
    weapons_allowed=("sword",),
    primary_stats=("strength", "constitution"),
    starting_abilities=("phys_009", "phys_013"),
    progression={},
    resistances_progression={
        5: {"armor": 15},
        10: {"armor": 25}
    }, # Berserkers shrug off physical blows through sheer toughness.
    role_type="Melee Damage",
    specializations=("Fury", "Juggernaut"),
    allowed_ability_source=("attack",)
)


# --- DICTIONARY OF ALL CLASSES ---
# A single, accessible dictionary to hold all the defined character classes for easy access.
ALL_CLASSES = {
    "mage": mage,
    "paladin": paladin,
    "warrior": warrior,
    "rogue": rogue,
    "ranger": ranger,
    "druid": druid,
    "cleric": cleric,
    "berserker": berserker
}