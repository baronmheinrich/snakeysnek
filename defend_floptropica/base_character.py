# defining a base character class to use for inheritance.
# this class will contain common attributes and methods for all characters in the game.

class BaseCharacter:
    def __init__(self, name="Dummy", movement=1, health=1000, energy=1000, abilityMenu={"attack1": [0, 0], "attack2": [0, 0], "attack3": [0, 0], "attack4": [0, 0]}):
        self.name = name
        self.movement = movement
        self.health = health
        self.energy = energy
        self.abilityMenu = abilityMenu

    def attack(self, target):
        damage = self.energy - target.energy
        damage = max(damage, 0)  # Ensure damage is not negative
        target.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0
    
    def has_energy(self, ability):
        return self.energy >= ability.energy_cost

    def __str__(self):
        return f"{self.name}: Health={self.health}, Energy={self.energy}, Abilities={self.abilityMenu}"