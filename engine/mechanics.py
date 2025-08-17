from constants import ARMOR_SCALING_FACTOR, MAGIC_RESISTANCE_SCALING_FACTOR, BASE_XP_TO_LEVEL, RESISTANCES

def calculate_max_hp(level, constitution, class_hp_per_level):
    BASE_HP = 40
    class_hp = (level - 1) * class_hp_per_level
    con_bonus = constitution * 4
    return BASE_HP + class_hp + con_bonus

def calculate_damage_reduction(resistance_value, toughness):
    return resistance_value / (resistance_value + toughness)

def calculate_damage_taken(resistance_value, attack_source):
    attack_data = attack_source
    damage_source = attack_data.get('damage_source', 'physical')
    mob_level = attack_data.get('attacker_level', 1)
    damage = attack_data.get('damage_amount', 1)
    resist = resistance_value.get(damage_source, 0)
    character_resistances = resistance_value

    if damage_source in character_resistances:
        toughness = mob_level * MAGIC_RESISTANCE_SCALING_FACTOR
    else:
        toughness = 1
    
    reduction = calculate_damage_reduction(resist, toughness)
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