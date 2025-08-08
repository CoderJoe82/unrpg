class DataManager:
    def __init__(self):
        # The manager OWNS the runtime data.
        # It starts empty.
        self.runtime_locations = {}
        self.runtime_items = {}

    def get_location(self, location_id):
        # This is the magic: "Lazy Loading"
        # 1. Has this location already been loaded into memory?
        if location_id in self.runtime_locations:
            return self.runtime_locations[location_id]
        
        # 2. If not, load it FROM THE DISK for the first time.
        #    (This assumes each location is in its own file, e.g., 'data/locations/oakhaven.json')
        else:
            location_data = self._load_location_from_file(location_id)
            self.runtime_locations[location_id] = location_data
            return location_data

    def save_game_data(self): 
        # This is also smarter. It only saves the data that has actually
        # been loaded and is currently in the runtime dictionaries.
        # This keeps save files small.
        save_bundle = {
            "locations": self.runtime_locations,
            "items": self.runtime_items
        }
        return save_bundle