import json
import glob

def load_all_spells():
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

