# This file contains the data structure to be used for the levels in the game.
# The GameMaster class will manage the levels, characters, enemies, and overall game state.

class GameMaster:
    def __init__(self):
        self.levels = []
        self.current_level = 0
        self.characters = []
        self.enemies = []

    def add_level(self, level):
        self.levels.append(level)

    def start_level(self, level_index):
        if 0 <= level_index < len(self.levels):
            self.current_level = level_index
            # Initialize level-specific data here
            print(f"Starting level {level_index}")
        else:
            print("Invalid level index")

    def add_character(self, character):
        self.characters.append(character)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def get_current_level(self):
        return self.levels[self.current_level] if self.levels else None