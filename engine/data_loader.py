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

def load_all_shields():
    """
    Finds all JSON files in the data/armors directory and returns a single dictionary of all armors
    """
    path_pattern = 'data/armors/shield_armors.json'

    all_shields = {}

    shield_files = glob.glob(path_pattern)

    for file_path in shield_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_shields[item['id']] = item
    
    return all_shields

def load_all_light_armors():
    """
    Finds all JSON files in the data/armors directory and returns a single dictionary of all armors
    """
    path_pattern = 'data/armors/light/light_armors.json'

    all_light_armors = {}

    light_armor_files = glob.glob(path_pattern)

    for file_path in light_armor_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_light_armors[item['id']] = item

    return all_light_armors

def load_all_medium_armors():
    """
    Finds all JSON files in the data/armors directory and returns a single dictionary of all armors
    """
    path_pattern = 'data/armors/shield_armors.json'

    all_medium_armors = {}

    medium_armor_files = glob.glob(path_pattern)

    for file_path in medium_armor_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_medium_armors[item['id']] = item

    return all_medium_armors

def load_all_heavy_armors():
    """
    Finds all JSON files in the data/armors directory and returns a single dictionary of all armors
    """
    path_pattern = 'data/armors/heavy/heavy_armors.json'

    all_heavy_armors = {}

    heavy_armor_files = glob.glob(path_pattern)

    for file_path in heavy_armor_files:
        with open(file_path, 'r') as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_heavy_armors[item['id']] = item

    return all_heavy_armors       

def load_all_rings():
    """
    Finds all JSON files in the data/rings directory and returns a single dictionary of all rings
    """
    path_pattern = "data/rings/rings.json"

    all_rings = {}

    ring_files = glob.glob(path_pattern)

    for file_path in ring_files:
        with open(file_path, "r") as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_rings[item['id']] = item

    return all_rings

def load_all_charms():
    """
    Finds all JSON files in the data/charms directory and returns a single dictionary of all charms
    """
    path_pattern = "data/charms/charms.json"

    all_charms = {}

    charm_files = glob.glob(path_pattern)

    for file_path in charm_files:
        with open(file_path, "r") as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_charms[item['id']] = item

    return all_charms

def load_all_amulets():
    """
    Finds all JSON files in the data/amulets directory and returns a single dictionary of all amulets
    """
    path_pattern = "data/amulets/amulets.json"

    all_amulets = {}

    amulets_files = glob.glob(path_pattern)

    for file_path in amulets_files:
        with open(file_path, "r") as f:
            data = json.load(f)

            for data_info in data.keys():
                for item in data[data_info]:
                    all_amulets[item['id']] = item

    return all_amulets

def load_all_equipment():
    """
    Finds all JSON files that hold equipment items and returns a single dictionary off all the equipment items
    """
    
    path_names = ("data/armors/heavy/heavy_armors.json", "data/armors/medium/medium_armors.json", "data/armors/light/light_armors.json", "data/armors/shield_armors.json", "data/charms/charms.json", "data/rings/rings.json", "data/weapons/*_weapons.json", "data/amulets/amulets.json")

    all_equipment = {}

    for path_name in path_names:
        path_pattern = path_name
        
        equipment_files = glob.glob(path_pattern)

        for file_path in equipment_files:
            with open(file_path, "r") as f:
                data = json.load(f)

                for data_info in data.keys():
                    for item in data[data_info]:
                        all_equipment[item['id']] = item

    return all_equipment