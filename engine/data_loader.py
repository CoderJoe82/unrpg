import json
import glob

def load_all_abilities():
    """
    Finds all JSON files in the data/spells directory and returns a single dictonary of all spells
    """
    path_pattern = "data/spells/*_spells.json"

    all_spells = {}

    spell_files = glob.glob(path_pattern)

    # print(f"Found spell files: {spell_files}")

    for file_path in spell_files:
        with open(file_path, "r") as f:
            data = json.load(f)

            for spell_data in data['spells']:
                spell_id = spell_data['id']
                all_spells[spell_id] = spell_data

    return all_spells

def load_all_weapons():
    """
    Finds all JSON files in the data/weapons directory and returns a single dictionary of all weapons
    """
    path_pattern = "data/weapons/*_weapons.json"

    all_weapons = {}

    weapon_files = glob.glob(path_pattern)

    for file_path in weapon_files:
        with open(file_path, "r") as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_weapons[item['id']] = item
    
    return all_weapons

def load_all_armors():
    """
    Finds all JSON files in the data/armors directory and returns a single dictionary of all armors
    """
    path_pattern = 'data/armors/*_armors.json'

    all_armors = {}

    armor_files = glob.glob(path_pattern)

    for file_path in armor_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_armors[item['id']] = item

    return all_armors