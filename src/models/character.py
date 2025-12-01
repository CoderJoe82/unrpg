class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1

        self.stats = {
            "Strength" : 10,
            "Dexterity" : 10,
            "Constitution" : 10,
            "Charisma" : 10,
            "Intellect" : 10,
            "Wisdom" : 10,
            "Faith" : 10
        }

        self.max_hp = 100
        self.current_hp = 100
        self.max_mana = 50
        self.current_mana = 50