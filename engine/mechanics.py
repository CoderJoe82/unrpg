from constants import ARMOR_SCALING_FACTOR, RESISTANCE_SCALING_FACTOR, BASE_XP_TO_LEVEL, RESISTANCES

def calculate_damage_reduction(resistance_value, toughness):
    return resistance_value / (resistance_value + toughness)

def calculate_damage_taken(resistance_value, attack_source, total_armor):
    final_damage = 0
    attack_data = attack_source
    damage_source = attack_data.get('damage_source', 'physical')
    mob_level = attack_data.get('attacker_level', 1)
    damage = attack_data.get('damage_amount', 1)
    resist = resistance_value.get(damage_source, 0)
    character_resistances = resistance_value
    toughness = None

    if damage_source in character_resistances:
        toughness = mob_level * RESISTANCE_SCALING_FACTOR
    else:
        toughness = 1
    
    reduction = calculate_damage_reduction(resist, toughness)
    
    if damage_source == 'physical':
        character_armor_absorption_percentage_percent = total_armor / (total_armor + (ARMOR_SCALING_FACTOR * mob_level))
        value_of_damage_absorbed_by_armor = int(damage * character_armor_absorption_percentage_percent)
        damage_not_mitigated_by_armor = damage - value_of_damage_absorbed_by_armor
        final_damage = damage_not_mitigated_by_armor * (1 - reduction)
    else:
        final_damage = damage * (1 - reduction)

    return final_damage

def calculate_xp_to_next_level(level):
    xp = BASE_XP_TO_LEVEL
    growth_rate = 1.15
    xp_to_level = xp * (growth_rate ** (level - 1))
    return xp_to_level

def get_total_xp_for_level(level):
    xp = 0
    for i in range(1, level):
        xp += calculate_xp_to_next_level(i)
    return xp

def get_equipment_list():
    pass

# def get_hp_bonuses(gear, spell_effect, other)
#     hp_bonuses = 0
#     gear = {
#         "item_hp_bonus" : 2,
#         "item2_hp_bonus" : 4,
#         "item6_hp_bonus" : 6 #<---- these are just exmaples to show my thinking
#     }
#     spell_effect = {}
#     other = {}

#     for equipment in gear:
#         hp_bonuses += gear[equipment]
#     for effect in spell_effect:
#         hp_bonuses += gear[effect]
#     for thing in other:
#         hp_bonuses += other[thing]

#     return hp_bonuses