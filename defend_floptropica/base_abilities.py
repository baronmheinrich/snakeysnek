# this class defines base abilities for the characters in the game.
# each ability has a name, energy cost, and damage value, and tile ranges
class Abilities:
    def __init__(self, name="Basic Attack", energy_cost=50, damage=100, tile_range=[(0, 0)]):
        self.name = name
        self.energy_cost = energy_cost
        self.damage = damage
        self.tile_range = tile_range

    def __str__(self):
        return f"Ability: {self.name}, Energy Cost: {self.energy_cost}, Damage: {self.damage}, Tile Range: {self.tile_range}"
    
    